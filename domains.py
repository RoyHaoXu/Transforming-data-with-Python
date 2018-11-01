import read
df = read.load_data()
count = {}
for e in range(9999):
    if df.iloc[e,2] in count:
        count[df.iloc[e,2]]+=1
    else:
        count[df.iloc[e,2]]=1
sort = sorted(count.items(),key=lambda item:item[1])
print(sort)