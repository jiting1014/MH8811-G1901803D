import json
filename=input("Please input the name of file you want to open:")
fh=open(filename)
data=json.load(fh)
fh.close()
print('The type of the data structure is:',type(data))

def save(sav):
    filename_0=input('Please input the name of file you want to save (eg. name.json):')
    with open(filename_0,'w') as file_save:
        json.dump(sav,file_save)
        file_save.close()
def serialize_lst(l):
    res=''
    for i in l:
        res=res+str(i)+str(type(i))
        res=res+'|'
    return res[:-1]
def deserialize_lst(d):
    filename_lst=input('Please input the name of file you want to open (eg. name.json):')
    fh_lst=open(filename_lst)
    data_lst=json.load(fh_lst)
    fh_lst.close()
    str_lst=data_lst.split('|')
    for i in range(int(len(d))):
        if "<class 'int'>" in str_lst[i]:
            str_lst[i]=int(str_lst[i].rstrip("<class 'int'>"))
        elif "<class 'float'>" in str_lst[i]:
            str_lst[i]=float(str_lst[i].rstrip("<class 'float'>"))
        else:
            str_lst[i]=str_lst[i].rstrip("<class 'str'>")
    return str_lst
def serialize_dict(di):
    str_dict=dict([(x,str(y)) for x,y in di.items()])
    lst_1=list(str_dict.keys())
    lst_2=list(str_dict.values())
    res=''
    for i in range(int(len(lst_1))):
        res=res+lst_1[i]+'='+lst_2[i]+str(type(list(di.values())[i]))
        res=res+'|'
    return res[:-1]
def deserialize_dict():
    filename_dict=input('Please input the name of file you want to open (eg. name.json):')
    fh_dict=open(filename_dict)
    data_dict=json.load(fh_dict)
    fh_dict.close()
    split_dict=data_dict.split('|')
    lst=[]
    for i in split_dict:
        lst.append(i.split('='))
    dict_0=dict(lst)
    lst_3=list(dict_0.values())
    for i in range(int(len(lst_3))):
        if "<class 'int'>" in lst_3[i]:
            lst_3[i]=int(lst_3[i].rstrip("<class 'int'>"))
        elif "<class 'float'>" in lst_3[i]:
            lst_3[i]=float(lst_3[i].rstrip("<class 'float'>"))
        else:
            lst_3[i]=lst_3[i].rstrip("<class 'str'>")
    lst_4=list(dict_0.keys())
    final_dict=dict(zip(list(dict_0.keys()),lst_3))
    return final_dict
def serialize_null(s_null):
    res=json.dumps(s_null)
    return res
def deserialize_null():
    filename_null=input('Please input the name of file you want to open (eg. name.json):')
    fh_null=open(filename_null)
    data_null=json.load(fh_null)
    fh_null.close()
    res=json.loads(data_null)
    return res

if type(data)==type({}):
    if data:
        serialized=serialize_dict(data)
        save(serialized)
        deserialized=deserialize_dict()
        if deserialized==data:
            print('Success!')
        else:
            print('Failure!')
    else:
        serialized=serialize_null(data)
        save(serialized)
        deserialized=deserialize_null()
        if deserialized==data:
            print('Success!')
        else:
            print('Failure!')

if type(data)==type([]):
    if data:
        serialized=serialize_lst(data)
        save(serialized)
        deserialized=deserialize_lst(data)
    else:
        serialized=serialize_null(data)
        save(serialized)
        deserialized=deserialize_null()
    if deserialized==data:
        print('Success!')
    else:
        print('Failure!')



