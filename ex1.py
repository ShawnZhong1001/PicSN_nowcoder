# -*- encoding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import re


# Page 5: Web Crawler from qiushibaike
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


# Page 6:
def demo_string():
    print "I love Ctrip!"
    print 'I love Ctrip!'
    print "I love 'Ctrip'!"
    print 'I love "Ctrip"!'
    print "I love \'Ctrip\'!"
    print "I" + " love" + " Ctrip" + "!"
    # string function: capitaliza(), replace(), startwith(), endwith()
    # len(), split(), find(), lstrip(), rstrip(), join()
    stra = "hello, world!"
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    print stra.startswith('hello')
    print stra.endswith('d')
    print len(stra)
    print stra.split(' ')
    print stra.find('!')
    strb = "\n\rhello nowcoder\r\n"
    print strb.lstrip()
    print strb.rstrip()
    print '-'.join(['a', 'b', 'c'])
    # make string turn into digit: ``;str;repr
    temp = 42
    print "The temperature is " + `temp`
    # long string
    print '''This is a very long string.
Still continue...
Still here.'''
    # newline
    print 1 + 2 \
          + 3
    # original string
    print r'Let\'s go!\\'


def demo_operator():
    print True, not True
    print 1 < 2
    print 2 << 3, 5 | 3, 5 & 3, 5 ^ 3
    x = 2
    y = 3.3
    print x, y, type(x), type(y)


def demo_buildinfunction():
    pass


def demo_controlflow():
    pass


def demo_list():
    lista = [1, 2, 3]
    listb = ['a', 1, 'b', 1.123]
    print lista, listb
    print 'a' in lista
    lista.extend(listb)
    print lista
    print len(lista)
    lista = lista + listb
    print lista
    listb.insert(0, 'www');
    print listb
    listb.pop(1);
    print listb  # 1 for position
    listb.reverse();
    print listb
    print listb[0], listb[-1]
    listb.sort();
    print listb
    listb.sort(reverse=True);
    print listb
    print listb * 2;
    print [0] * 14  # memset(src, 0, len)
    print '================'
    listhello = list('Hello')  # turn a string into a list
    print listhello
    print ''.join(listhello)  # turn a list into a string
    name = list('Perl')
    name[1:] = list('ython')
    print name
    name[5:5] = list('Learning')
    print name



def demo_tuple():
    pass


def demo_dict():
    pass


def demo_set():
    pass


def demo_exception():
    pass


def demo_random():
    pass


def demo_re():
    pass


if __name__ == '__main__':
    # comments
    # print "Hello, nowcoder!"
    # qiushibaike()
    # demo_string()
    # demo_operator()
    demo_list()
