from algoliaqb import AlgoliaQueryBuilder


def test_normal_filters():
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
        "is_reported": True
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert filter_query == "is_reported:True"
