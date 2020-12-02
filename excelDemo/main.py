# !/usr/bin/python3
# -*- coding: utf-8 -*-

import xlsxwriter as xw
import pandas as pd
import openpyxl as op

"""
xlsxwriter是一个用于创建Excel .xlsx文件的库。
https://xlsxwriter.readthedocs.io/
写入大.xlsx文件时使用内存优化模式。  
xlrd：用于读取 Excel 文件；xlwt：用于写入 Excel 文件；xlutils：用于操作 Excel 文件的实用工具，比如复制、分割、筛选等；
    
pandas通过对Excel文件的读写实现数据输入输出
http://pandas.pydata.org/
    1、pandas支持.xls，.xlsx文件的读写。
    2、支持只加载每个表的单一工作页。

openpyxl是一个用于读取和编写Excel 2010 xlsx/xlsm/xltx/xltm文件的库。
https://openpyxl.readthedocs.io/en/stable/
    1、openpyxl支持.xlsx文件的读写。
    2、支持Excel操作。
    3、加载大.xlsx文件可以使用read_only模式。
    4、写入大.xlsx文件可以使用write_only模式。
    
对比：
pandas：数据处理是 pandas 的立身之本，Excel 作为 pandas 输入/输出数据的容器
openpyxl：（1）功能较强：一款比较综合的工具，不仅能够同时读取和修改Excel文档，而且可以对Excel文件内单元格进行详细设置，包括单元格样式等内容，图表功能是一亮点，使用openpyxl可以读写xltm, xltx, xlsm, xlsx等类型的文件
          （2）可处理数据量较大的Excel文件，跨平台处理大量数据是其它模块没法相比的。
          （3）因此，openpyxl成为处理Excel复杂问题的首选库函数
          （4）支持读写Excel 2010文档，不支持更早版本
xlsxwriter：（1）功能较强：提供字体设置、前景色背景色、border设置、视图缩放(zoom)、单元格合并、autofilter、freeze panes、公式、data validation、单元格注释、行高和列宽设置等。
            （2）支持数据量大文件写入
            （4）不支持读取和修改，只能用来创建新的文件。你无法做到读出->修改->写回，只能是写入->写入->写入。
            （5）不支持XLS文件：XLS是Office 2013或更早版本所使用的格式
            （6）暂时不支持透视表(Pivot Table）
"""


def get_data():
    orderIds = [1, 2, 3]
    items = ['A', 'B', 'C']
    myData = ["姜子牙", "八佰", "金刚川"]
    testData = [orderIds, items, myData]
    return testData
    # filename2 = '测试2.xlsx'
    # filename3 = '测试3.xlsx'


# xlsxwriter 一行一行写
def xw_toexcel(data, file_name):
    """ 通过 xlsxwriter 方式 """
    # 创建工作簿
    workbook = xw.Workbook(file_name)
    # 创建子表
    worksheet = workbook.add_worksheet("sheet")
    # 激活表
    worksheet.activate()
    # 设置表头
    title = ['序号', '等级', '名称']
    # 从A1单元格开始写入表头
    worksheet.write_row('A1', title)
    # 从第二行开始写入数据
    i = 2
    for j in range(len(data)):
        insertData = [data[0][j], data[1][j], data[2][j]]
        row = 'A' + str(i)
        worksheet.write_row(row, insertData)
        i += 1
    # 关闭表
    workbook.close()


def pd_toexcel(data, file_name):
    """ pandas方式 """
    # 用字典设置DataFrame所需数据
    dfData = {
        '序号': data[0],
        '等级': data[1],
        '名称': data[2]
    }
    # 创建DataFrame
    df = pd.DataFrame(dfData)
    # 存表，去除原始索引列（0,1,2...）
    df.to_excel(file_name, index=False)


def op_toexcel(data, file_name):
    """ openpyxl方式 """
    # 创建工作簿对象
    wb = op.Workbook()
    # 创建子表
    ws = wb['Sheet']
    # 添加表头
    ws.append(['序号', '等级', '名称'])
    for i in range(len(data[0])):
        d = data[0][i], data[1][i], data[2][i]
        # 每次写入一行
        ws.append(d)
    wb.save(file_name)


def main():
    # xw_toexcel(get_data(), '测试1.xlsx')

    # pd_toexcel(get_data(), '测试2.xlsx')

    op_toexcel(get_data(), '测试3.xlsx')


if __name__ == '__main__':
    main()

