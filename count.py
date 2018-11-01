import read
df = read.load_data()
a = str(df.iloc[0,3])
for e in range(1,9999):
    a=a+" "
    a = a+str(df.iloc[e,3])
a = a.replace('(','')
a = a.replace(')','')
a = a.replace('?','')
a = a.replace('[','')
a = a.replace(']','')
a = a.lower()
aa = a.split(' ')
import collections
count = collections.Counter(aa)
sort = sorted(count.items(),key=lambda item:item[1])
l = len(sort)
print(sort[(l-1-100):(l-1)])