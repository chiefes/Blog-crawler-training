import urllib
import time
url = ['']*350
page = 1
link = 1
while page <= 7:
    con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read() 
    i = 0
    title = con.find("<a title=")
    href = con.find("href=", title)
    html = con.find(".html", href)
    while title != -1 and href != -1 and html != -1 and i < 50 :
        url[i]= con[href + 6:html + 5]
        print link,' ',url[i]
        title = con.find("<a title" , html)
        href = con.find("href=", title)
        html = con.find(".html", href)
        i = i + 1 
        link = link + 1
    else:
        print page,'find end!' 
    page = page + 1    

else:
    print "all find end"

j = 0
while j < 350:
    content = urllib.urlopen(url[j]).read()
    open(r"hanhan/"+url[j][-26:], 'w+') .write(content)
    print 'downloading', url[j]
    j = j + 1
    time.sleep(5)
else:
    print "download article finished"
