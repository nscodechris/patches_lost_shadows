
import pandas as pd

csv_temp_names = []
csv_names = []
txt_names = []
final_list = []


def get_names_if_txt(txt_file):
    with open(txt_file) as file:
        lines = file.readlines()
        for i in lines:
            x = i.replace("\n", "")
            # print(x)
            txt_names.append(x)


def get_names_if_csv(csv_file):
    df = pd.read_csv(csv_file, sep=";")
    # print(df)
    csv_temp_names = df["Name"].values
    for i in csv_temp_names:
        csv_names.append(i)


def make_heading(*args):

    for i in args:
        for x in i:
            # print(x)
            final_list.append({"database": "database1",
                                "name": x})


def write_names_to_txt(write_to):
    to_string = "\n".join(str(elem) + "," for elem in final_list)
    with open(write_to, "a") as f:
        f.write(to_string)
        f.close()


if __name__ == '__main__':
    get_names_if_csv("names.txt")
    make_heading(csv_names)
    write_names_to_txt("final_dict.txt")



