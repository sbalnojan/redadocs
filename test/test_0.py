import pytest
import redadocs.dashboards  as rdd

### --------------------------------------------------------------------------------------------------------------------
### Mock the Redash client to run a bunch of tests...
### --------------------------------------------------------------------------------------------------------------------

class mockClient:
    count = 0
    db_dict = {}
    def __init__(self, db_arr):
        self.db_dict["results"]=db_arr
        self.db_dict["count"]=len(db_arr)

    def dashboards(self, page_size=25):
        return self.db_dict

    def update_dashboard(self, dashboard_id, properties={}):
        # get the proper db
        my_db = [cdict for cdict in self.db_dict["results"] if cdict["id"] == dashboard_id][0]
        # update the dict
        new_db = my_db.update(properties)
        self.db_dict["results"].remove(my_db)
        self.db_dict["results"].append(new_db)

    def dashboard(self,slug):
        my_db = [cdict for cdict in self.db_dict["results"] if cdict["slug"] == slug ][0]
        return my_db



### --------------------------------------------------------------------------------------------------------------------
### Tests for module dashboards....
### --------------------------------------------------------------------------------------------------------------------

def test_get_substring_between():
    string = "<PublicLink>htttp://...\nhhdh</PublicLink>"

    assert rdd.get_substring_between(string, "<PublicLink>", "</PublicLink>") == "htttp://...\nhhdh", "Should be a link"

def test_get_db_count():
    client = mockClient({"key":"value"})
    assert rdd.get_db_count(client.dashboards()) == 1, "Should be one"

    client = mockClient([{"key":"value"},{"key":"value"}])
    assert rdd.get_db_count(client.dashboards()) == 2, "Should be two"

def test_get_db_overview():
    client = mockClient([{"key":"value"},{"key":"value"}])

    assert rdd.get_db_overview(client) == "Dashboard Count: 2\n" \
                                      , "Should be an overview..."

def test_get_details():
    db_arr = [{"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST1"
    }, {"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST2"
    }
              ]

    client = mockClient(db_arr)
    assert rdd.get_all_db_details(client) == "## Dashboard Overview \n" \
                                         "### Name: TEST1\n" \
                                         "Tags: ['TEST', 'TEST2'] \n" \
                                         "Updated: 2021-03-08T09:52:12.562Z\n" \
                                         "Archived?: False\n" \
                                         "\n### Name: TEST2\n" \
                                         "Tags: ['TEST', 'TEST2'] \n" \
                                         "Updated: 2021-03-08T09:52:12.562Z\n" \
                                         "Archived?: False\n"

def test_get_db_list():
    db_arr = [{"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST1",
               "slug":"test-1"
    }, {"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST2",
                "slug": "test-2"
    }
              ]

    client = mockClient(db_arr)

    assert rdd.get_db_list(client) == (["test-1","test-2"],["TEST1","TEST2"]), "Should display slugs + names of dashboards"

def test_update_db_list():
    db_arr = [{"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST1",
               "slug":"test-1",
               "id":1
    }, {"tags":['TEST','TEST2'],
               "updated_at":'2021-03-08T09:52:12.562Z',
                "is_archived": False,
               "name": "TEST2",
                "slug": "test-2",
                "id":2
    }
              ]

    client = mockClient(db_arr)

    list_to_update = (["test-1","test-2"],["TESTX","TESTY"])
    rdd.update_db_list(client,list_to_update)
    actual = rdd.get_db_list(client)
    assert actual == (["TESTX","TESTY"]), "Should rename dashboards"

    # from importlib import reload
    # reload(rdd)