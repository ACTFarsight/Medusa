#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Yonyou import Yonyou
from OA.Weaver import Weaver
from OA.Ruvar import Ruvar
def Main(Url,FileName,Values,ProxyIp):
    try:
        Yonyou.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Weaver.Main(Url,FileName,Values,ProxyIp)
    except:
        pass
    try:
        Ruvar.Main(Url,FileName,Values,ProxyIp)
    except:
        pass