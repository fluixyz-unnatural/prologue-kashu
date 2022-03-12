# 和歌集のタイトルをPythonのリストでまとめる
titles= []
with open('titles.csv','r') as f:
        lines = f.readlines()
        for l in lines:
            titles.append(l[:-1])