#!/usr/env/bin python3
# -*- coding:utf-8 -*-
def paqu_gushi(r):
    soup = BeautifulSoup(r.content, 'lxml' )
    f= open('wenjian.txt', 'w')
    for tag in soup.find_all('div', class_ = 'guwencont2'):
        shi_name = tag.get_text()
        # shi_name = soup.find_all('a')
        # print('%s'%(shi_name))
        f.write( '%s\n' % (shi_name))

    f.close()    
