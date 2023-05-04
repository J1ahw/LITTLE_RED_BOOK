import pandas as pd
df = pd.read_excel('xhs_in.xlsx',header=0)

df[['1','2','3','4','5','6']] = df['raw'].str.split(' ', n=6, expand=True)
df[['6.1','6.2','6.3']] = df['6'].str.split('，', n=3, expand=True)
df['start_url'] = df['6.1']
df = df ['start_url']

df.to_excel('xhs_out.xlsx',index=False)