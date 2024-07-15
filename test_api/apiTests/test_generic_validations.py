from src import call_api
import json
import jsonpath_ng
import jsonschema
import pandas


def test_response_codes():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=200",
                            payload=[{"team": "qa", "status": 200}])
    assert response.status_code == 200


def test_field_in_response():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=200",
                            payload=[{"team": "qa", "status": 200}])
    response = json.loads(response.text)
    id = jsonpath_ng.parse("$.id").find(response)
    assert (id[0].value == 100)


def test_lists_in_response():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=200",
                            payload=[{"team": "qa", "status": 200}])
    expected = [{'apt_no': 111, 'street': 'Palm Grove Blvd', 'state': 'California', 'zip': '89870'},
                {'apt_no': 112, 'street': 'Palm Grove Blvd', 'state': 'California', 'zip': '89870'},
                {'apt_no': 110, 'street': 'Palm Grove Blvd', 'state': 'California', 'zip': '89870'},
                {'apt_no': 1, 'street': 'Plumeria Blvd', 'state': 'Arizona', 'zip': '89880'}]
    response = json.loads(response.text)
    ids = jsonpath_ng.parse("$.data.address[*]").find(response)
    address_list = [a.value for a in ids]
    assert (address_list == expected)


def test_response_time():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=202",
                            payload=[{"team": "qa", "status": 202}])
    elapsed_time = response.elapsed
    elapsed_time_in_seconds = elapsed_time.total_seconds()
    # or use time.time() and subtract end time from start time
    assert elapsed_time_in_seconds < 1.5, "Request took more than 1.5 seconds to run."


def test_response_schema():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=200",
                            payload=[{"team": "qa", "status": 200}])
    response = json.loads(response.text)
    schema = {
        "type": "object",
        "properties": {
            "state": {"type": "string"},
            "id": {"type": "number"},
            "team": {"type": "string"},
            "data": {
                "type": "object",
                "address":
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "apt_no": {"type": "number"},
                                "street": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"}
                            }
                        }
                    }
            }
        },
    }
    assert jsonschema.validate(instance=response, schema=schema) is None, "Schema validation failed."


def test_data_type_of_field_in_array():
    response = call_api.api("POST", "https://672d5343-67ef-4512-8404-978180e2d867.mock.pstmn.io/post?status=201",
                            payload=[{"team": "qa", "status": 201}])
    response = json.loads(response.text)
    data = pandas.json_normalize(response)
    df = pandas.DataFrame(data)
    assert df.id.dtype == "int64", "All records have integer type for id column."



