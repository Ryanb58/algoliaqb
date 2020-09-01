# Algolia Query Builder

A library to help build queries for searching Algolia.

This package is meant to be used with the [algoliasearch](https://github.com/algolia/algoliasearch-client-python) library.

[![PyPI version](https://badge.fury.io/py/algoliaqb.svg)](https://badge.fury.io/py/algoliaqb)


### Problem:

An app I have been working on has a few points of code duplication and increased complexity. This package is a way for me to fix those issues and increase readability.

### Installation

```
pip install algoliaqb
```


### Filter Strings

By default `filter_map` considers all input as strings. This is pretty straight forward. Lets say for example you have the following filter map:

```
filter_map = {
    "group_id": "tenant_id",
}
```

with the following `flask.args`:

```
{
    "group_id": 1
}
```

AlgoliaQB will look for `group_id` within `flask.args`, grab the value, then remap the key and value for you.

```
tenant_id:1
```

Now lets try an example with a few more filters.

```
filter_map = {
    "group_id": "tenant_id",
    "is_reported": "is_reported"
}
```

with the following `flask.args`:

```
{
    "group_id": 1,
    "is_reported": "true
}
```

The returned filter_string is as follows.

```
tenant_id:1 AND is_reported:true
```

### Library Usage Example:

```python
from algoliasearch.search_client import SearchClient
from algoliaqb import AlgoliaQueryBuilder
from flask import request


aqb = AlgoliaQueryBuilder(
    search_param="search",
    filter_map={
        "group_id": "tenant_id",
        "is_reported": "is_reported"
    }
)

# Extract the search query from our flask apps request.args var.
search_query = aqb.get_search_query(request.args)
# Get the filter query from our request args.
filter_query = aqb.get_filter_query(request.args)

# Now that we have the filter string, we just pass it into the search function.

search_client = SearchClient()
index = search_client.init_index("contacts")
results = index.search(search_query, {"filters": filter_query})
```
