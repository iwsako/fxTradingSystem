import sqlite3


# 為替とニュース記事を格納するDBを作成
def createDB():
    dbnames = ['FX.db', 'NewsArticles.db']
    for d in dbnames:
        # dbに接続
        conn = sqlite3.connect(d)
        # sqliteのカーソルオブジェクト作成
        cur = conn.cursor()

        # それぞれのDBでテーブル作成
        if 'FX' in d:
            createTABLEforFX(d, cur)
        else:
            createTABLEforNA(d, cur)

        # DBへ設定の反映
        conn.commit()
        cur.close()
        conn.close()



def createTABLEforFX(dbname, cur):
    pair_list = ["USDJPY", "GBPJPY"]
    for pair in pair_list:
        cur.execute(
            'CREATE TABLE IF NOT EXISTS {} (date INTEGER, high FLOAT, low FLOAT, open FLOAT, close FLOAT)'.format(pair)
        )

    # 暗号化したapiキーなどを保存するテーブル
    cur.execute(
        'CREATE TABLE IF NOT EXISTS key (accountid STRING, apikey STRING)'
    )
        

def createTABLEforNA(dbname, cur):
    cur.execute(
        'CREATE TABLE IF NOT EXISTS news(title STRING, pub STRING, body STRING)'
    )
    # cur.execute('INSERT INTO news(title, date, body) values("aaa", "bbb", "ccc")')

## test
if __name__ == '__main__':
    createDB()
