# Crawl The contents of Google Scholar
# Author : ls
# Create : 10/26,2013
# Revised: 11/19,2013

import urllib2
import re, random
from bs4 import BeautifulSoup


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
class GoogleScholar:
    def __init__(self):
        self.index = 0

    def getHtml(self, url):
        request = urllib2.Request(url)
        user_agent = user_agents[self.index]
        request.add_header('User-agent', user_agent)
        response = urllib2.urlopen(request)
        return response.read()
    
    def searchTitle(self, queryTitle):
        
        self.index = random.randint(0, 9)
        try:
            # the first layer
            queryTitle = urllib2.quote(queryTitle.replace(' ', '+'))
            url = 'http://scholar.google.com.hk/scholar?hl=zh-CN&q=%s' % queryTitle
            queryRes = self.getHtml(url)
            soup = BeautifulSoup(queryRes)
            paperOnClick = soup.findAll('a', attrs = {'class':'gs_nph', 'href':'#'}, limit = 1)
            mClick = re.search(r'event,\'.+\',', str(paperOnClick[0]))
            if mClick:
                # the second layer
                clickProperty = mClick.group()[7:-2]
                refUrl = 'http://scholar.google.com.hk/scholar?q=info:%s:scholar.google.com/&output=cite&hl=zh-CN' % clickProperty
                refRes = self.getHtml(refUrl)
                soup = BeautifulSoup(refRes)
                bibTex = soup.find('a', text = re.compile(u'BibTeX'))

                # the third layer
                bibUrl = 'http://scholar.google.com.hk'+bibTex['href']
                bibRes = self.getHtml(bibUrl)

                print bibRes

        except:
            print 'error'
                
                
                


title = 'A Coarse-to-fine approach for fast deformable object detection'
api = GoogleScholar()
api.searchTitle(title)            
    




    
    
