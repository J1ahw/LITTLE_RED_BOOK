import pandas as pd
import datetime

def getYesterday(): 
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

df = pd.read_excel('byPostLink.xlsx',header=0)


category1 = []
category2 = []
df['result'] = pd.isna(df['picture'])
today = datetime.date.today()
yesterday = getYesterday()
date = []
createrUserId = []
fan = []
address = []
profile = []
country = []
location_dic = {'英国': 'UK',
                '马来西亚': 'MALAYSIA',
                '韩国': 'KOREA',
                '美国': 'US',
                '澳大利亚': 'AUSTRILIA',
                '新加坡': 'SINGAPORE',
                '日本': 'JAPAN',
                '西班牙': 'SPAIN',
                '加拿大': 'CANADA',
                '德国': 'GERMANY',
                '法国': 'FRANCE',
                '泰国': 'THAILAND',
                #'国家中文' :'国家英文',
                #'国家中文' :'国家英文',
                #'国家中文' :'国家英文',
                }

for index, row in df.iterrows():
# 辨别视频/图片
    if row['result']:
        category1.append('视频')
        category2.append('VIDEO')
    else:
        category1.append('图片')
        category2.append('PHOTO')
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
    if '万' in str(row['fans']):
        row['fans'] = str.replace(row['fans'],'万',' ')
        fan.append(round(float(row['fans']) * 10000))
    else:
        fan.append(row['fans'])
# 地区
    country = str.split(row['location'],'：')[1]
    address.append(location_dic[country])
# 性别
    row['gender'] = str.strip(row['gender'], '#').upper()
# 生成 CREATER PROFILE
    createrProfile = f'CHINESE, {row["gender"]}, {location_dic[country]} BASED STUDENT/RESIDENT'
    profile.append(createrProfile)
# 点赞+收藏+评论总数   
df['like'] = df['like'].astype(int)
df['collected'] = df['collected'].astype(int)
df['comment'] = df['comment'].astype(int)
df['COLLECT+LIKE'] = df['like'] + df['collected'] + df['comment']

# 生成 DataFrame
df['笔记格式'] = category1
df['POST FORMAT'] = category2
df['POST DATE'] = date
df['CREATER PROFILE'] = profile
df['CREATER USER ID'] = createrUserId
df['FOLLOWERS'] = fan
df['FOLLOWERS'] = df['FOLLOWERS'].astype(int)
df['CREATER ACCOUNT'] = df['detail-href']
df['CREATER NICKNAME'] = df['detail']
df['ADDRESS'] = address
df['POST LINK'] = df['web-scraper-start-url']
new_df = df[['CREATER NICKNAME','ADDRESS','CREATER PROFILE', 'CREATER USER ID','笔记格式','POST FORMAT','POST DATE','FOLLOWERS','COLLECT+LIKE','CREATER ACCOUNT','POST LINK']]

# 导出 EXCEL
new_df.to_excel('final_data.xlsx',index=False)




