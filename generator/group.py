import os
import win32com.client
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for _ in range(random.randrange(maxlen)))


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\data"
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range("A{}".format(i+1)).Value = random_string(15)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()
