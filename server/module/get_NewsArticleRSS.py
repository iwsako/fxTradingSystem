import feedparser
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import requests
from datetime import datetime


# URL先からタイトルと本文，発行日を取ってくる
def getNewsArticleFromRSS():
    # 将来的にはこのRSSもユーザが登録できるようにする
    RSS_URLs = ["https://news.yahoo.co.jp/pickup/economy/rss.xml"]
    conn = sqlite3.connect('NewsArticles.db')
    cur = conn.cursor()
    db_column=["title", 'pub', 'body', 'link']
    sql_df = pd.read_sql('select * from news order by pub limit 10;', conn)
    addsql_df = pd.DataFrame(columns=db_column)

    d = feedparser.parse(RSS_URLs[0])
    # print(RSS_URLs)
    for entry in d.entries:
        # DBにあるデータから追加するタイトルが存在するかチェックしDFに追加
        if(entry.title not in sql_df["title"].values):
            body = getBodyDataFromBS(entry.link)
            pub = parseRssDate(entry.published)
            addsql_df = addsql_df.append(pd.Series([entry.title, pub, body, entry.link], index=db_column), ignore_index=True)
        
    # print(addsql_df)
    addsql_df.to_sql('news', conn, if_exists='append', index=False)

    cur.close()
    conn.close()


# rssのurl先から本文のサマリーを取得する
def getBodyDataFromBS(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    # サマリーだけ取得する
    body = soup.find('p', {"class": "tpcNews_summary"}).get_text()
    return body


# rssの日付をパース
def parseRssDate(rssPubDate):
    pubdate_parse = datetime.strptime(rssPubDate, '%a, %d %b %Y %H:%M:%S %z')
    pubdate = pubdate_parse.strftime('%Y/%m/%d %H:%M:%S')
    return pubdate


# DBに保管されてるデータのチェック用
def checkNewsDB():
    conn = sqlite3.connect('NewsArticles.db')
    cur = conn.cursor()
    df = pd.read_sql('select * from news', conn)
    print(df["body"])
    print(df["pub"])
    print(df["link"])
    cur.close()
    conn.close()


# for test
# getNewsArticleFromRSS()
if __name__ == '__main__':
    getNewsArticleFromRSS()
    checkNewsDB()
