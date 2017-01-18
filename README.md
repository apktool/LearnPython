
[TOC]

# 查看帮助

help(list)

dir(list)

# 判断类型

isinstance(tmp,str)
type(tmp)

# list

- 空列表

```python
temp=[]
```

- 显示list类的所有方法

## 排序

```python
list2.sort()
```

## 反向排序

```python
list2.sort(reverse=True)
```

# tuple

## 空元祖

```python
temp=()
```

## 空元祖需要注意，重点是逗号，而不是括号。

```python
temp=(1)
temp=(1,)
temp=1,
temp=2,3,4

type(temp)
```

## 元组添加元素

```python
temp=(0,1,2,4,5,6)
temp=temp[:3]+(3,)+temp[3:]
```

## 元祖删除元素

```python
del temp
```

# string

|符号|说明|
|:--|:--|
| capitalize() | 把字符串的第一个字符改为大写 |
| casefold() | 把整个字符串的所有字符改为小写 |
| center(width) | 将字符串居中，并使用空格填充至长度 width 的新字符串 |
| count(sub[, start[, end]]) | 返回 sub 在字符串里边出现的次数，start 和 end 参数表示范围，可选 |
| encode(encoding='utf-8', errors='strict') | 以 encoding 指定的编码格式对字符串进行编码 |
| endswith(sub[, start[, end]]) | 检查字符串是否以 sub 子字符串结束，如果是返回 True，否则返回 Falsestart 和 end 参数表示范围，可选 |
| expandtabs([tabsize=8]) | 把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8 |
| find(sub[, start[, end]]) | 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选 |
| index(sub[, start[, end]]) | 跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常 |
| isalnum() | 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False |
| isalpha() | 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False |
| isdecimal() | 如果字符串只包含十进制数字则返回 True，否则返回 False |
| isdigit() | 如果字符串只包含数字则返回 True，否则返回 False |
| islower() | 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False |
| isnumeric() | 如果字符串中只包含数字字符，则返回 True，否则返回 False |
| isspace() | 如果字符串中只包含空格，则返回 True，否则返回 False |
| istitle() | 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False |
| isupper() | 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False |
| join(sub) | 以字符串作为分隔符，插入到 sub 中所有的字符之间 |
| ljust(width) | 返回一个左对齐的字符串，并使用空格填充至长度为 width 的新字符串 |
| lower() | 转换字符串中所有大写字符为小写 |
| lstrip() | 去掉字符串左边的所有空格 |
| partition(sub) | 找到子字符串 sub，把字符串分成一个 3 元组 (pre_sub, sub, fol_sub)，如果字符串中不包含 sub 则返回 ('原字符串', '', '') |
| replace(old, new[, count]) | 把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次 |
| rfind(sub[, start[, end]]) | 类似于 find() 方法，不过是从右边开始查找 |
| rindex(sub[, start[, end]]) | 类似于 index() 方法，不过是从右边开始 |
| rjust(width) | 返回一个右对齐的字符串，并使用空格填充至长度为 width 的新字符串 |
| rpartition(sub) | 类似于 partition() 方法，不过是从右边开始查找 |
| rstrip() | 删除字符串末尾的空格 |
| split(sep=None, maxsplit=-1) | 不带参数默认是以空格为分隔符切片字符串，如果 maxsplit 参数有设置，则仅分隔 maxsplit 个子字符串，返回切片后的子字符串拼接的列表 |
| splitlines(([keepends])) | 按照 '\n' 分隔，返回一个包含各行作为元素的列表，如果 keepends 参数指定，则返回前 keepends 行 |
| startswith(prefix[, start[, end]]) | 检查字符串是否以 prefix 开头，是则返回 True，否则返回 Falsestart 和 end 参数可以指定范围检查，可选 |
| strip([chars]) | 删除字符串前边和后边所有的空格，chars 参数可以定制删除的字符，可选 |
| swapcase() | 翻转字符串中的大小写 |
| title() | 返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串 |
| translate(table) | 根据 table 的规则（可以由 str.maketrans('a', 'b') 定制）转换字符串中的字符 |
| upper() | 转换字符串中的所有小写字符为大写 |
| zfill(width) | 返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充 |

$f(x)=\left 123 \right$

