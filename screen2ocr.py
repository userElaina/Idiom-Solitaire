# conda create -y -n py311 python=3.11
# conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 cpuonly -c pytorch -y
# conda install pillow==9.4.0 numpy easyocr cpuonly -c pytorch -y
# pip install keyboard

import re
import sys
import time
import easyocr
import keyboard
import numpy as np
from PIL import ImageGrab

reader = easyocr.Reader(['ch_sim'])
# reader = easyocr.Reader(['ch_sim', 'en'])

def ocr(img: np.ndarray) -> str:
    return reader.readtext(img)

if __name__ == '__main__':
    print('start')
    while True:
        if keyboard.is_pressed('ctrl+c'):
            sys.exit(0)
        if keyboard.is_pressed('windows+shift+s'):
            print('get Meta Shift S')
            time.sleep(5)

            print('get img')
            img = ImageGrab.grabclipboard()
            while img is None:
                img = ImageGrab.grabclipboard()
            data = np.array(img)

            print('ocr img')
            l = list()
            pattern = r'[\u4e00-\u9fa5]+'
            for idx, s, acc in ocr(data):
                matches = re.findall(pattern, s)
                l += matches
            print('ocr:', ' '.join(l))
