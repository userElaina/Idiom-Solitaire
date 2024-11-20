from utils import *
import pypinyin

j = rdj('res3')
d = dict()

for i in j:
    ks = pypinyin.pinyin(
        i[0],
        style=pypinyin.Style.NORMAL,
        heteronym=True,
        v_to_u=False
    )[0]
    for k in ks:
        if k in d:
            if j[i] not in d[k]:
                d[k].append(j[i])
        else:
            d[k] = [j[i]]

svj(d, 'res4')
