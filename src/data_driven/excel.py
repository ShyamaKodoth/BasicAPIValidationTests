import openpyxl
import pandas
import json
import datetime


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

    # def create_parquet(self, file_path):
    #     excel_data_df = pandas.read_csv(file_path, infer_datetime_format=True)
    #     excel_data_df["TIMESTAMP_VALUE3"] = excel_data_df["TIMESTAMP_VALUE3"] * 1000
    #     excel_data_df["TIMESTAMP_VALUE3"] = excel_data_df["TIMESTAMP_VALUE3"].astype("datetime64[ms]")
    #     excel_data_df["TIMESTAMP_VALUE1"] = pandas.to_datetime(excel_data_df["TIMESTAMP_VALUE1"],
    #                                                            format="%Y-%m-%d %H:%M:%S.%f")
    #     excel_data_df["TIMESTAMP_VALUE1"] = excel_data_df["TIMESTAMP_VALUE1"].astype("datetime64[ms]")
    #     print(excel_data_df["TIMESTAMP_VALUE1"])
    #     print(excel_data_df["TIMESTAMP_VALUE3"])
    #     excel_data_df.to_parquet('date_timestamp4.parquet', times="int96")

    # def create_csv(self, file_path):
    #     df = pandas.read_parquet(file_path)
    #     df.to_csv('filename.csv')
    #     print(df['mdm_maturity_date'])
    #     #print(df['as_of_date', 'call_date', 'dated_date', 'first_cpn_date', 'maturity_date', 'mdm_maturity_date'])

