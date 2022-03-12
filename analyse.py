from titles import titles
import json
import math
import numpy
import matplotlib.pyplot as plt
import seaborn

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
        if k1 in ks2:
            r2 += (v1[k1] - v2[k1]) ** 2
        else:
            r2 += v1[k1] ** 2
    
    for k2 in ks2:
        if k2 in ks1:
            pass
        else:
            r2 += v2[k2] ** 2
    
    return math.sqrt(r2)
    
def draw_heatmap(data):
    ax = seaborn.heatmap(data)
    ax.invert_yaxis()
    plt.savefig('out.png')

def main():
    matrix = numpy.zeros((21,21))
    for i, title1 in enumerate(titles):
        for j, title2 in enumerate(titles):
            r = similarity(title1,title2)
            matrix[i][j] = r
    draw_heatmap(matrix)

if __name__ == '__main__':
    main()
