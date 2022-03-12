# 歌集ごとに距離ベクトルを計算して図にする

from titles import titles
import json
import math
import numpy
import matplotlib.pyplot as plt
import seaborn

# vector.pyで保存したjsonを開く
def getVector(kashu):
    v = {}
    with open('./jsons/'+kashu+'.json','r') as f:
        v = json.load(f)
    return v['vector']

def similarity(kashu1, kashu2):
    r2 = 0
    v1 = getVector(kashu1)
    v2 = getVector(kashu2)
    ks1 = v1.keys()
    ks2 = v2.keys()

    for k1 in ks1:
        if k1 in ks2: # kashu1にもkashu2にも存在する次元
            r2 += (v1[k1] - v2[k1]) ** 2
        else: # kashu1にしか存在しない次元
            r2 += v1[k1] ** 2
    
    for k2 in ks2:
        if k2 in ks1:
            pass
        else: # kashu2にしか存在しない次元
            r2 += v2[k2] ** 2
    
    # 歌集間の距離を返す
    return math.sqrt(r2)
    
def draw_heatmap(data):
    # matplotlibっていう有名なライブラリを
    # 手軽に扱うためのライブラリ
    ax = seaborn.heatmap(data)
    ax.invert_yaxis()
    plt.savefig('out.png')

def main():
    # 21個の歌集同士の類似度を求めるので21*21の配列を用意しておく
    matrix = numpy.zeros((21,21))
    
    for i, title1 in enumerate(titles):
        for j, title2 in enumerate(titles):
            r = similarity(title1,title2)
            matrix[i][j] = r
    
    draw_heatmap(matrix)

if __name__ == '__main__':
    main()
