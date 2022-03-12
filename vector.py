from titles import titles
import json
import math 

def analyse_kashu(kashu):
    out = {}
    out['vector'] = {}
    with open('./csvs/'+kashu+'.csv','r') as f:
        lines = f.read()
        out['count'] = len(lines)
        for l in lines.split('\n'):
            gram = waka_tri_gram(l)
            for g in gram:
                if g in out['vector'].keys() :
                    out['vector'][g] += 1
                else:
                    out['vector'][g] = 1
    r2 = 0
    dim = 50*50*50
    for key in out['vector']:
        r2 += out['vector'][key]**2
    r = math.sqrt(r2)
    for key in out['vector']:
        out['vector'][key] /= r
    return out

def waka_tri_gram(waka):
    ans = []
    lines = waka.split('−')
    for l in lines:
        gram = tri_gram(l)
        ans.extend(gram)
    return ans

def tri_gram(s):
    gram = []
    for i in range(len(s)-2):
        gram.append(s[i:i+3])
    return gram

def main():
    for title in titles:
        data = analyse_kashu(title)
        with open('./jsons/'+title+'.json','w') as d:
            print(title)
            json.dump(data, d, ensure_ascii=False)


if __name__ == '__main__':
    main()
