# -*- coding: utf-8 -*-

import os
import sys

format_type = 'txt' # 在此处表示标准格式的文件名后缀

if __name__ == '__main__':
    # 也可使用os.getcwd方法获取当前路径
    # 但是需要注意，使用os.getcwd的话
    # python  F:\MyProject\test.py
    # 和进入F:\MyProject文件夹之后再python test.py中
    # 返回结果是不一样的
    # 因为当前的工作目录是不一样的
    files_dir = sys.path[0] + '\data_rename' # 需要更改的文件夹路径
    print('the files in %s will be renamed!' % files_dir) # 打印信息文件即将更改
    # 遍历该文件夹下的所有文件，为了检验是否正确，文件夹中还添加了一个无用的tmp目录
    all_files = [f for f in os.listdir(files_dir)
                 if os.path.isfile(os.path.join(files_dir,f))]
    # 上面需要注意的是os.path.isfile和os.path.isdir两个方法
    # 如果只是文件名的话，则默认是当前路径
    # 而这里明显不能用当前路径，需要使用os.path.join方法
    # os.path.join方法将两个路径连接起来
    print(all_files) # 输出文件夹中的文件
    are_you_sure = input('press y to continue:  ') # 确认是否进行更改
    # 如果不确认更改，退出程序
    if are_you_sure.lower() != 'y':
        print('you entered %s to exit!' % are_you_sure.lower())
        exit()
    filenames = [f for f in all_files] # 获取文件列表
    for filename in filenames: # 遍历文件列表
        # 对每个名称进行文件名和扩展名的分离
        basename, extensionname = os.path.splitext(filename)
        if basename[0] != '1': # 如果文件名不是是1开头的，就说明命名有问题
            name, num = basename.split('-')
            basename = num + '-' + name
            filename_new = basename + extensionname # 文件名重新组合
            # 重命名，需要加上os.path.join方法
            os.rename(os.path.join(files_dir, filename),
                      os.path.join(files_dir, filename_new))
    # 再遍历一遍文件夹得到文件列表并显示
    all_files_new = [f for f in os.listdir(files_dir)
                 if os.path.isfile(os.path.join(files_dir,f))]
    print('the files in %s have been renamed!' % files_dir)
    print(all_files_new)
