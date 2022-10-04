import pandas as pd
import os
from pathlib import Path
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook



CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class InventoryItems:
    def __init__(self):

        self.store_count = [
            ["test2", 0, 0, ""],
            ["test3", 0, 0, ""],
        ]


create_inventory = InventoryItems()


class MakeExcelFiles:
    def __init__(self):
        # create pandas dataframe from lists of class
        self.df_abreheim_shop_store_count = pd.DataFrame(create_inventory.store_count)



    def write_data(self, sheet_name, folder_name, work_book_name, df_name):
        path = (CURR_DIR_PATH + folder_name + work_book_name)
        # MakeExcelFiles.Remove_password_xlsx(self, path, "five@morning!Mind5")
        wb = load_workbook(path)
        ws = wb["store_count"]
        for r in dataframe_to_rows(df_name, index=False,
                                   header=False):  # No index and don't append the column headers
            ws.append(r)
        wb.save(path)
        # MakeExcelFiles.PassProtect(self, path, "five@morning!Mind5")


    def run_main(self):


        # create excel files

        MakeExcelFiles.write_data(self, "store_count", "\\inventory_items", "\\item_store.xlsx",
                                    self.df_abreheim_shop_store_count)



path = (CURR_DIR_PATH + "\\inventory_items" + "\\item_store.xlsx")
make_excel_files = MakeExcelFiles()
# make_excel_files.run_main()
df = pd.read_excel(path, sheet_name="store_count")
print(df)


