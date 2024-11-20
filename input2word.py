import os
import json
try:
    import pypinyin
    def _pypinyin_dict(words: list) -> dict:
        ans = dict()
        _words = ''
        for i in words:
            _i = i[-1]
            if _i not in _words:
                _words += _i
        _py = pypinyin.pinyin(
            _words,
            style=pypinyin.Style.NORMAL,
            heteronym=True,
            v_to_u=False
        )
        for idx in range(len(_words)):
            for pronounce in _py[idx]:
                ans.setdefault(pronounce, '')
                ans[pronounce] += _words[idx]
        return ans
except ImportError:
    print('(optional) pinyin support: pip install pypinyin')


STR_ZH = '__zh__'
FILE_DIR = os.path.dirname(os.path.abspath('.'))
FILE_HI3RD = os.path.join(
    FILE_DIR,
    'Honkai-Impact-3rd-Input-Dictionary',
    'data',
    'head.json'
)

DICT_HI3RD: dict = json.loads(open(FILE_HI3RD, 'rb').read().decode('utf8'))

def dict_hi3rd(s: str) -> list:
    return DICT_HI3RD.get(s, list())


all_dict_func = {
    '崩坏3rd': dict_hi3rd
}

def find_from_pinyin(pronounce: str) -> dict:
    return {d:all_dict_func[d](pronounce) for d in all_dict_func}


def finds_from_pinyin(l: list) -> dict:
    ans = dict()
    for pronounce in l:
        if pronounce in ans:
            continue
        ans[pronounce] = find_from_pinyin(pronounce)
    return ans


def finds_from_zh(words: list) -> dict:
    _zh = _pypinyin_dict(words)
    ans = finds_from_pinyin(_zh.keys())
    for pronounce in _zh:
        ans[pronounce][STR_ZH] = _zh[pronounce]
    return ans


def find_from_zh(word: str) -> dict:
    return finds_from_zh([word])


def prt_msg(ans: dict, dict_name: bool = True) -> str:
    s = ''
    for pronounce in ans:
        s += pronounce
        if STR_ZH in ans[pronounce]:
            s += ' (%s)' % ans[pronounce][STR_ZH]
        s += ':'
        _empty_flg = True
        for dictionary in ans[pronounce]:
            if dictionary == STR_ZH:
                continue
            for word in ans[pronounce][dictionary]:
                _empty_flg = False
                s += '\n ' + word
                if dict_name:
                    s += ' (%s)' % dictionary
        if _empty_flg:
            s += ' (无)'
        s += '\n\n'
    return s


if __name__ == '__main__':
    print('start')
    while True:
        s = input('>>> ')
        _py = pypinyin.pinyin(
            s,
            style=pypinyin.Style.NORMAL,
            heteronym=True,
            v_to_u=False
        )[-1]
        ans = finds_from_pinyin(_py)
        print(prt_msg(ans)[:-2])
