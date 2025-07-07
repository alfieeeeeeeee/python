import requests
import xml.etree.ElementTree as ET

from datetime import datetime
from sys import argv

import warnings
warnings.filterwarnings('ignore')



class Converter:
    def __init__(self):
        self.base58 = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
        self.digit_map = [11, 10, 3, 8, 4, 6]
        self.xor_magic = 177451812
        self.add_magic = 8728348608
        self.template = list('BV1  4 1 7  ')

    def decode(self, cipher):
        plain = 0
        for i, digit in enumerate(self.digit_map):
            plain += self.base58.index(cipher[digit]) * 58 ** i
        return 'av%s' % ((plain - self.add_magic) ^ self.xor_magic)

    def encode(self, plain):
        plain = (int(plain[2:]) ^ self.xor_magic) + self.add_magic
        for i, digit in enumerate(self.digit_map):
            self.template[digit] = self.base58[plain // 58 ** i % 58]
        return ''.join(self.template)



if __name__ == '__main__':

    assert len(argv) == 2, 'Too many arguments'
    aid = argv[1]

    if aid.startswith('http'):
        aid = aid.replace('/?', '?').split('?')[0].split('/')[-1]

    if aid.startswith('BV'):
        assert len(aid) == 12, 'Invalid BV number'
        aid = Converter().decode(aid)

    if not aid.startswith('av'):
        raise ValueError('Invalid input')

    print('Requesting cid')
    cid_api = 'https://api.bilibili.com/x/player/pagelist?aid=%s' % aid[2:]
    ret = requests.get(cid_api).json()['data'][0]
    cid, title = ret['cid'], ret['part']

    print('Requesting danmaku')
    dmk_api = 'https://api.bilibili.com/x/v1/dm/list.so?oid=%d' % cid
    dmk = requests.get(dmk_api).content

    print('Parsing XML')
    root = ET.fromstring(dmk)
    elts = root.findall('d')
    processed = []

    for elt in elts:

        progress, mode, fontsize, color, ctime, _, hash, id, *_ = elt.attrib['p'].split(',')
        if color == 'undefined':
            color = '16777215'

        text = elt.text.replace('"', '""').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        if '""' in text or ',' in text:
            text = '"%s"' % text

        processed.append((
            '%08.3f' % float(progress),
            datetime.fromtimestamp(int(ctime)).strftime('%Y-%m-%d %H:%M:%S'),
            '%19d' % int(id),
            '%08x' % int(hash, 16),
            '#%06X' % int(color),
            mode, fontsize, text
        ))

    print('Saving to CSV')
    FILENAME_OUT = 'danmaku_%s_%s_%d.csv' % (aid, title, int(datetime.now().timestamp()))
    with open(FILENAME_OUT, 'w', encoding='utf-8') as fout:
        fout.write('PROGRESS,CTIME,ID,HASH,COLOR,MODE,FONTSIZE,TEXT\n')
        processed = sorted(processed, key=lambda x: x[1])
        processed = sorted(processed, key=lambda x: x[0])
        for line in processed:
            fout.write(','.join(line) + '\n')
