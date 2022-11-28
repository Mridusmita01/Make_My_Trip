# import xlrd
# from Library.config import Config
# path = r'C:\Users\HP\Desktop\pythonProject1\MakeMyTrip\sprint2.xlsx'
#
# class ReadExel:
    # def read_locators(self,sheetname):
    #     workbook = xlrd.open_workbook(Config.Data_path)
    #     worksheet = workbook.sheet_by_name(sheetname)
    #     rows = worksheet.get_rows()
    #     print(rows)
    #     header = next(rows)
    #     d = {}
    #     for row in rows:
    #         d[row[0].value] = (row[1].value,row[2].value)
    #     return d
    #
    # def read_locators_1(self,sheetname):
    #     workbook = xlrd.open_workbook(Config.Data_path)
    #     worksheet = workbook.sheet_by_name(sheetname)
    #     rows = worksheet.get_rows()
    #     columns = worksheet.ncols
    #     print(rows)
    #     header = next(rows)
    #     data = []
    #     for row in rows:
    #         values = ()
    #         for j in range(columns):
    #             values += (row[j].value,)
    #         data.append(values)
    #     return data

import xlrd
from Library.config import Config


class ReadExel:

    def read_test_data(self,sheetname):
        wb = xlrd.open_workbook(Config.Data_path)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header=next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self,sheetname):
        wb = xlrd.open_workbook(Config.Data_path)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d