# 格式化字符串

## 字符串格式化符号含义


|符号|说明|
|:--:|:--|
| %c | 格式化字符及其ASCII码 |
| %s | 格式化字符串 |
| %d | 格式化整数 |
| %o | 格式化无符号八进制数 |
| %x | 格式化无符号十六进制数 |
| %X | 格式化无符号十六进制数（大写） |
| %f | 格式化定点数，可指定小数点后的精度 |
| %e | 用科学计数法格式化定点数 |
| %E | 作用同%e，用科学计数法格式化定点数 |
| %g | 根据值的大小决定使用%f或%e |
| %G | 作用同%g，根据值的大小决定使用%f或者%E |


## 格式化操作符辅助指令

|符号|说明|
|:--:|:--|
| m.n | m是显示的最小总宽度，n是小数点后的位数 |
| - | 用于左对齐 |
| + | 在正数前面显示加号（+） |
| # | 在八进制数前面显示'0o'，在十六进制数前面显示 '0x'或 '0X' |
| 0 | 显示的数字前面填充'0'取代空格 |


## 字符串转义字符含义

|符号|说明|
|:--:|:--:|
| \' | 单引号 |
| \& | 双引号 |
| \a | 发出系统响铃声 |
| \b | 退格符 |
| \n | 换行符 |
| \t | 横向制表符(TAB) |
| \v | 纵向制表符 |
| \r | 回车符 |
| \f | 换页符 |
| \o | 八进制数代表的字符 |
| \x | 十六进制数代表的字符 |
| \0 | 表示一个空字符 |
| \\\ | 反斜杠 |

# 文件

## 文件打开模式

| 打开模式 | 执行操作 |
|:--:|:--|
| 'r' | 以只读方式打开文件（默认） |
| 'w' | 以写入的方式打开文件，会覆盖已存在的文件 |
| 'x' | 如果文件已经存在，使用此模式打开将引发异常 |
| 'a' | 以写入模式打开，如果文件存在，则在末尾追加写入 |
| 'b' | 以二进制模式打开文件 |
| 't' | 以文本模式打开（默认） |
| '+' | 可读写模式（可添加到其他模式中使用） |
| 'U' | 通用换行符支持 |

## 文件对象方法

| 文件对象方法 | 执行操作 |
|:--|:--|
| f.close() | 关闭文件 |
| f.read([size=-1]) | 从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回 |
| f.readline([size=-1]) | 文件中读取并返回一行（包括行结束符），如果有size有定义则返回size个字符 |
| f.write(str) | 将字符串str写入文件 |
| f.writelines(seq) | 向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
| f.seek(offset, from) | 在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节 |
| f.tell() | 返回当前在文件中的位置 |
| f.truncate([size=file.tell()]) | 截取文件到size个字节，默认是截取到文件指针当前位置 |

# os,os.path

## os模块中关于文件/目录常用的函数使用方法

|函数名|使用方法|
|:--|:--|
| getcwd() | 返回当前工作目录 | 
| chdir(path) | 改变工作目录 |
| listdir(path='.') | 列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录） |
| mkdir(path) | 创建单层目录，如该目录已存在抛出异常 |
| makedirs(path) | 递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突 |
| remove(path) | 删除文件 |
| rmdir(path) | 删除单层目录，如该目录非空则抛出异常 |
| removedirs(path) | 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常 |
| rename(old, new) | 将文件old重命名为new |
| system(command) | 运行系统的shell命令 |
| walk(top) | 遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件]) |
| |以下是支持路径操作中常用到的一些定义，支持所有平台 |
| os.curdir | 指代当前目录（'.'） |
| os.pardir | 指代上一级目录（'..'） |
| os.sep | 输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'） |
| os.linesep | 当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）| 
| os.name | 指代当前使用的操作系统（包括：'posix','nt','mac','os2','ce','java'）|

## os.path模块中关于路径常用的函数使用方法

