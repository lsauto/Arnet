# Crawl The contents of Google Scholar
# Author : ls
# Create : 10/26,2013
# Revised: 11/24,2013

import urllib2
import re, random
import time
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

    def TypeBook(self, strr):
        if re.search('\@book', strr):
            return 2
        else:
            return 0
        
    def TypeBooklet(self, strr):
        if re.search('\@booklet', strr):
            return 3
        else:
            return 0

    def TypeConference(self, strr):
        if re.search('\@conference', strr):
            return 4
        else:
            return 0

    def TypeInbook(self, strr):
        if re.search('\@inbook', strr):
            return 5
        else:
            return 0

    def TypeIncollection(self, strr):
        if re.search('\@incollection', strr):
            return 6
        else:
            return 0

    def TypeInproceedings(self, strr):
        if re.search('\@inproceedings', strr):
            return 7
        else:
            return 0

    def TypeManual(self, strr):
        if re.search('\@manual', strr):
            return 8
        else:
            return 0

    def TypeMastersthesis(self, strr):
        if re.search('\@mastersthesis', strr):
            return 9
        else:
            return 0

    def TypeMisc(self, strr):
        if re.search('\@misc', strr):
            return 10
        else:
            return 0

    def TypePhdthesis(self, strr):
        if re.search('\@phdthesis', strr):
            return 11
        else:
            return 0

    def TypeProceedings(self, strr):
        if re.search('\@proceedings', strr):
            return 12
        else:
            return 0

    def TypeTechreport(self, strr):
        if re.search('\@techreport', strr):
            return 13
        else:
            return 0

    def TypeUnpublished(self, strr):
        if re.search('\@unpublished', strr):
            return 14
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
    paperType = ['TypeArticle', 'TypeBook', 'TypeBooklet', 'TypeConference', 'TypeInbook', \
                 'TypeIncollection', 'TypeInproceedings', 'TypeManual', 'TypeMastersthesis', 'TypeMisc', \
                 'TypePhdthesis', 'TypeProceedings', 'TypeTechreport', 'TypeUnpublished']
    for n in range(14):
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

    def randomSleep(self):
        sleeptime = random.randint(30, 90)
        time.sleep(sleeptime)
    
    def searchTitle(self, queryTitle):
        self.randomSleep()
        
        self.index = random.randint(0, 9)
##        try:
        # the first layer
        queryTitle = urllib2.quote(queryTitle.replace(' ', '+'))
        url = 'http://scholar.google.com.hk/scholar?hl=zh-CN&q=%s' % queryTitle
        queryRes = self.getHtml(url)
        soup = BeautifulSoup(queryRes)
        topFirst = soup.find('div', attrs = {'style':re.compile(u'z-index:')})
        soup = BeautifulSoup(str(topFirst))
        
        pdfA = soup.find('a', attrs = {'href':re.compile(u'.pdf\Z')}) # find the the url of pdf
        
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

            entry = ParseBibTex(bibRes)
            if pdfA:
                entry['pdfurl'] = pdfA['href']

            return entry
                

##        except:
##            print 'error'
                
                          
def ReadNewLine(fileArent):
    line = fileArent.readline()
    bLine = True
    if not line:
        bLine = False
    return bLine, line, fileArent

class Seeks():
    def SeekTitle(self, line):
        pattern = re.compile(r'\#\*')
        match = pattern.match(line)
        return 'title', match
    def SeekAuthors(self, line):
        pattern = re.compile(r'\#\@')
        match = pattern.match(line)
        return 'authors',match
    def SeekYear(self, line):
        pattern = re.compile(r'\#year')
        match = pattern.match(line)
        return 'year', match
    def SeekConf(self, line):
        pattern = re.compile(r'\#conf')
        match = pattern.match(line)
        return 'conf', match
    def SeekCitation(self, line):
        pattern = re.compile(r'\#citation')
        match = pattern.match(line)
        return 'citation', match
    def SeekIndex(self, line):
        pattern = re.compile(r'\#index')
        match = pattern.match(line)
        return 'index', match
    def SeekArnetID(self, line):
        pattern = re.compile(r'\#arnetid')
        match = pattern.match(line)
        return 'arnetid', match
    def SeekRefs(self, line):
        pattern = re.compile(r'\#\%')
        match = pattern.match(line)
        return 'ref', match
    def SeekAbstract(self, line):
        pattern = re.compile(r'\#\!')
        match = pattern.match(line)
        return 'abstract', match

