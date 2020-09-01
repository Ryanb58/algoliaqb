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
        return data.get(self.search_param, None)

    def get_filter_query(self, data):
        """
        Return a filter_query based on the filter_map and Flask's request.args.
        """
        filters = []

        for key, value in self.filter_map.items():
            if key in data.keys():
                # Yep, that bit is in the request. Go get it and add it to
                # our filters.
                if isinstance(value, dict):
                    sub_filters = []
                    for sub_key, sub_value in value.items():
                        sub_filters.append(f"{sub_value}:{data.get(sub_key)}")
                    filters.append(f"({' AND '.join(sub_filters)})")
                else:
                    filters.append(f"{str(value)}:{data.get(key)}")
        return " AND ".join(filters)
