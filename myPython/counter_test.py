# -*- coding: utf-8 -*-

from collections import Counter


""" Counter() 方法，获取列表中元素的出现次数 """
words = ['look', 'at', 'my', 'eyes', 'look', 'at', 'my', 'eyes', 'look', 'at', 'my', 'eyes']

a = Counter(words)

print(a)

morewords = ['this', 'is', 'my', 'eyes']

b = Counter(morewords)

print(b)
