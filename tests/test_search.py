from algoliaqb import AlgoliaQueryBuilder


def test_normal_filters():
    aqb = AlgoliaQueryBuilder(
        search_param="search",
        filter_map={
            "is_reported": "is_reported"
        }
    )

    flask_request_args = {
        "search": None
    }

    search_query = aqb.get_search_query(flask_request_args)

    assert search_query == ""

