#!/usr/bin/env python3

import MeCab

def mecab_tokenize(text: str) -> list:
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)
    result = []
    while node:
        word = node.surface
        pos = node.feature.split(',')[0]
        # if pos in ['名詞', '動詞', '形容詞']:
        result.append(word)
        node = node.next
    return result

if __name__ == '__main__':
    text = '私は私のことが好きなあなたが好きです'
    print(mecab_tokenize(text))