| 函数名 | 使用方法 |
|:--|:--|
| basename(path) | 去掉目录路径，单独返回文件名 |
| dirname(path) | 去掉文件名，单独返回目录路径 |
| join(path1[, path2[, ...]]) | 将path1, path2各部分组合成一个路径名 |
| split(path) | 分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在 |
| splitext(path) | 分离文件名与扩展名，返回(f_name, f_extension)元组 |
| getsize(file) | 返回指定文件的尺寸，单位是字节 |
| getatime(file) | 返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
| getctime(file) | 返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
| getmtime(file) | 返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
| |以下为函数返回 True 或 False |
| exists(path) | 判断指定路径（目录或文件）是否存在 |
| isabs(path) | 判断指定路径是否为绝对路径 |
| isdir(path) | 判断指定路径是否存在且是一个目录 |
| isfile(path) | 判断指定路径是否存在且是一个文件 |
| islink(path) | 判断指定路径是否存在且是一个符号链接 |
| ismount(path) | 判断指定路径是否存在且是一个挂载点 |
| samefile(path1, paht2) | 判断path1和path2两个路径是否指向同一个文件 |


# Python异常

## 标准异常总结

| 异常 | 异常描述 |
|:--|:--|
| AssertionError | 断言语句（assert）失败 |
| AttributeError | 尝试访问未知的对象属性 |
| EOFError | 用户输入文件末尾标志EOF（Ctrl+d） |
| FloatingPointError | 浮点计算错误 |
| GeneratorExit | generator.close()方法被调用的时候
| ImportError | 导入模块失败的时候 |
| IndexError | 索引超出序列的范围 |
| KeyError | 字典中查找一个不存在的关键字 |
| KeyboardInterrupt | 用户输入中断键（Ctrl+c）
| MemoryError | 内存溢出（可通过删除对象释放内存） |
| NameError | 尝试访问一个不存在的变量 |
| NotImplementedError | 尚未实现的方法 |
| OSError | 操作系统产生的异常（例如打开一个不存在的文件） |
| OverflowError | 数值运算超出最大限制 |
| ReferenceError | 弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象 |
| RuntimeError | 一般的运行时错误 |
| StopIteration | 迭代器没有更多的值
| SyntaxError | Python的语法错误 |
| IndentationError  | 缩进错误
| TabError | Tab和空格混合使用 |
| SystemError | Python编译器系统错误 |
| SystemExit | Python编译器进程被关闭
| TypeError | 不同类型间的无效操作 |
| UnboundLocalError | 访问一个未初始化的本地变量（NameError的子类） |
| UnicodeError | Unicode相关的错误（ValueError的子类） |
| UnicodeEncodeError | Unicode编码时的错误（UnicodeError的子类） |
| UnicodeDecodeError | Unicode解码时的错误（UnicodeError的子类） |
| UnicodeTranslateError | Unicode转换时的错误（UnicodeError的子类） |
| ValueError | 传入无效的参数 |
| ZeroDivisionError | 除数为零 |

# 内置异常类的层次结构

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
		+-- StopIteration
		+-- ArithmeticError
		|	 +-- FloatingPointError
		|	 +-- OverflowError
		|	 +-- ZeroDivisionError
		+-- AssertionError
		+-- AttributeError
		+-- BufferError
		+-- EOFError
		+-- ImportError
		+-- LookupError
		|	 +-- IndexError
		|	 +-- KeyError
		+-- MemoryError
		+-- NameError
		|	 +-- UnboundLocalError
		+-- OSError
		|	 +-- BlockingIOError
		|	 +-- ChildProcessError
		|	 +-- ConnectionError
		|	 |	 +-- BrokenPipeError
		|	 |	 +-- ConnectionAbortedError
		|	 |	 +-- ConnectionRefusedError
		|	 |	 +-- ConnectionResetError
		|	 +-- FileExistsError
		|	 +-- FileNotFoundError
		|	 +-- InterruptedError
		|	 +-- IsADirectoryError
		|	 +-- NotADirectoryError
		|	 +-- PermissionError
		|	 +-- ProcessLookupError
		|	 +-- TimeoutError
		+-- ReferenceError
		+-- RuntimeError
		|	 +-- NotImplementedError
		+-- SyntaxError
		|	 +-- IndentationError
		|			+-- TabError
		+-- SystemError
		+-- TypeError
		+-- ValueError
		|	 +-- UnicodeError
		|			+-- UnicodeDecodeError
		|			+-- UnicodeEncodeError
		|			+-- UnicodeTranslateError
		+-- Warning
			+-- DeprecationWarning
			+-- PendingDeprecationWarning
			+-- RuntimeWarning
			+-- SyntaxWarning
			+-- UserWarning
			+-- FutureWarning
			+-- ImportWarning
			+-- UnicodeWarning
			+-- BytesWarning
			+-- ResourceWarning
