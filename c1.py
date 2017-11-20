#coding=utf8
import requests
from bs4 import BeautifulSoup
import random
import re

def demo_craw_xiushi():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()

def demo_list():
    lista =[1,2,3]
    print 1,lista
    listb=['a',1,'c',1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,len(lista)
    lista=lista+listb
    print 6,lista
    listb.insert(0,'www')
    print 7,listb
    listb.pop(1)
    print 8,listb
    listb.reverse()
    print 9,listb
    print 10,listb[0],listb[1]
    listb.sort(reverse=True)
    print 11,listb
    listb.sort()
    print 12,listb
    print 13,listb*2
    print 14,[0]*14

    tuplea=(1,2,3)
    listaa=[1,2,3]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def demo_dict():
    dicta={1:1,2:4,3:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('3')
    for key,value in dicta.items():
        print 'key_value:',key,value
    dictb={'+':add,'-':sub}
    print 4,dictb['+'](3,4)
    print 5,dictb['-'](5,3)
    dictb['*']='x'
    print dictb
    dicta.pop(3)
    print dicta

def demo_set():#需要区分tuple 和 set的结构
    seta=set((1,2,3))#seta=set([1,2,3])
    setb=set((2,3,4))
    print 1,seta
    print 2,seta.intersection(setb),seta & setb
    print 3,seta|setb,seta.union(setb)
    print 4,seta-setb

class User:
    type='USER'

    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def __repr__(self):
        return 'im '+self.name+' '+str(self.uid)
class Admin(User):
    type='ADMIN'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group=group
    def __repr__(self):
        return 'im '+self.name+' '+str(self.uid)+' '+self.group


def create_user(type):
    if type=='USER':
        return User('u1',1)
    elif type=='ADMIN':
        return Admin('a1',101,'g1')
    else:
        raise ValueError('error')

def demo_exception():
    try:
        print 2/1
        # print 2/0
        raise Exception('Raise Error','NowCoder')

    except Exception as e:
        print 'error:',e
    finally:
        print 'clearn up'
def demo_random():
    random.seed(1)
    print 1,int(random.random()*100)
    print 2,random.randint(0,200)
    print 3,random.choice(range(0,100))
    print 4,random.sample(range(0,100),4)
    a=[1,2,3,4,5]
    random.shuffle(a)
    print 5,a


def demo_re():
    str='abc123def12gh15'
    pl=re.compile('[\d]+')
    p2=re.compile('\d')

    print pl.findall(str)
    print p2.findall(str)

    str='a@163.com;b@gmail.com;c@qq.com;e@163.com;'
    p3=re.compile('[\w]+@[163|qq]+\.com')
    print p3.findall(str)

    str='<html><h>title</h><body>xxx</body></html>'
    p4=re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    p5=re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5,p5.findall(str)

    str='xxxxx2016-06-11yy'
    p6=re.compile('\d{4}-\d{2}-\d{2}')
    print p6.findall(str)

if __name__ == '__main__':
    # demo_craw_xiushi()
    # demo_list()
    # demo_dict()
    # demo_set()

    # user1=User('u1',1)
    # print user1
    # admin1=Admin('al',101,'g1')
    # print admin1
    # print create_user('USER')

    # demo_exception()
    # demo_random()
    demo_re()
