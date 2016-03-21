#codeing:utf-8

import urllib
#import time
url = ['']*350
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read() 
i = 0
title = con.find("<a title=")
href = con.find("href=", title)
html = con.find(".html", href)
while title != -1 and href != -1 and html != -1 and i < 50 :
    url[i]= con[href + 6:html + 5]
    print url[i]
    title = con.find("<a title" , html)
    href = con.find("href=", title)
    html = con.find(".html", href)
    i = i + 1 
else:
    print 'find end!' 


#j = 0
#while j < 50:
    #content = urllib.urlopen(url[j]).read()
    #open(r"hanhan/"+url[j][-26:], 'w+') .write(content)
    #print 'downloading', url[j]
    #j = j + 1
    #time.sleep(1)
#else:
    #print "download article finished"

    

