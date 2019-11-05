# -*- encode: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
# import numpy as numpy
import json
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import time
from db_operation import createDB


app = Flask(__name__)


# フロントからoandaのapiキーやアカウントIDを取得
# DBの作成とFXデータの取得を行なう
# News記事はRSSリーダーを使用して格納
@app.route('/')
def initFunc():
    # キーが登録されているかどうかをチェック
    
    
    # なければキーをDBに格納させる
    # SHAの暗号化
    pass

@app.route('/streaming')
def fxStreaming():
    # oandapyからストリーミングデータを取得
    # フロントにチャートデータを送信，DBへ記録
    pass


@app.route('/news')
def getNewsRSS():
    # RSSの取得(10分ごと)
    
    pass

if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
    createDB()
    print("server is running")
    # host = 'localhost'
    # port = 33553
    # host_port = (host, port)

    # server = pywsgi.WSGIServer(
    #     host_port,
    #     app,
    #     handler_class=WebSocketHandler
    # )

    # server.serve_forever()
    # console.log("server is running")