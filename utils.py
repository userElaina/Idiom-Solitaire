import re
import json

ZH_PATTERN = r'[\u4e00-\u9fa5]+'


def svj(j: dict, nm: str) -> None:
    s = json.dumps(j, ensure_ascii=False, indent=4)
    open('result/%s.json' % nm, 'wb').write(s.encode('utf8'))


def rdj(nm: str) -> dict:
    return json.loads(open('result/%s.json' % nm, 'rb').read().decode('utf8'))
