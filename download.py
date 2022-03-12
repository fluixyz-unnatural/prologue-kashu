import requests
from bs4 import BeautifulSoup
import time

link_num = [1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# 5,6,7が金葉
def zeroume(num):
    return str('000' + str(num) )[-3:] 

def main():

    pre_link = 'https://lapis.nichibun.ac.jp/waka/waka_i'
    for i in link_num:
        link = pre_link+zeroume(i)+'.html'
        res = requests.get(link)
        soup = BeautifulSoup(res.content, "html.parser")
        print(soup.h1.text)
        with open('./htmls/'+zeroume(i)+'_' + soup.h1.text+'.html', 'w') as f:
            f.write(str(soup.html))
        time.sleep(2)

if __name__ == '__main__':
    main()
