from comtypes.client import CreateObject
import os
import win32com.client

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\data"
print("\n", "project_dir = ", project_dir)
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range("A{}".format(i+1)).Value = "group {}".format(i)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()
