import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from hkh.src.HKH_DIAPER_YK import * # 기저귀 브랜드 분류하는 패키지

import pymongo
import sys
from datetime import datetime, timedelta

def get_item():

    client = pymongo.MongoClient("mongodb://133.186.168.8:50000")
    db = client.DB_TEST
    
    item_d = pd.DataFrame(list(db.colt_item_option.find()))

    item_option_columns = ['brand_name','doc_id','goods_name']
    df = item_d[item_option_columns]
    
    return df

def seperate_in_else_data(df):
    in_data = df[~((df['brand_name'].str.contains('상세')) | (df['brand_name'] == '') | (df['brand_name'].str.contains('없음')| df['brand_name'].str.contains('별도')))]
    else_data =  df[(df['brand_name'].str.contains('상세')) | (df['brand_name'] == '') | (df['brand_name'].str.contains('없음') | df['brand_name'].str.contains('별도'))]
    return in_data, else_data

def large_brand_name(in_data, else_data):
    in_data['large_brand_name'] = in_data['brand_name'].apply(seperate_diaper_brand)
    else_data['large_brand_name'] = else_data['goods_name'].apply(seperate_diaper_brand)
    return in_data, else_data

def merge_data(in_data,else_data):
    diaper = pd.concat([in_data.dropna(subset = ['large_brand_name']), else_data.dropna(subset = ['large_brand_name'])])
    return diaper

def classify_brand(diaper):
    df_haggies = diaper[diaper['large_brand_name'] == '하기스']
    df_goon = diaper[diaper['large_brand_name'] == '군']
    df_merries = diaper[diaper['large_brand_name'] == '메리즈']
    df_pampers = diaper[diaper['large_brand_name'] == '펨퍼스']
    df_mammypoko = diaper[diaper['large_brand_name'] == '마미포코']
    df_bosomi = diaper[diaper['large_brand_name'] == '보솜이']
    df_naturel = diaper[diaper['large_brand_name'] == '네이처러브메레']
    df_superdady = diaper[diaper['large_brand_name'] == '슈퍼대디']
    df_penelope = diaper[diaper['large_brand_name'] == '페넬로페']
    df_kindoh = diaper[diaper['large_brand_name'] == '킨도']
    df_nabijam = diaper[diaper['large_brand_name'] == '나비잠']
    return df_haggies,df_goon,df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady,df_penelope,df_kindoh,df_nabijam

def medium_brand_name(df_haggies,df_goon,df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady,df_penelope,df_kindoh,df_nabijam):
    df_haggies['medium_brand_name'] = df_haggies['goods_name'].apply(haggies_j)
    # 메리즈는 medium_brand_name 건너 뜀 (분류가 없음)
    df_goon['medium_brand_name'] = df_goon['goods_name'].apply(goon_j)
    df_pampers['medium_brand_name'] = df_pampers['goods_name'].apply(pampers_j)
    df_mammypoko['medium_brand_name'] = df_mammypoko['goods_name'].apply(mammypoko_j)
    df_bosomi['medium_brand_name'] = df_bosomi['goods_name'].apply(bosomi_j)
    df_naturel['medium_brand_name'] = df_naturel['goods_name'].apply(naturel_j)
    df_superdady['medium_brand_name'] = df_superdady['goods_name'].apply(superdady_j)
    df_penelope['medium_brand_name'] = df_penelope['goods_name'].apply(penelope_j)
    df_kindoh['medium_brand_name'] = df_kindoh['goods_name'].apply(kindoh_j)
    df_nabijam['medium_brand_name'] = df_nabijam['goods_name'].apply(nabijam_j)
    return df_haggies,df_goon,df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady,df_penelope,df_kindoh,df_nabijam

def merge_brand(df_haggies,df_goon,df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady,df_penelope,df_kindoh,df_nabijam):
    df_diaper = pd.concat([df_haggies,df_goon,df_merries, df_pampers, df_mammypoko,df_bosomi, df_naturel,df_superdady,df_penelope,df_kindoh,df_nabijam])
    return df_diaper

def insert_item_option(df_diaper):
    client = pymongo.MongoClient('mongodb://133.186.168.8:50000', maxPoolSize = None)
    db_test = client.DB_TEST
    db = db_test.colt_item_option
    df_diaper = df_diaper.rename(columns=lambda x: x.lower()) # 소문자로 변경
    for diaper_doc_id, diaper_large_brand_name, diaper_medium_brand_name in df_diaper[['doc_id','large_brand_name','medium_brand_name']].values[:]:
        db_test.colt_item_option.update_many({'doc_id': diaper_doc_id},{'$set':{'large_brand_name':diaper_large_brand_name,'medium_brand_name':diaper_medium_brand_name}})

def main():
    item = get_item()
    print ('데이터 불러오기 완료')
    print ('----------------------')
    in_data, else_data = seperate_in_else_data(item)
    print ('in_data, else_data 분리완료')
    print ('----------------------')
    in_data, else_data = large_brand_name(in_data, else_data)
    print ('large_brand_name 분류 완료')
    print ('----------------------')
    diaper = merge_data(in_data,else_data)

    df_haggies, df_goon, df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady, df_penelope, df_kindoh, df_nabijam = classify_brand(diaper)
    print ('기저기 브랜드 분류 완료')
    print ('----------------------')
    df_haggies, df_goon, df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady, df_penelope, df_kindoh, df_nabijam = \
    medium_brand_name(df_haggies, df_goon, df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady, df_penelope, df_kindoh, df_nabijam)
    print ('medium_brand_name 분류 완료')
    print ('----------------------')
    df_diaper = merge_brand(df_haggies, df_goon, df_merries, df_pampers, df_mammypoko, df_bosomi, df_naturel,df_superdady, df_penelope, df_kindoh, df_nabijam)
    print ('정제 완료')
    print ('----------------------')
    insert_item_option(df_diaper)
    print ('데이터 삽입 완료')
    print ('----------END-----------')
def classify_diaper_brand_name():
    s = datetime.now()
    main()
    print (datetime.now() - s)