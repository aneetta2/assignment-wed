dict={'a':1,'b':2,'c':3,'d':4,'e':5}
rem_list=['b','c','d']
print("the orginal dictionary is:"+str(dict))
[dict.pop(key)for key in rem_list]
print("dictionary after removal of keys:"+str(dict))