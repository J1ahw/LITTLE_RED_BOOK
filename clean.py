import pandas as pd
import datetime

def getYesterday(): 
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

df = pd.read_excel('byPostLink.xlsx',header=0)


category = []
df['result'] = pd.isna(df['picture'])
today = datetime.date.today()
yesterday = getYesterday()
date = []
createrUserId = []
fan = []
address= []
for index, row in df.iterrows():
# 辨别视频/图片
    if row['result']:
        category.append('视频')
    else:
        category.append('图片')
# 转换日期
    if str.startswith(row['date'], '今'):
        date.append(datetime.datetime.strftime(today,"%d.%m.%Y"))
    elif str.startswith(row['date'], '昨'):
        date.append(datetime.datetime.strftime(yesterday,"%d.%m.%Y"))
    else:
        month = str.split(row['date'],'-')[0]
        day = str.split(row['date'],'-')[1]
        date.append(f'{day}.{month}.2023')
# 小红书号
    createrUserId.append(str.split(row['number'],'：')[1])
# 粉丝数
    if '万' in row['fans']:
        row['fans'] = str.replace(row['fans'],'万',' ')
        fan.append(round(float(row['fans']) * 10000))
    else:
        fan.append(row['fans'])
# 地区
    if '英国' in row['location']:
        address.append('UK')
    elif '马来西亚' in row['location']:
        address.append('MALAYSIA')
    elif '韩国' in row['location']:
        address.append('KOREA')
    elif '美国' in row['location']:
        address.append('US')
    elif '澳大利亚' in row['location']:
        address.append('AUSTRILIA')
    elif '新加坡' in row['location']:
        address.append('SINGAPORE')
    elif '日本' in row['location']:
        address.append('JAPAN')
    elif '西班牙' in row['location']:
        address.append('SPAIN')
    elif '加拿大' in row['location']:
        address.append('CANADA')
    elif '德国' in row['location']:
        address.append('GERMANY')
    elif '法国' in row['location']:
        address.append('FRANCE') 
    elif '泰国' in row['location']:
        address.append('THAILAND') 
    #elif '国家中文' in row['location']:
        #address.append('国家英文') 
    #elif '国家中文' in row['location']:
        #address.append('国家英文') 
    #elif '国家中文' in row['location']:
        #address.append('国家英文') 
    else:
        address.append('CHINA')

# 点赞+收藏+评论总数   
df['like'] = df['like'].astype(int)
df['collected'] = df['collected'].astype(int)
df['comment'] = df['comment'].astype(int)
df['COLLECT+LIKE'] = df['like'] + df['collected'] + df['comment']

# 生成 DataFrame
df['笔记格式'] = category
df['POST DATE'] = date
df['CREATER USER ID'] = createrUserId
df['FOLLOWERS'] = fan
df['FOLLOWERS'] = df['FOLLOWERS'].astype(int)
df['CREATER ACCOUNT'] = df['detail-href']
df['CREATER NICKNAME'] = df['detail']
df['ADDRESS'] = address
df['POST LINK'] = df['web-scraper-start-url']
new_df = df[['CREATER NICKNAME','ADDRESS','CREATER USER ID','笔记格式','POST DATE','FOLLOWERS','COLLECT+LIKE','CREATER ACCOUNT','POST LINK']]
# 导出 EXCEL
new_df.to_excel('cleaned_data.xlsx',index=False)




