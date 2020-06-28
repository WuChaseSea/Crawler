# -*- coding: utf-8 -*-
import os
import xlsxwriter

'''
@function: 获取该文件夹下的文件列表
'''
def getfilenames(filepath):
    filenames = [] # 定义一个列表来存放所有的文件名

    # 遍历该文件夹下的data文件夹
    # os.walk()返回当前文件夹名，遍历文件夹里的文件夹和文件
    # 完成循环之后， filename是不包含后缀名的文件名列表
    for file_name, folders, files in os.walk(filepath):
        if files: # 如果文件夹列表files不为空的话
            # 截取所有文件名去掉后缀名和点之后的字符，后缀名有4个，加上点号
            # 需要注意的是filenames中每一个元素都是列表
            # 这种file[:-5]的方法具有特殊性，去掉后面的5个字符
            # filenames.append([file[:-5] for file in files])
            # 采用splitext()方法分离文件名和后缀名更为通用
            filenames.append([ os.path.splitext(file)[0] for file in files])
    # 由于data文件夹中只有一层，所以walk()方法只遍历了一遍
    # filenames中只有一个元素
    return filenames

'''
@funtion: 采用os模块写入txt文件
'''
def createtxtfile():
    filenames = getfilenames('data')

    xlsxname = 'students' # 用以统计的表格名
    count = 0
    f = open(xlsxname+'.txt', 'w')
    for filename in filenames:
        # 此处需要注意filenames是一个只有一个元素的列表
        # filename则是包含所有文件夹名的列表
        # 因此需要用name再次进行遍历
        for name in filename:
            f.write(name[:5]+'\t'+name[6:]+'\n')
    f.close()
    print('成功写入TXT文件！')

'''
@funtion: 采用xlsxwriter创建xlsx文件
'''
def createxlsxfile():
    filenames = getfilenames('data')
    workbook = xlsxwriter.Workbook('students.xlsx') # 创建xlsx文件
    students = workbook.add_worksheet('students') # 在xlsx文件中新建一个工作表
    count = 0; # 计数，表示写到该表的第几行
    for filename in filenames:
        for name in filename:
            # 向students表中写入一行，第一行第一列开始写入一个列表
            students.write_row(count, 0, [name[:5], name[6:]])
            count = count + 1 # 即将写入下一行，count加一
    workbook.close()
    print('成功写入xlsx文件！')


if __name__=='__main__':
    createtxtfile()
    createxlsxfile()
