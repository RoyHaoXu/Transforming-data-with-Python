import read
from dateutil.parser import parse
df = read.load_data()
def hour(s):
    a = parse(s).hour
    return a 
df.iloc[:,0] = df.iloc[:,0].apply(hour)
print(df.iloc[:,0].value_counts())