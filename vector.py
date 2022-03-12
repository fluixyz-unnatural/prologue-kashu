# parse.pyで作った和歌リストから歌集ベクトルを作る

from titles import titles
import json
import math 

# 和歌の集合である歌集をそれぞれtri-gramで処理する
def analyse_kashu(kashu):
    # 解析結果を保存するための辞書型
    out = {}
    out['vector'] = {}

    # parse.pyで作ったcsvを開く
    with open('./csvs/'+kashu+'.csv','r') as f:
        lines = f.read()

        # 和歌の数を保存しておく
        out['count'] = len(lines)

        # 和歌ごとに処理していく
        for l in lines.split('\n'):
            gram = waka_tri_gram(l)
            for g in gram:
                if g in out['vector'].keys() :
                    out['vector'][g] += 1
                else:
                    out['vector'][g] = 1
    
    # 正規化する
    r2 = 0
    dim = 50*50*50
    for key in out['vector']:
        r2 += out['vector'][key]**2
    r = math.sqrt(r2)
    for key in out['vector']:
        out['vector'][key] /= r
    return out

# 和歌は、「ふるいけや-かわずとびこむ-みずのおと」みたいに別れているので
# それぞれをtri_gramで処理する
def waka_tri_gram(waka):
    ans = []
    lines = waka.split('−')
    for l in lines:
        gram = tri_gram(l)
        ans.extend(gram)
    return ans

# 「あいうえお」を「あいう」「いうえ」「うえお」に分ける
# 詳しくはn-gramで検索
def tri_gram(s):
    gram = []
    for i in range(len(s)-2):
        gram.append(s[i:i+3])
    return gram

def main():
    # 歌集ごとに歌集ベクトルを作ってjsonで保存する
    for title in titles:
        data = analyse_kashu(title)
        with open('./jsons/'+title+'.json','w') as d:
            print(title)
            json.dump(data, d, ensure_ascii=False)


if __name__ == '__main__':
    main()
