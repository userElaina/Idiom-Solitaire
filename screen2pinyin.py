import re
import sys
import time
import easyocr
import keyboard
import numpy as np
from PIL import ImageGrab
import pypinyin

ZH_PATTERN = r'[\u4e00-\u9fa5]+'

reader = easyocr.Reader(['ch_sim'])
# reader = easyocr.Reader(['ch_sim', 'en'])

def ocr(img: np.ndarray) -> str:
    return reader.readtext(img)

def f1() -> None:
    print('get Meta Shift S')
    time.sleep(5)

    print('get img')
    img = ImageGrab.grabclipboard()
    while img is None:
        img = ImageGrab.grabclipboard()
    data = np.array(img)

    print('get str')
    l = list()
    for idx, s, acc in ocr(data):
        matches = re.findall(ZH_PATTERN, s)
        l += matches
    print('ocr:', ' '.join(l))

    print('get pinyin')
    s = ''
    for i in l:
        if i[0] not in s:
            s += i[0]
    # print('zh:', s)

    l = pypinyin.pinyin(
        s,
        style=pypinyin.Style.NORMAL,
        heteronym=True,
        v_to_u=False
    )
    # print('pinyin:', l)

    d = dict()
    for i, j in enumerate(s):
        for k in l[i]:
            if k in d:
                d[k].append(j)
            else:
                d[k] = [j]
    print('pinyin:', d)


if __name__ == '__main__':
    print('start')
    while True:
        if keyboard.is_pressed('ctrl+c'):
            sys.exit(0)
        if keyboard.is_pressed('windows+shift+s'):
            f1()
