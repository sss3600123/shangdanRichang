#coding: utf-8


from operator import itemgetter
"""
    根据 元素的 值排序
"""
rows = [
    {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
    { 'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

for row in rows:
    for k, v in row.items():
        print(k, v)


rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

rows_by_fname2 = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname2)


rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)