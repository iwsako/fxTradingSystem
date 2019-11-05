import feedparser
import BeautifulSoup

# URL先からタイトルと本文，発行日を取ってくる
def getNewsArticleFromRSS():
    RSS_URLs = ["https://news.yahoo.co.jp/pickup/rss.xml"]

    d = feedparser.parse(RSS_URLs[0])

    for entry in d.entries:
        print(entry)
        print(entry.title, entry.link, entry.published)
        print("-----")


# for test
# if __name__ == "__main()__":
#     getNewsArticleFromRSS()