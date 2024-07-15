import os
from src import call_api
from src.data_driven import excel


def test_from_excel():
    cur_dir = os.path.curdir
    file_path = cur_dir + "/test_api/test_data_files/data.xlsx"
    test_data = excel.excel().get_rows(os.path.abspath(file_path), 'Sheet 1')
    for i in test_data:
        response = call_api.api("POST", "https://postman-echo.com/post?status=200",
                                payload=i)
        assert response.status_code == 200


def test_excel_by_data():
    cur_dir = os.path.curdir
    file_path = cur_dir + "/test_api/test_data_files/data.xlsx"
    test_data = excel.excel().get_row_by_key(os.path.abspath(file_path), 'Sheet 1','Id','A1001')
    response = call_api.api("POST", "https://postman-echo.com/post?status=200",
                            payload=test_data)
    assert response.status_code == 200
