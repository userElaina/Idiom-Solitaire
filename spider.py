import requests
from utils import *

u = "https://api-static.mihoyo.com/common/blackboard/bh3_wiki/v1/home/content/list?app_sn=bh3_wiki&channel_id=17"
res = requests.get(u)

# s = open('list.jfproj', 'rb').read().decode('utf8')
s = res.text

j = json.loads(s)
j = j['data']['list'][0]
j = j['children']

j2 = dict()

for i in j:
    # i['ch_ext'] = json.loads(i['ch_ext'])
    jid = i['id']
    jname = i['name']
    l = list()
    if jid == 38:
        continue
    elif jid == 18:
        j2[jname] = dict()
        for k in i['list']:
            u = 'https://api-static.mihoyo.com/common/blackboard/bh3_wiki/v1/content/info?app_sn=bh3_wiki&content_id=%d' % k['content_id']
            res = requests.get(u)
            s = res.text
            pattern = re.compile(r'角色/([^\\]+)\\')
            matches = re.findall(pattern, s)
            assert len(matches) == 1
            ch = matches[0]
            j2[jname].setdefault(ch, dict())

            pattern = re.compile(r'\\u003cli\s+data-target=\\"costume\.items\\"\s+data-index=\\"\d+\\"\s+class=\\"obc-tmpl__switch-btn\\"\\u003e\\n\s+([^\\]+)\\n\s+\\u003c/li\\u003e')
            # \u003cli data-target=\"costume.items\" data-index=\"0\" class=\"obc-tmpl__switch-btn\"\u003e\n      粉色妖精小姐♪\n    \u003c/li\u003e
            # <li data-target="costume.items" data-index="1" class="obc-tmpl__switch-btn"> 粉色甜心小姐♪ </li>
            matches = re.findall(pattern, s)
            if matches[0] != k['title']:
                print('!neq:', k['title'], matches[0])
            j2[jname][ch][k['title']] = matches
            l += matches
    elif jid in [21, 218, 19, 59, 20, 47]:
        # 人偶 协同者 圣痕 宿舍名册 武器 敌人
        for k in i['list']:
            l.append(k['title'])
        j2[jname] = l
    else:
        print('!jid:', jid, jname)
        continue
    # open('result/' + jname + '.list', 'wb').write('\n'.join(l).encode('utf8'))

svj(j2, 'res')

# !neq: 女武神 · 荣光 女武神·荣光
# !neq: 夜隐重霞 原皮
# !neq: 彼岸双生 彼岸双生-表人格
# !neq: 暮光骑士 · 月煌 暮光骑士·月煌
# !neq: 猎袭装 · 影铁 猎袭装-影铁
# !neq: 圣仪装 · 今样 圣仪装·今样
# !neq: 御神装 · 勿忘 御神装·勿忘
# !neq: 苍骑士 · 月魂 苍骑士·月魂
# !neq: 女武神 · 凯旋 女武神-凯旋
# !neq: 女武神 · 迅羽 女武神-迅羽
# !neq: 女武神 · 战车 女武神·战车
# !neq: 女武神 · 游侠 女武神·游侠
