# 和歌集の情報が乗っているWebページをダウンロードする

import requests
from bs4 import BeautifulSoup
import time

def zeroume(num):
    return str('000' + str(num) )[-3:] 

def main():
    # https://lapis.nichibun.ac.jp/waka/waka_i{番号}.html に目当ての情報がある
    # 番号のリストを書いて並べておく
    # 金葉和歌集には3バージョンあり、その最新版だけを取得する
    # 5,6,7が金葉
    pre_link = 'https://lapis.nichibun.ac.jp/waka/waka_i'
    link_num = [1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    # リンク(歌集)ごとにダウンロードする
    for i in link_num:
        # https://lapis.nichibun.ac.jp/waka/waka_i001.html みたいになる
        link = pre_link+zeroume(i)+'.html' 

        # HTTP通信でGETする ブラウザにURLを入力してエンターを押すのと同じ
        # JavaScriptは実行されないのでサイトによっては上手く行かない。
        res = requests.get(link) 

        # HTMLを解析するBeautifulSoupというパッケージを使う
        # 今回は文字コードの変換が面倒だからそれを任せるだけ
        soup = BeautifulSoup(res.content, "html.parser")

        #取得できているかの確認のためprintする
        print(soup.h1.text)

        # ファイルとして保存する
        with open('./htmls/'+zeroume(i)+'_' + soup.h1.text+'.html', 'w') as f:
            f.write(str(soup.html))

        # スクレイピングでサイトに負荷をかけるのはあまりよろしくないので適当にsleepを入れる
        time.sleep(2)

if __name__ == '__main__':
    main()
