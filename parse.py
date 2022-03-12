from bs4 import BeautifulSoup
from titles import titles

def parser1(soup):
    tables = soup.find_all('table',attrs={'width':'650'})
    wakas = []
    for table in tables:
        waka = (table.find_all('td')[1].find_all('div')[-2].text.split('\n')[1])
        wakas.append(waka)
    return wakas

def parser2(soup):
    tables = soup.find_all('table',attrs={'width':'650'})
    wakas = []
    for table in tables:
        waka = (table.find_all('td')[1].find_all('div')[2].text.split('\n')[0])
        wakas.append(waka)
    return wakas

def main():
    for title in titles:
        print(title)
        file_name = './htmls/'+title+'.html'
        wakas = []
        with open(file_name, 'r') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            if title in ['001_古今集','002_後撰集','003_拾遺集','009_千載集']:
                wakas = parser1(soup)
            else:
                wakas = parser2(soup)
        with open('./csvs/'+title + '.csv', 'w') as f:
            f.write('\n'.join(wakas))

if __name__ == '__main__':
    main()