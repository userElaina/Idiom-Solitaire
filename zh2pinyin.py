# pip install pypinyin

from pypinyin import pinyin, Style

print(pinyin(['aa你a v好☆dd☆','a','你的'], style=Style.NORMAL, heteronym=True, v_to_u=False))
# [['aa'], ['ni'], ['a v'], ['hao'], ['☆dd☆'], ['a'], ['ni'], ['de', 'di']]
