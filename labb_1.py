import justpy as jp
import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# Load data showing percent of women in different majors per year
# wm = pd.read_csv('hm_2.txt')
# data = pd.read_csv('hm_2.txt', sep="\t")
# df = data[["Type", "Art.No","Color", "Price", "Size", "URL", "Pictures"]]
# df.to_excel("hm_raw.xlsx", index=False)
# wm = pd.read_excel("hm_raw.xlsx")
wm = pd.read_csv("picture.csv")

# convert picture string values to match html
picture = '<img src="'+wm['picture'] + '">'

# changing the picture values in dataframe
wm["picture"] = picture
# turning dataframe to dict so it fits on to rowData
dicto = wm.to_dict(orient="records")
# print(dicto)


grid_options = {
    "defaultColDef": {
        "filter": "true",
        "sortable": "true",
        "resizable": "true",
        "cellStyle": {"textAlign": '"center"'},
        "headerClass": 'font-bold'
    },

    "columnDefs": [
      {'headerName': "Item", 'field': "item"},
      {'headerName': "Picture", 'field': "picture"},
      {"headerName": "Enabled", "field": "enabled", "cellRenderer": 'checkboxRenderer'}
    ],
    "rowData": dicto,
}


def grid_change(self, msg):
    print(msg)
def grid_test():
    wp = jp.WebPage()
    grid = jp.AgGrid(a=wp, options=grid_options)
    grid.on('cellValueChanged', grid_change)
    grid.html_columns = [1]

    return wp

jp.justpy(grid_test)
