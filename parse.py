# 和歌集が載っているWebページから和歌の読みの情報だけを抜き取る

from bs4 import BeautifulSoup
from titles import titles

def parser1(soup):
    # <table width="650"> みたいなタグを抜き出す
    tables = soup.find_all('table',attrs={'width':'650'})

    wakas = []
    for table in tables:
        # <table>内の0から数えて1番目の<td>の中にある後ろから2番目の<div>内のテキストの0から数えて1行目を抜き出す
        waka = (table.find_all('td')[1].find_all('div')[-2].text.split('\n')[1])
        # wakasリストに加える
        wakas.append(waka)
    return wakas

def parser2(soup):
    # <table width="650"> みたいなタグを抜き出す
    tables = soup.find_all('table',attrs={'width':'650'})
    wakas = []
    for table in tables:
        # <table>内の0から数えて1番目の<td>の中にある前から3番目の<div>内のテキストの最初の行を抜き出す
        waka = (table.find_all('td')[1].find_all('div')[2].text.split('\n')[0])
        wakas.append(waka)
    return wakas

def main():
    for title in titles:
        print(title) # 進み具合を確認するためにタイトルをプリントする
        file_name = './htmls/'+title+'.html' # ./htmls/古今集.html みたいに保存する

        wakas = [] 
        # download.pyで手に入れたhtmlファイルを開く

        with open(file_name, 'r') as f:

            # このままではただのテキストなのでBeautifulSoupで扱いやすくする
            soup = BeautifulSoup(f.read(), 'html.parser')

            # ページによって構造が少し違うのでパーサーを2種類作った
            if title in ['001_古今集','002_後撰集','003_拾遺集','009_千載集']:
                wakas = parser1(soup)
            else:
                wakas = parser2(soup)
        
        # 和歌をCSVに保存する
        with open('./csvs/'+title + '.csv', 'w') as f:
            f.write('\n'.join(wakas))

if __name__ == '__main__':
    main()