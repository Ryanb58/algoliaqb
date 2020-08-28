from algoliaqb import AlgoliaQueryBuilder


def test_normal_filters():
    aqb = AlgoliaQueryBuilder(
        search_param="search",
        filter_map={
            "is_reported": "is_reported"
        }
    )

    flask_request_args = {
        "is_reported": True
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert filter_query == "is_reported:True"




def test_object_filters():
    aqb = AlgoliaQueryBuilder(
        search_param="search",
        filter_map={
            "status_id": {
                "status_id": "statuses.status_id",
                "group_id": "statuses.group_id"
            },
            "is_reported": "is_reported"
        }
    )

    flask_request_args = {
        "is_reported": True,
        "status_id": 21,
        "group_id": 4
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert "is_reported:True" in filter_query
    assert "statuses.status_id:21" in filter_query
    assert "statuses.group_id:4" in filter_query

    assert filter_query == "(statuses.status_id:21 AND statuses.group_id:4) AND is_reported:True"