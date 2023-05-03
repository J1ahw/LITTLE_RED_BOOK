import pandas as pd
df = pd.read_excel('raw.xlsx',header=0)

df[['1','2','3','4','5','6']] = df['raw'].str.split(' ', n=6, expand=True)
#crowdfunding_info_df[['category','sub-category']] = crowdfunding_info_df['category & sub-category'].str.split('/', n=2, expand=True)
df[['2.1','2.2']] = df['2'].str.split('发布了一篇', n=2, expand=True)
df[['6.1','6.2','6.3']] = df['6'].str.split('，', n=3, expand=True)
df['name'] = df['2.1']
df['Post Link'] = df['6.1']
df = df [['name','Post Link']]

df.to_excel('new.xlsx',index=False)