# -*- coding: utf-8 -*-
# @Time : 2021/7/23 15:20
# @Author : Limusen
# @File : sample

import xlrd
import xlwt
from icecream import ic

# 使用xlrd创建一个工作薄对象
book = r"C:\Users\admin\PycharmProjects\P9_P10selenium2\file\daibi.xlsx"
workbook = xlrd.open_workbook(book)
# 根据工作表的名称创建表格对象
sheet = workbook.sheet_by_name('Sheet1')
# 根据工作表的索引创建表格对象，索引从0开始
sheet = workbook.sheet_by_index(0)
# 获取工作表的总行数
row_count = sheet.nrows  # 结果：5
ic(row_count)
# 获取工作表的总列数
col_count = sheet.ncols  # 结果：5
ic(col_count)

# 以列表的方式返回一行数据，行从0开始
rows = sheet.row(1)  # 表示获取第一行数据  结果：[text:'newdream001', text:'王天', text:'男', number:16.0, number:420.0]
ic(rows)

# 通过行、列坐标创建单元格对象,坐标从0开始
cell = sheet.cell(1, 1)  # 表示第2行第2列的单元格
ic(cell)

# 通过行、列坐标获取单元格的类型（0. empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格））
cell_type = sheet.cell_type(2, 3)  # 表示第3行第4列的单元格类型 结果：2
ic(cell_type)

# 通过行、列坐标获取单元格的值,坐标从0开始
cell_value = sheet.cell_value(1, 0)  # 表示第2行第1列的单元格内的值  结果：newdream001
ic(cell_value  )
