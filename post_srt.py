# -*- coding: utf-8 -*-
import os,sys
import re
import chardet
#获取文件夹下所有srt文件并且删除最后一个文件（.py）
dir=sys.path[0]
dirlist=os.listdir(dir)
dirlist.pop()

linelist=[]
for f in dirlist:
    file=open(f,"r")
    while True:
        line=file.readline()
        reline=re.compile(line)
        if(reline.match("00:00:00,000 --> 00:00:00,000\n")):
            break
        linelist.append(line)
    file.close
    newlinelist=[]
    for l in linelist:
	    lg=l.decode('gbk')
	    nu=lg.encode('utf-8')
	    newlinelist.append(nu)

    #把list写入新文件并覆盖
    new=open(f,'w+')
    length=len(newlinelist)
    new.writelines(newlinelist[0:length-2])
    new.flush
    new.close


