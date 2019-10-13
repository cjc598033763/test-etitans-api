# loc2 = ("xpath", '//ul[@role="listbox"]/li[{num}]'.format(num=1))
# print(loc2)
# for i in range(1,9):
#     print(i)
#
#     self.loc3 = ("xpath", "//ul[@role='listbox']/li")

# from xlrd import open_workbook
# a= open_workbook("abc.xls")
# b=a.sheet_by_name("Sheet1")
# c=b.cell_value(0,0).find('${tel}')
# print(c)
tel=123
s='hello'
print(s.find('o'))
if s.find('9')!=-1:
    print(s.find('9'))
    new_s=s.replace('o',str(tel))
    print(new_s)
elif s.find('o')!=-1:
    new_s=s.replace('hello',str(tel+1))
    print(new_s)
else:
    print("88")
from xlrd import open_workbook
from xlutils.copy import copy
def update_():
    tel="13"
    wb=open_workbook("abc.xls")
    wwb=copy(wb)
    sheet=wwb.get_sheet("Sheet1")
    sheet.write(0,0,"11")
    wwb.save("abc.xls")

update_()


