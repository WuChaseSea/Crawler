<!--not to html-->/<!-- not to html -->
# IO编程

## 文件读写

### 打开文件

可能初学者最先想到的就是怎么打开文件，这在编程语句中很简单，一句话的事。在Python中打开文件使用open函数。不妨看看open函数的原型：
open(name[, mode[, buffering]])
在上面的函数式中，参数分别表示：
name： 一个包含了你要访问的文件名称的字符串值；
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)；
buffering：如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认；
	模式	描述
	r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
	rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
	r+	打开一个文件用于读写。文件指针将会放在文件的开头。
	rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
	w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
	ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
假设我有一个test.txt的文件，存储路径是“F:\MyProject\WeChat”，则打开命令可使用 f = open(r'F:\MyProject\WeChat\test.txt')

### 文件读取

在使用open函数打开文件之后，可调用read()一次性将文件内容全部读到内存中，最后返回一个str类型的对象。
	f.read()
调用close()关闭对文件的引用。文件使用完毕后必须关闭，不然文件对象会一直占用系统资源。
为了捕捉程序中可能出现的IO异常，可以使用try…finally语句实现。但在Python中，通常读取文件并读取其中的内容是使用with语句。
	with open(r'F:\MyProject\WeChat\test.txt') as file_reader:
		print(file_reader.read())
read()方法是一次将文件内容读到内存，。但是这样很容易出现内存不足的情况，对于这种容易出现内存不足的大文件读取的情况，可以多次调用read(size)方法，表示一次最多读取size个字节。对于某些文本文件，比如配置文件等，按行读取更合适。Python提供了readline()方法和readlines()方法，readline()方法每次读取一行内容，readlines()一次读取所有内容并返回一个列表。上述代码采用readlines()方法如下：
with open(r'F:\MyProject\WeChat\test.txt') as file_reader:
	for line in file_reader.readlines():
		print(line.strip())  #strip()用于去掉字符串首尾的空格

### 文件写入

写入文件和读文件类似，区别在于写入文件时在打开文件时模式使用'w'或'wb'，表示写入文件或者写入二进制文件。
	f = open(r'F:\MyProject\WeChat\test.txt', 'w')
	f.write('test')
	f.close()
使用with语句写入文件则是：
	with open(r'F:\MyProject\WeChat\test.txt', 'w') as file_writer:
		file_writer.write('test')

## 文件和目录操作

在Python中对文件和目录操作需要包含的模块有os和shutil

os.getcwd()	返回当前Python脚本工作的目录路径
os.listdir()	返回指定目录下的所有文件和目录名
os.remove(filepath)	删除一个文件
os.removedirs()	删除多个空目录
os.path.isfile(filepath)	判断给出的路径是否是一个文件
os.path.isdir(filepath)	判断给出的路径是否是一个目录
os.patg.isabs()	判断给出的路径是否是绝对路径
os.path.exists()	判断给出的路径是否存在
os.path.split()	分离一个路径的目录名和文件名，结果返回一个元组
os.path.splitext()	分离扩展名，结果返回一个元组
os.path.dirname(filepath)	获取路径名
os.path.basename(filepath)	获取文件名
os.getenv()	读取环境变量
os.putenv()	设置环境变量
os.linesep	返回当前平台使用的行终止符。Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.name	返回当前正在使用的平台。Windows使用'nt'，Linux/Unix返回'posix'
os.rename(old, new)	重命名文件或者目录
os.makedirs()	创建多级目录
os.mkdir()	创建单个目录
os.stat(file)	获取文件属性
os.chmod(file)	修改文件权限与时间戳
os.path.getsize(filename)	获取文件大小
shutil.copytree(olddir, newdir)	复制文件夹
shutil.copyfile(oldfile, newfile)	复制文件，oldfile和newfile都只能是文件
shutil.copy(oldfile, newfile)	复制文件，oldfile只能说文件， newfile可以是文件，也可以是目标目录
shutil.move(oldpos, newpos)	移动文件或者目录
os.rmdir(dir)	删除目录，但只能删除空目录
shutil.rmtree(dir)	删除目录，空目录和有内容的目录都可以删除

## 序列化操作

在程序运行过程中，会产生很多变量，但是，程序一结束或者意外中断的话，程序中的内存变量都会被操作系统回收。但是，有时我们需要将这些内存中的变量进行存储或者传输，该过程就是序列化操作。
内存中的变量进行序列化之后，可以将其写入磁盘，或者进行传输操作到别的机器上，以实现程序状态的保存和共享，反过来，将变量内容从序列化的对象中读取到内存中来的过程，被称为反序列化。
在Python中，提供了cPickle和pickle两个模块实现序列化。cPickle是由C语言编写的，效率更高，两个模块的功能一模一样。一般优先考虑导入cPickle模块：
try:
	import cPickle as pickle
except ImportError:
	import pickle
在pickle模块中，实现序列化使用dumps方法或者dump方法。
impoet pickle
d = dict{name='Peter', age=18}
pickle.dumps(s)
pickle.dumps()方法将任意对象序列化为一个bytes，然后就可以将这个bytes写入文件。或者使用dump方法直接将对象序列化并写入文件。
f = open(r'F:\MyProject\WeChat\test.txt', 'wb')
pickle.dump(d, f)
f.close()
当需要将对象从磁盘读到内存中来，可以先将内容读到一个bytes，然后使用pickle.loads()方法反序列化出对象。也可以直接使用pickle.load()方法反序列化出对象：
f = open(r'F:\MyProject\WeChat\test.txt', 'rb')
d = pickle.load(f)
f.close()
需要注意的是，反序列化出的变量与原变量没有什么关系，只是内容一样。在爬虫中，经常需要将对象序列化为XML或者JSON格式。
