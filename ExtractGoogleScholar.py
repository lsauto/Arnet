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

class ParseBibType():
    def TypeArticle(self, strr):
        if re.search('\@article', strr):
            return 1
        else:
            return 0
    def TypeInproceedings(self, strr):
        if re.search('\@inproceedings', strr):
            return 2
        else:
            return 0

        
class ParseBibEntries():
    def EnAddress(self, strr):
        mm = re.search('(?<=address={).*?(?=})', strr)
        return 'address', mm

    def EnAnnote(self, strr):
        mm = re.search('(?<=annote={).*?(?=})', strr)
        return 'annote', mm
    
    def EnAuthor(self, strr):
        mm = re.search('(?<=author={).*?(?=})', strr)
        return 'author', mm

    def EnBooktitle(self, strr):
        mm = re.search('(?<=booktitle={).*?(?=})', strr)
        return 'booktitle', mm

    def EnChapter(self, strr):
        mm = re.search('(?<=chapter={).*?(?=})', strr)
        return 'chapter', mm

    def EnCrossref(self, strr):
        mm = re.search('(?<=crossref={).*?(?=})', strr)
        return 'crossref', mm

    def EnEdition(self, strr):
        mm = re.search('(?<=edition={).*?(?=})', strr)
        return 'edition', mm

    def EnEditor(self, strr):
        mm = re.search('(?<=editor={).*?(?=})', strr)
        return 'editor', mm

    def EnEprint(self, strr):
        mm = re.search('(?<=eprint={).*?(?=})', strr)
        return 'eprint', mm

    def EnHowpublished(self, strr):
        mm = re.search('(?<=howpublished={).*?(?=})', strr)
        return 'howpublished', mm

    def EnInstitution(self, strr):
        mm = re.search('(?<=institution={).*?(?=})', strr)
        return 'institution', mm

    def EnJournal(self, strr):
        mm = re.search('(?<=journal={).*?(?=})', strr)
        return 'journal', mm

    def EnKey(self, strr):
        mm = re.search('(?<=key={).*?(?=})', strr)
        return 'key', mm

    def EnMonth(self, strr):
        mm = re.search('(?<=month={).*?(?=})', strr)
        return 'month', mm

    def EnNote(self, strr):
        mm = re.search('(?<=note={).*?(?=})', strr)
        return 'note', mm

    def EnNumber(self, strr):
        mm = re.search('(?<=number={).*?(?=})', strr)
        return 'number', mm

    def EnOrganization(self, strr):
        mm = re.search('(?<=organization={).*?(?=})', strr)
        return 'organization', mm

    def EnPages(self, strr):
        mm = re.search('(?<=pages={).*?(?=})', strr)
        return 'pages', mm

    def EnPublisher(self, strr):
        mm = re.search('(?<=publisher={).*?(?=})', strr)
        return 'publisher', mm

    def EnSchool(self, strr):
        mm = re.search('(?<=school={).*?(?=})', strr)
        return 'school', mm

    def EnSeries(self, strr):
        mm = re.search('(?<=series={).*?(?=})', strr)
        return 'series', mm

    def EnTitle(self, strr):
        mm = re.search('(?<=title={).*?(?=})', strr)
        return 'title', mm

    def EnType(self, strr):
        mm = re.search('(?<=type={).*?(?=})', strr)
        return 'type', mm

    def EnUrl(self, strr):
        mm = re.search('(?<=url={).*?(?=})', strr)
        return 'url', mm

    def EnVolume(self, strr):
        mm = re.search('(?<=volume={).*?(?=})', strr)
        return 'volume', mm

    def EnYear(self, strr):
        mm = re.search('(?<=year={).*?(?=})', strr)
        return 'year', mm
        
        
def ParseBibTex(strr):
    entry = {}
    paperType = ['TypeArticle', 'TypeInproceedings']
    for n in range(2):
        ty = getattr(ParseBibType(), paperType[n])(strr)
        if ty:
            entry['type'] = ty
            break

    entryType = ['EnAddress', 'EnAnnote', 'EnAuthor', 'EnBooktitle', 'EnChapter', 'EnCrossref',\
                 'EnEdition', 'EnEditor', 'EnEprint', 'EnHowpublished', 'EnInstitution', 'EnJournal',\
                 'EnKey', 'EnMonth', 'EnNote', 'EnNumber', 'EnOrganization', 'EnPages',\
                 'EnPublisher', 'EnSchool', 'EnSeries', 'EnTitle', 'EnType', 'EnUrl', \
                 'EnVolume', 'EnYear']
    for n in range(26):
        bibEntry, mm = getattr(ParseBibEntries(), entryType[n])(strr)
        if mm:
            entry[bibEntry] = mm.group()

    return entry
            

    
    

    
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
##        try:
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

##            print bibRes

            return ParseBibTex(bibRes)
                

##        except:
##            print 'error'
                
                
                


title = 'A Coarse-to-fine approach for fast deformable object detection'
api = GoogleScholar()
entry = api.searchTitle(title)
print entry
    




    
    
