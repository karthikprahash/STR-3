# STR-3
i=input()
t='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
p=''
for s in i:
    t1=t.index(s)
    t2=t1+3
    p=p+t[t2]
print(p)
    
