from utils import *

j = rdj('res')
j2 = dict()
name: str = ''


item = '女武神'
j_i = dict()
for name in j[item]:
    j_name = dict()
    build: str = ''
    for build in j[item][name]:
        dress: str = ''
        l_dress = list()
        for dress in j[item][name][build]:
            dress = dress.replace('诡戏干役', '诡戏千役')
            dress = dress.replace('原皮', '夜隐重霞')
            dress = dress.replace('-表人格', '').replace('-里人格', '')
            if not dress.startswith('8'):
                dress = dress.replace('-', '·')
            dress = dress.replace(' · ', '·')
            if dress not in l_dress:
                l_dress.append(dress)
        build = build.replace('-', '·').replace(' · ', '·')
        if build != l_dress[0]:
            print(build, l_dress)
            raise ValueError(build)
        j_name[build] = l_dress

    j_i[name] = j_name
j2[item] = j_i


item = '人偶'
j_i = list()
for name in j[item]:
    name = name.replace(' ', '')
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


item = '协同者'
j_i = list()
for name in j[item]:
    matches = re.findall(ZH_PATTERN, name)
    name = matches[0]
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


item = '宿舍名册'
j_i = list()
for name in j[item]:
    name = name.replace('【宿舍】', '').replace(' ', '')
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


item = '圣痕'
j_i = list()
for name in j[item]:
    name = name.replace(' ', '')
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


item = '武器'
j_i = list()
for name in j[item]:
    name = name.replace(' · ', '·')
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


item = '敌人'
j_i = list()
pattern = r'\s*（[^)]+）'
for name in j[item]:
    name = name.replace(' · ', '·')
    name = name.replace(' -', '-').replace('- ', '-')
    matches = re.findall(pattern, name)
    for i in matches:
        name = name.replace(i, '')
    if name not in j_i:
        j_i.append(name)
j2[item] = j_i


svj(j2, 'res2')
