a=int(input("natural eded daxil edin:"))
n=range(0,100001)
q=[]
r_value=[]
for s in n:
    if s<=a:
        q.append(s)

if len(str(a))==2:
    for s in q:
        value_1=s//10
        value_2=s%10
        r_value.append(value_1)
        r_value.append(value_2)
if len(str(a))==3:
    for s in q:
        if len(str(s))==2:
            value_1=s//10
            value_2=s%10
            r_value.append(value_1)
            r_value.append(value_2)
        if len(str(s))==3:
            value_1=s//100
            value_2=s%100//10
            value_3=s%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
if len(str(a))==4:
    for s in q:
        if len(str(s))==2:
            value_1=s//10
            value_2=s%10
            r_value.append(value_1)
            r_value.append(value_2)
        if len(str(s))==3:
            value_1=s//100
            value_2=s%100//10
            value_3=s%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
        if len(str(s))==4:
            value_1=s//1000
            value_2=s%1000//100
            value_3=s%1000%100//10
            value_4=s%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
if len(str(a))==5:
    for s in q:
        if len(str(s))==2:
            value_1=s//10
            value_2=s%10
            r_value.append(value_1)
            r_value.append(value_2)
        if len(str(s))==3:
            value_1=s//100
            value_2=s%100//10
            value_3=s%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
        if len(str(s))==4:
            value_1=s//1000
            value_2=s%1000//100
            value_3=s%1000%100//10
            value_4=s%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
        if len(str(s))==5:
            value_1=s//10000
            value_2=s%10000//1000
            value_3=s%10000%1000//100
            value_4=s%10000%1000%100//10
            value_5=s%10000%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
            r_value.append(value_5)
if len(str(s))==6:
    for s in q:
        if len(str(s))==2:
            value_1=s//10
            value_2=s%10
            r_value.append(value_1)
            r_value.append(value_2)
        if len(str(s))==3:
            value_1=s//100
            value_2=s%100//10
            value_3=s%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
        if len(str(s))==4:
            value_1=s//1000
            value_2=s%1000//100
            value_3=s%1000%100//10
            value_4=s%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
        if len(str(s))==5:
            value_1=s//10000
            value_2=s%10000//1000
            value_3=s%10000%1000//100
            value_4=s%10000%1000%100//10
            value_5=s%10000%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
            r_value.append(value_5)
        if len(str(s))==6:
            value_1=s//100000
            value_2=s%100000//10000
            value_3=s%100000%10000//1000
            value_4=s%100000%10000%1000//100
            value_5=s%100000%10000%1000%100//10
            value_6=s%100000%10000%1000%100%10
            r_value.append(value_1)
            r_value.append(value_2)
            r_value.append(value_3)
            r_value.append(value_4)
            r_value.append(value_5)
            r_value.append(value_6)
        
print(sum(r_value))   
