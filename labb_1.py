import justpy as jp
import pandas as pd



# Load data showing percent of women in different majors per year
wm = pd.read_csv('picture.csv')


async def grid_test():
    wp = jp.WebPage()
    wm.jp.ag_grid(a=wp)  # a=wp adds the grid to WebPage wp
    img_url = wm['picture'].values
    jp.Img(src=img_url, a=wp, classes='m-2 p-2 cursor-pointer')
    return wp

jp.justpy(grid_test)