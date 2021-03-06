#文件操作|内容分隔再存储
'''
读取文件->按照‘:’分隔每行元素->将使用'======'分隔的内容存储到不同的文件中

文件内容定义：
每行使用':'分隔不同内容
不同的内容块使用'======'分隔
'''

'''
record.txt'内容样例如下

Li:How are you?
Wang:I am fine, think you!
======
Li:What happend?
Wang:Nothing
'''

def save_file(boy,girl,count):
	file_name_boy='boy_'+str(count)+'.txt'
	file_name_girl='girl_'+str(count)+'.txt'

	boy_file=open(file_name_boy,'w')
	girl_file=open(file_name_girl,'w')

	boy_file.writelines(boy)
	girl_file.writelines(girl)

def split_file(file_name):
	f=open('record.txt')
	boy=[]
	girl=[]
	count=1
	for each_line in f:
		if each_line[:6]!='======':
			(role,line_spoken)=each_line.split(':',1)
			if role=='Li':
				boy.append(line_spoken)
			if role=='Wang':
				girl.append(line_spoken)
		else:
			save_file(boy,girl,count)

			boy=[]
			girl=[]
			count+=1

	save_file(boy,girl,count)
	f.close()

split_file('record.txt')
