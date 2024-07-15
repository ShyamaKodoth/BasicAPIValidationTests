import openpyxl
import pandas
import json


class excel:

    def get_rows(self, file_path, sheet_name):
        excel_data_df = pandas.read_excel(file_path, sheet_name=sheet_name, header=1)
        json_data = excel_data_df.to_json(orient='records')
        # to dictionary
        output = json.loads(json_data)
        return output

    def get_row_by_key(self, file_path, sheet_name, key, value):
        excel_data_df = pandas.read_excel(file_path, sheet_name=sheet_name, header=1)
        # gets Id column from data frame , r = excel_data_df.get("Id")
        dfa = excel_data_df.loc[excel_data_df[key] == value]
        json_data = dfa.to_json(orient='records')
        # to dictionary
        output = json.loads(json_data)
        return output