# only need the title, year, arentid  
def SeekBibType(line):
    funType = ['SeekTitle', 'SeekYear', 'SeekArnetID']#

    if line.isspace():
        bibType = []
        match = False
    else:
        for n in range(3):
            bibType, match = getattr(Seeks(), funType[n])(line)
            if match:
                break

    return bibType, match


##title = 'A Coarse-to-fine approach for fast deformable object detection'
##api = GoogleScholar()
##entry = api.searchTitle(title)
##print entry

# Read the Arnet
bNewEntry = False
fileArent = open('F:/www/ArnetData/DBLP-citation-Feb21.txt')

# Write the bibEntry of google
fileOutput = open('googleBibEntry.txt', 'a')

startTime = time.clock()
bLine = True
nLine = 0
skipLine = 0
numFail = 0
numSucess = 0
numRead = 0
while bLine:
    bLine, line, fileArent = ReadNewLine(fileArent) #bLine = 0, if the reach the end of file
    if not bLine:
        break

    #---- Skip lines ----
    print 'the nline is %d' % nLine
    nLine = nLine +1
    if nLine < skipLine:
        continue

##    if numRead > 1:
##        break
    #--- Reach the 10 times error ---
    if numFail > 10:
        print 'The next skipLine should be %d' % n
        break
    # -----------------------------------

    bibType, mType = SeekBibType(line)
    if mType and bibType == 'title':
        # get a new entry
        arnetEntry = {}
        arnetEntry['title'] = line[mType.end():-1]

        while bLine:
            bLine, line, fileArent = ReadNewLine(fileArent)
            nLine = nLine +1 # read a new line 
            # Judge the null string
            if not (bLine and line.strip()):
                break
            bibType, mType = SeekBibType(line)
            if not mType: # break if meet the blank(Careful!!!),
                continue 
            
            arnetEntry[bibType] = line[mType.end():-1]

        numRead = numRead + 1


##        entry = arnetEntry
        if re.search('\.\Z', arnetEntry['title']):
            arnetEntry['title'] = arnetEntry['title'][:-1] # delete the end of .
        api = GoogleScholar()
        entry = api.searchTitle(arnetEntry['title'])
        print arnetEntry
        print entry
        # if isempty, and judge the field exist so conintue
        if not entry or not entry.has_key('year') or not entry.has_key('title') \
           or not arnetEntry.has_key('title') or not arnetEntry.has_key('year') \
           or not arnetEntry.has_key('arnetid'):
            numFail = numFail +1
            print 'there is some error in the entry or the arnetEntry'
            continue     
        numFail = 0
        

        
        # judge the entry equal the arnetEntry
        if not entry['year'] == arnetEntry['year']:
            print 'the year is not equal'
            continue
        if not entry['title'].upper() == arnetEntry['title'].upper():
            print 'the title is not equal'
            continue
        
        numSucess = numSucess + 1

        entry['arnetid'] = arnetEntry['arnetid']
        # Write the dict to the txt
        # The arnetid Should in the first line 
        fileOutput.write('arnetid')
        fileOutput.write(':')
        fileOutput.write(str(entry['arnetid']))
        fileOutput.write('\n')
        for key in entry:
            if key == 'arnetid':
                continue
            fileOutput.write(key)
            fileOutput.write(':')
            fileOutput.write(str(entry[key]))
            fileOutput.write('\n') 
        fileOutput.write('\n')

        
        

        
fileArent.close()    
fileOutput.close()
endTime = time.clock()
print "The time of ececute is %f" % (endTime-startTime)
print 'The start line: %d, the end line: %d' % (skipLine, nLine)
print 'The number of arnet paper is %d' % numRead
print 'The number of sucess is %d' % numSucess

        

        

        

        
    
    





    
    
