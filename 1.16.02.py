# pickle

import pickle

my_list1=[123,3.14,'Li',['another list']]

pickle_file=open('my_list.pkl','wb')
pickle.dump(my_list1,pickle_file)
pickle_file.close()

pickle_file=open('my_list.pkl','rb')
my_list2=pickle.load(pickle_file)
print(my_list2)
pickle_file.close()
