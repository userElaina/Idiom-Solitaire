from utils import *

j = rdj('res2')
name: str = ''
deduplicate = dict()


item = '女武神'
for name in j[item]:
    if name not in deduplicate:
        deduplicate[name] = name
    for build in j[item][name]:
        for dress in j[item][name][build]:
            matches = re.findall(ZH_PATTERN, dress)
            k = ''.join(matches)
            if k not in deduplicate:
                deduplicate[k] = dress
                for kk in matches[1:]:
                    if kk not in deduplicate:
                        deduplicate[kk] = dress


for item in ['人偶', '协同者', '宿舍名册', '圣痕', '武器', '敌人']:
    for name in j[item]:
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
                    deduplicate[kk] = dress


svj(deduplicate, 'res3')
