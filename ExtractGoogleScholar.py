# Crawl The contents of Google Scholar
# Author : ls
# Create : 10/26,2013
# Revised: 11/16,2013

import urllib2
import re, random
from bs4 import BeautifulSoup


def GoogleScholarTitle(queryTitle):
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',\
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',\
               'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+',\
               '(KHTML, like Gecko) Element Browser 5.0',\
               'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
               'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
               'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
               'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)',\
               'Version/6.0 Mobile/10A5355d Safari/8536.25', \
               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)', \
               'Chrome/28.0.1468.0 Safari/537.36', \
               'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
    queryTitle = urllib2.quote(queryTitle.replace(' ', '+'))
##    queryTitle = queryTitle.replace(' ', '+')
##    print queryTitle
    url = 'http://scholar.google.com.hk/scholar?hl=zh-CN&q=%s' % queryTitle
##    print url
    request = urllib2.Request(url)
    index = random.randint(0, 9)
    user_agent = user_agents[index]
    request.add_header('User-agent', user_agent)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html)
    print soup.originalEncoding
##    print soup
##    print '---'
##    rankPaper = soup.findAll('div', attrs={'style':re.compile('z-index:.')}, limit = 1)
##    print result
    paperOnClick = soup.findAll('a', attrs = {'class':'gs_nph', 'href':'#'}, limit = 1)
    mClick = re.search(r'event,\'.+\',', str(paperOnClick[0]))
    if mClick:
        print mClick.group()[7:-2]
        clickProperty = mClick.group()[7:-2]
        refUrl = 'http://scholar.google.com.hk/scholar?q=info:%s:scholar.google.com/&output=cite&hl=zh-CN' % clickProperty
        refRequest = urllib2.Request(refUrl)
        refRequest.add_header('User-agent', user_agent)
        refResponse = urllib2.urlopen(refRequest)
        soup = BeautifulSoup(refResponse.read())
##        bibTex = soup.findAll('a', attrs = {'class':'gs_citi', 'target':'_blank'}, limit = 1)
        print soup.prettify()
        
        
    else:
        print 'The step of Click is error' 
    
##    if mClick:
##        strr = 
    
##    strr = str(paperOnClick[0])
##    print strr[1]
##    m = re.search('event', strr)
##    if m:
##        print 1
##    print m
##    print m.end()
##    print strr[m.end():]
##    m = re.search(r'\'.+\',', strr[m.end():])
##    print m.group()
##    strr = paperOnClick[0]
##    print strr._class_
##    onClick = paperOnClick[onclick]
##    print onClick
##    result = soup.findAll(attrs={'class':re.compile('z-index:%d+')})
##    result = soup.find('div', attrs)
    
    



title = 'A Coarse-to-fine approach for fast deformable object detection'
GoogleScholarTitle(title)



    
    