```

# 魔法方法

| 魔法方法 | 含义 |
|:--|:--|
| | | 基本的魔法方法 |
| `__new__(cls[, ...])` | 1. `__new__` 是在一个对象实例化的时候所调用的第一个方法<br> 2. 它的第一个参数是这个类，其他的参数是用来直接传递给 `__init__` 方法<br> 3. `__new__` 决定是否要使用该 `__init__` 方法，因为 `__new__` 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 `__new__` 没有返回实例对象，则 `__init__` 不会被调用<br> 4. `__new__` 主要是用于继承一个不可变的类型比如一个 tuple 或者 string
| `__init__(self[, ...])` |构造器，当一个实例被创建的时候调用的初始化方法 |
| `__del__(self)` | 析构器，当一个实例被销毁的时候调用的方法 |
| `__call__(self[, args...])` | 允许一个类的实例像函数一样被调用：x(a, b) 调用 `x.__call__(a, b)` |
| `__len__(self)` | 定义当被 len() 调用时的行为 |
| `__repr__(self)` | 定义当被 repr() 调用时的行为 |
| `__str__(self)` | 定义当被 str() 调用时的行为 |
| `__bytes__(self)` | 定义当被 bytes() 调用时的行为 |
| `__hash__(self)` | 定义当被 hash() 调用时的行为 |
| `__bool__(self)` | 定义当被 bool() 调用时的行为，应该返回 True 或 False |
| `__format__(self, format_spec)` | 定义当被 format() 调用时的行为 |
| | **有关属性** |
| `__getattr__(self, name)` | 定义当用户试图获取一个不存在的属性时的行为 |
| `__getattribute__(self, name)` | 定义当该类的属性被访问时的行为 |
| `__setattr__(self, name, value)` | 定义当一个属性被设置时的行为 |
| `__delattr__(self, name)` | 定义当一个属性被删除时的行为 |
| `__dir__(self)` | 定义当 dir() 被调用时的行为 |
| `__get__(self, instance, owner)` | 定义当描述符的值被取得时的行为 |
| `__set__(self, instance, value)` | 定义当描述符的值被改变时的行为 |
| `__delete__(self, instance)` | 定义当描述符的值被删除时的行为 |
| | **比较操作符** |
| `__lt__(self, other)` | 定义小于号的行为：x < y 调用 `x.__lt__(y)`  |
| `__le__(self, other)` | 定义小于等于号的行为：x <= y 调用 `x.__le__(y)`  |
| `__eq__(self, other)` | 定义等于号的行为：x == y 调用 `x.__eq__(y)` |
| `__ne__(self, other)` | 定义不等号的行为：x != y 调用 `x.__ne__(y)` |
| `__gt__(self, other)` | 定义大于号的行为：x > y 调用 `x.__gt__(y)` |
| `__ge__(self, other)` | 定义大于等于号的行为：x >= y 调用 `x.__ge__(y)` |
| | **算数运算符** |
| `__add__(self, other)` | 定义加法的行为：+ |
| `__sub__(self, other)` | 定义减法的行为：- |
| `__mul__(self, other)` | 定义乘法的行为：* |
| `__truediv__(self, other)` | 定义真除法的行为：/ |
| `__floordiv__(self, other)` | 定义整数除法的行为：// |
| `__mod__(self, other)` | 定义取模算法的行为：% |
| `__divmod__(self, other)` | 定义当被 divmod() 调用时的行为 |
| `__pow__(self, other[, modulo])` | 定义当被 power() 调用或 ** 运算时的行为 |
| `__lshift__(self, other)` | 定义按位左移位的行为：<< |
| `__rshift__(self, other)` | 定义按位右移位的行为：>> |
| `__and__(self, other)` | 定义按位与操作的行为：& |
| `__xor__(self, other)` | 定义按位异或操作的行为：^ |
| `__or__(self, other)` | 定义按位或操作的行为：|