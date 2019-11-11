import feedparser
# import BeautifulSoup
import pandas as pd
import sqlite3


# URL先からタイトルと本文，発行日を取ってくる
def getNewsArticleFromRSS():
    RSS_URLs = ["https://news.yahoo.co.jp/pickup/economy/rss.xml", "https://www.nhk.or.jp/rss/news/cat5.xml"]
    conn = sqlite3.connect('NewsArticles.db')
    cur = conn.cursor()
    db_column=["title", 'pub', 'body']
    sql_df = pd.read_sql('select * from news order by pub limit 10;', conn)
    addsql_df = pd.DataFrame(columns=db_column)

    d = feedparser.parse(RSS_URLs[0])
    # print(RSS_URLs)
    for entry in d.entries:
        # print(entry)
        # print(entry.title)
        # print("-----")
        # print(entry.link)
        # print("-----")
        # print(entry.published)
        # print("-----")
        # DBにあるデータから追加するタイトルが存在するかチェックしDFに追加
        
        if(entry.title not in sql_df["title"].values):
            addsql_df = addsql_df.append(pd.Series([entry.title, entry.published, "test"], index=db_column), ignore_index=True)
        
    # print(addsql_df)
    addsql_df.to_sql('news', conn, if_exists='append', index=False)

    cur.close()
    conn.close()

def checkNewsDB():
    conn = sqlite3.connect('NewsArticles.db')
    cur = conn.cursor()

    df = pd.read_sql('select * from news', conn)
    print(df)

    cur.close()
    conn.close()

# for test
# getNewsArticleFromRSS()
if __name__ == '__main__':
    getNewsArticleFromRSS()
    checkNewsDB()
