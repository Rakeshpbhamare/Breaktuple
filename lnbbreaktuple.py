tup=()
n=int(input('element no'))
for x in range(n):
    tup+=(int(input('enter element')),)
print(tup)
lst=list(tup)
print(lst)
lst_1=[]
lst_2=[]
lst_1.extend(lst[0:5:2])
lst_2.extend(lst[1::2])
#print(lst_1)
#print(lst_2)
tup_1=tuple(lst_1)
tup_2=tuple(lst_2)
print(tup_1)
print(tup_2)

