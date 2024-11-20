from utils import *
import pypinyin

clean_data = rdj('res2')
name: str = ''
deduplicate = dict()

item = '女武神'
for role in clean_data[item]:
    if role not in deduplicate:
        deduplicate[role] = role
    for build in clean_data[item][role]:
        for dress in clean_data[item][role][build]:
            matches = re.findall(ZH_PATTERN, dress)
            k = ''.join(matches)
            if k not in deduplicate:
                deduplicate[k] = dress
                for kk in matches[1:]:
                    if kk not in deduplicate:
                        deduplicate[kk] = dress
        del dress

for item in ['人偶', '协同者', '宿舍名册', '圣痕', '武器', '敌人']:
    for name in clean_data[item]:
        s = name.replace('(上)', '').replace('(中)', '').replace('(下)', '')
        s = s.replace('购物', '')
        s = s.replace('逐火十三英桀', '')
        s = s.replace('异能', '').replace('机械', '').replace('生物', '')
        matches = re.findall(ZH_PATTERN, s)
        if len(matches) < 1:
            continue
        k = ''.join(matches)
        if k not in deduplicate:
            deduplicate[k] = name
            for kk in matches[1:]:
                if kk not in deduplicate:
                    deduplicate[kk] = name

svj(deduplicate, 'res3')
py1 = dict()

for i in deduplicate:
    ks = pypinyin.pinyin(
        i[0],
        style=pypinyin.Style.NORMAL,
        heteronym=True,
        v_to_u=False
    )[0]
    for k in ks:
        if k in py1:
            if deduplicate[i] not in py1[k]:
                py1[k].append(deduplicate[i])
        else:
            py1[k] = [deduplicate[i]]

svj(py1, 'res4')
