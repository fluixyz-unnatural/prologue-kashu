# 説明

円城塔『プロローグ』に登場する和歌の分析をやってみたもの

## ファイル

### download.py

`https://lapis.nichibun.ac.jp`から和歌をダウンロードして html としてそのまま保存する。
文字コードの違いを BeautifulSoup に丸投げしてる。

### parse.py

html からひらがなの和歌を抜き出して csv として保存する。

### vector.py

csv を tri-gram でベクトル化し、それらの和から歌集ベクトルを作る。

### analyse.py

歌集ベクトル間の距離を求め、図にする。

## 使用パッケージ

### requests
HTTP通信をするためのライブラリ
Python標準のurllib2を使いやすくしたもの

### bs4
BeautifulSoup4の略
HTMLファイルから情報を抜き出すのに使う
スクレイピングといえばBeautifulSoup

### numpy
行列を扱うライブラリ
機械学習に必要不可欠
このプロジェクトではnumpyじゃなくても良いような使い方しかされていない

### matplotlib
作図のためのライブラリ
日本語を表示しようとするとフォントの設定がやや面倒

### seaborn
matplotlibをかんたんに使えるようにしたもの
