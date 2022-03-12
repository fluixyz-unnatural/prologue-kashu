# 説明

円城塔『プロローグ』に登場する和歌の分析をやってみたもの

## download.py

`https://lapis.nichibun.ac.jp`から和歌をダウンロードして html としてそのまま保存する。
文字コードの違いを BeautifulSoup に丸投げしてる。

## parse.py

html からひらがなの和歌を抜き出して csv として保存する。

## vector.py

csv を tri-gram でベクトル化し、それらの和から歌集ベクトルを作る。

## analyse.py

歌集ベクトル間の距離を求め、図にする。
