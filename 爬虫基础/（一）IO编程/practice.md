# IO编程实践

## 批量文件统计

情形：在一个文件夹里，存在着某一部门的所有人员的报告，名称全部以序号-姓名的方式进行命名，那么有时需要统计这些已交人员的信息。files_excel.py文件则是将所有人员的信息存到excel表格中去，也包含存到txt文件中去的方法。
假设在data文件夹中存在三个docx文件，需要统计文件信息然后将写入文件中。关键步骤有：
1. 获取data文件夹下的文件列表；
* 采用os.walk()方法遍历该文件夹下的所有文件；
* 采用os.path.splitext()方法将扩展名和文件名分离开
2. 写入txt文件中
* 采用open()方法直接写入内容
3. 写入xlsx文件中
* 经尝试，采用open()方法新建的xlsx和xls文件无法用excel打开
* 所以采用xlsxwriter库
* workbook = xlsxwriter.Workbook()新建xlsx文件
* workbook.add_worksheet()方法新建一个工作表
* write_row()方法向表中写入一行


## 文件批量重命名

在一个文件夹中，存在着某一部门的所有人员的报告，标准格式是序号-姓名的格式，但偶尔也会有人搞错，以姓名-序号的方式命名，这里将统一进行更改。
1. 采用os.listdir()方法获取当前文件夹中的文件列表；
2. 采用os.path.splitext()方法分离扩展名；
3. 采用os.rename()方法进行名称的更改；

## 转换为可执行文件

将已经完成的py文件转换为exe可执行文件

* pyinstaller test.py 如果没有-F参数，那么在dist文件夹中会有一个exe文件，发给别人的时候需要将dist文件夹进行打包；
* pyinstaller -F test.py 有-F参数的话，在dist文件夹中就只有一个exe文件，发给别人的时候只发送这个exe文件就行
