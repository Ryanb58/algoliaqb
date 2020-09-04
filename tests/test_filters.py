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


def test_date_filter():
    aqb = AlgoliaQueryBuilder(
        search_param="search",
        filter_map={
            "group_id":"group_id",
            "created_on": {
                "type": "date",
                "created_on_start": "created_on",
                "created_on_end": "created_on"
            }
        }
    )

    flask_request_args = {
        "group_id": 4,
        "created_on_start":  "1538697600",
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert "created_on > 1538697600" in filter_query
    assert filter_query == "group_id:4 AND created_on > 1538697600"


    flask_request_args = {
        "group_id": 4,
        "created_on_start":  "1538697600",
        "created_on_end":  "1539697800",
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert "created_on:1538697600 TO 1539697800" in filter_query
    assert filter_query == "group_id:4 AND created_on:1538697600 TO 1539697800"

    flask_request_args = {
        "group_id": 4,
        "created_on_end":  "1539697800",
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert "created_on < 1539697800" in filter_query
    assert filter_query == "group_id:4 AND created_on < 1539697800"


def test_not_using_normal_string_filters():
    aqb = AlgoliaQueryBuilder(
        search_param="search",
        filter_map={
            "group_id": "group_id",
            "status_id": {
                "group_id": "statuses.group_id",
                "status_id": "statuses.status_id",
            },
            "is_reported": "is_reported",
            "main_contact_account_id": "main_contact.account_id",
            "created_on": {
                "type": "date",
                "created_on_start": "created_on",
                "created_on_end": "created_on",
            },
            "updated_on": {
                "type": "date",
                "updated_on_start": "updated_on",
                "updated_on_end": "updated_on",
            },
            "referral_source_id": {
                "group_id": "referral_sources.group_id",
                "referral_source_id": "referral_sources.id",
            },
            "tag_id": {
                "group_id": "tags.group_id",
                "tag_id": "tags.id",
            }
        }
    )

    flask_request_args = {
        "page": 1,
        "order_by": "status_custom-position",
        "group_id": 4,
    }

    filter_query = aqb.get_filter_query(flask_request_args)

    assert "group_id:4" in filter_query
    assert filter_query == "group_id:4"
