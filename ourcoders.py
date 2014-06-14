# -*- coding:utf-8 -*-
import urllib2
import re

query = u"{query}"

if query != 'new' and query != 'hot' and query != 'cold':
    print """
    <?xml version="1.0"?>
    <items>
    <item uid="Ourcode" arg="http://ourcoders.com">
        <title>ourcoders.com</title>
        <subtitle>直接访问</subtitle>
        <icon type="fileicon"></icon>
    </item>
    </items>
    """
else:
    ocurl = "http://ourcoders.com/thread/"
    surl = ""
    if query == 'new':
        query = ''
    
    surl = ocurl + query
    f = urllib2.urlopen(surl).read()
    res = re.findall(r'<a href="/thread/show/\d+/">[^<]+</a>', f)
    c = re.compile(r'<a href="/thread/show/([^\D]+)/">([^<]+)</a>')

    print """
    <?xml version="1.0"?>
    <items>
    """
    
    for r in res:
        s = c.search(r)
        link = ocurl + 'show/' + s.group(1)
        print '<item uid="ourcoder" arg="' + link + '">'
        print '    <title>' + s.group(2) + '</title>'
        print '    <subtitle>' + link +'</subtitle>'
        print '    <icon type="fileicon"></icon>'
        print '</item>'

    print """
    </items>
    """