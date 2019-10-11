#%%

import pandas as pd

def split_user(df):
    str_temp = df["user_time"]
    if("2019" in str_temp):
        temp_list = str_temp.split("2019")
        return temp_list[0].strip()
    else:
        return None

def split_time(df):
    str_temp = df["user_time"]
    if("2019" in str_temp):
        temp_list = str_temp.split("2019")
        return str(2019)+temp_list[1].strip()
    else:
        return None

def calculate_rate(df):
    str_temp = df["rating"]
    try:
        num_list = re.findall("\d",str_temp)
        if(num_list):
            sum_num=0
            for num in num_list:
                sum_num += int(num)
            return sum_num/len(num_list)
        else:
            return None
    except:
        return None

dt = pd.read_csv("raw_data.csv")
dt = dt[dt["comments"].notnull()]
dt.to_excel("intem.xlsx")
dt["user"] = dt.apply(split_user, axis=1)
dt["time"] = dt.apply(split_time, axis=1)
dt["rating"] = dt.apply(calculate_rate, axis=1)
dt['rating'] = dt['rating'].astype(float)
dt['rating'] = dt['rating'].fillna(dt['rating'] .mean())
dt = dt[dt["time"].notnull()]
dt = dt[['city','place','rating','comments','url','user','time']]
dt.to_csv("cleaned_data.csv",index=False)


#%% city,place,rating,comments,url,user,time
import pandas as pd

df_ctrip=pd.read_csv("cleaned_data.csv")
df_weibo=pd.read_excel("TeamWork/771737.xlsx")

df_weibo["city"]=""
df_weibo["place"]=""
df_weibo["rating"]=""
df_weibo=df_weibo[['微博ID(mblogId)',
                   '微博url(url)',
                   '爬取时间(__time)',
                   '微博内容(post_content)']]
df_weibo=df_weibo.rename(columns={'微博ID(mblogId)':'user','微博url(url)':'url',
                         '爬取时间(__time)':'time','微博内容(post_content)':'comments'})

df_weibo = df_weibo[['city','place','rating','comments','url','user','time']]