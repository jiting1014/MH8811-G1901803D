def my_min(list):
    my_min=None
    for num in list:
        if my_min is None:
            my_min=num
            continue
        if my_min>num:
            my_min=num
    return my_min
def my_max(list):
    my_max=None
    for num in list:
        if my_max is None:
            my_max=num
            continue
        if my_max<num:
            my_max=num
    return my_max
def my_ave(list):
    count=0
    s=0
    for num in list:
        count=count+1
        s=s+num
    my_ave=s/count
    return my_ave
def my_mediam(list):
    list.sort()
    if len(list)/2==int(len(list)/2):
        my_mediam=(list[int(len(list)/2)]+list[int(len(list)/2-1)])/2
    else:
        my_mediam=list[int(len(list)/2)]
    return my_mediam
def my_range(list):
    my_range=my_max(list)-my_min(list)
    return my_range
def my_var(list):
    sum_my_var=0
    for num in list:
        var_num=(num-my_ave(list))**2
        sum_my_var=sum_my_var+var_num
    my_var=sum_my_var/len(list)
    return my_var

fhandle=open ('MH8811-04-Data.csv')
lines = []
for line in fhandle:
    line=line.rstrip()
    if line:
        lines.append(line)
my_list=list(map(int,lines))

short_list=[9,41,12,3,74,15]
print('The output for Classwork:')
print(short_list)

print('The minimum is',my_min(short_list))
print('The maximum is',my_max(short_list))
print('The average is',my_ave(short_list))
print('The medium is',my_mediam(short_list))
print('The range is',my_range(short_list))
print('The sample variance is',my_var(short_list))

print('The output for Homework:')
print(my_list)

print('The minimum is',my_min(my_list))
print('The maximum is',my_max(my_list))
print('The average is',my_ave(my_list))
print('The medium is',my_mediam(my_list))
print('The range is',my_range(my_list))
print('The sample variance is',my_var(my_list))