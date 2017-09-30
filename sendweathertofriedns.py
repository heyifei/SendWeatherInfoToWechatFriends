#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1
@author: heyifei
@email:heyifei88@foxmail.com
@license: Apac_he Licence 
@file: sendweathertofriedns.py
@time: 2017/9/2 22:07
"""

import requests as req
from lxml import etree
import itchat


# def url
shanghai_url = "http://www.nmc.cn/publish/forecast/ASH/shang-hai.html"

changde_url = "http://www.nmc.cn/publish/forecast/AHN/chang-de.html"

chongqing_url = "http://www.nmc.cn/publish/forecast/ACQ/chong-qing.html"

# def friends
friends = ['@xxxxxxx',
           '@xxxxxxx',
           '@xxxxxxx',
           '@xxxxxxx',
           '@xxxxxxx',
           '@xxxxxxx',
           '@xxxxxxx']

def geturlinfobyxpath(url):
    '''get URL info'''
    kv = {'user-agent': 'Mozilla/5.0'}
    r = req.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    tree = etree.HTML(r.text)
    nodes = tree.xpath('//div[@class="day"]/div/text()')
    city = tree.xpath('//title/text()')
    updatetime = tree.xpath('//div[@class="btitle"]/span/text()')
    newnode ="".join(nodes).replace("\n", "").replace(" ", "")
    sms = "source：heyifei get data from www.nmc.cn。"
    sendsms = '%s%s%s%s' % (city, updatetime, newnode, sms)
    itchat.auto_login(hotReload=True)

    # to all friends
    # friends = itchat.get_friends()
    for f in friends:
          # to all friends
          # username = f.UserName
        itchat.send_msg(sendsms, toUserName=f)
    #print(sendsms)

if __name__ == '__main__':
    geturlinfobyxpath(shanghai_url)

