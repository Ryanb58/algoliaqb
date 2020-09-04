class AlgoliaQueryBuilder(object):
    """
    Bridge the divide between flask query params and Algolia search.

    Builds the queries based off of a map.
    """

    def __init__(self, search_param=None, filter_map=None):
        """Constructor"""
        self.search_param = search_param
        self.filter_map = filter_map

    def get_search_query(self, data):
        return data.get(self.search_param, "")

    def get_filter_query(self, data):
        """
        Return a filter_query based on the filter_map and Flask's request.args.
        """
        filters = []

        for key, value in self.filter_map.items():
            #if key in data.keys():
                # Yep, that bit is in the request. Go get it and add it to
                # our filters.
                if isinstance(value, dict):
                    if "type" in value and value.get("type") == "date":
                        filter_str = self.handle_date_filter(value, data)
                        if filter_str:
                            filters.append(filter_str)
                    elif key in data.keys():
                        sub_filters = []
                        for sub_key, sub_value in value.items():
                            sub_filters.append(f"{sub_value}:{data.get(sub_key)}")
                        filters.append(f"({' AND '.join(sub_filters)})")
                elif key in data.keys():
                    filters.append(f"{str(value)}:{data.get(key)}")
        return " AND ".join(filters)

    def handle_date_filter(self, sub_filter_map, data):
        """
        Handle object of date type.

        postfix:
        _start  - Where to start.
        _end    - Where to end.

        Returns None if the keys were not found.
        """
        keys = sub_filter_map.keys()
        start_key = next(filter(lambda x: x.endswith("start"), keys), None)
        end_key = next(filter(lambda x: x.endswith("end"), keys), None)

        if start_key in data.keys() and end_key in data.keys():
            facet_name = sub_filter_map.get(start_key)
            facet_value_start = data.get(start_key)
            facet_value_end = data.get(end_key)

            if not (facet_name and facet_value_start and facet_value_end):
                return None

            return f"{facet_name}:{facet_value_start} TO {facet_value_end}"
        elif start_key in data.keys() and end_key not in data.keys():
            facet_name = sub_filter_map.get(start_key)
            facet_value_start = data.get(start_key)

            if not (facet_name and facet_value_start):
                return None

            return f"{facet_name} > {facet_value_start}"
        elif end_key in data.keys() and start_key not in data.keys():
            facet_name = sub_filter_map.get(start_key)
            facet_value_end = data.get(end_key)

            if not (facet_name and facet_value_end):
                return None

            return f"{facet_name} < {facet_value_end}"
        else:
            return None
