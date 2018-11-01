import pandas as pd
def load_data():
    df = pd.read_csv('hn_stories.csv',header=None)
    df.columns = ['submission_time','upvotes','url','headline']
    return df
df = pd.read_csv('hn_stories.csv')
if __name__ == "__main__":
    df = load_data()
    print(df)

    
