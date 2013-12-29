# Crawl The contents of Google Scholar
# Author : ls
# Create : 10/26,2013
# Revised: 12/22,2013


import re, random
import time
import LoadIpTxt
from GoogleScholarParse import GoogleScholar






##IP, NUMIP = LoadIpTxt.PraseTxtIP('1222Proxy.txt')
##ValidMax = 5
##IPValid = [ValidMax for i in range(NUMIP)]

              
                          
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


title = 'A Coarse-to-fine approach for fast deformable object detection'
api = GoogleScholar()
entry = api.searchTitle(title)
print entry

### Read the Arnet
##bNewEntry = False
##fileArent = open('F:/www/ArnetData/DBLP-citation-Feb21.txt')
##
### Write the bibEntry of google
##fileOutput = open('googleBibEntry.txt', 'a')
##
##startTime = time.clock()
##bLine = True
##nLine = 0
##skipLine = 6073
##numFail = 0
##numSucess = 0
##numRead = 0
##while bLine:
##    bLine, line, fileArent = ReadNewLine(fileArent) #bLine = 0, if the reach the end of file
##    if not bLine:
##        break
##    
##    nLine = nLine +1
##    if nLine < skipLine:
##        continue
##
##    #---- Skip lines ----
##    print 'the nline is %d' % nLine
##    print 'The number of arnet paper is %d' % numRead
##    print 'The number of sucess is %d' % numSucess
##
####    if numRead > 0:
####        break
##    #--- Reach the 10 times error ---
##    if numFail > 10:
##        print 'The next skipLine should be %d' % nLine
##        break
##    # -----------------------------------
##
##    bibType, mType = SeekBibType(line)
##    if mType and bibType == 'title':
##        # get a new entry
##        arnetEntry = {}
##        arnetEntry['title'] = line[mType.end():-1]
##
##        while bLine:
##            bLine, line, fileArent = ReadNewLine(fileArent)
##            nLine = nLine +1 # read a new line 
##            # Judge the null string
##            if not (bLine and line.strip()):
##                break
##            bibType, mType = SeekBibType(line)
##            if not mType: # break if meet the blank(Careful!!!),
##                continue 
##            
##            arnetEntry[bibType] = line[mType.end():-1]
##
##        numRead = numRead + 1
##
####        entry = arnetEntry
##        api = GoogleScholar()
##        entry = api.searchTitle(arnetEntry['title'])
##        print arnetEntry
##        print entry
##        # if isempty, and judge the field exist so conintue
##        if not entry or not entry.has_key('year') or not entry.has_key('title') \
##           or not arnetEntry.has_key('title') or not arnetEntry.has_key('year') \
##           or not arnetEntry.has_key('arnetid'):
##            numFail = numFail +1
##            print 'there is some error in the entry or the arnetEntry'
##            continue     
##        numFail = 0
##        
##
##        if re.search('\.\Z', arnetEntry['title']):
##            arnetEntry['title'] = arnetEntry['title'][:-1] # delete the end of .
##        if re.search('\.\Z', entry['title']):
##            entry['title'] = entry['title'][:-1] # delete the end of .
##        
##        # judge the entry equal the arnetEntry
##        if not entry['year'] == arnetEntry['year']:
##            print 'the year is not equal'
##            continue
##        if not entry['title'].upper() == arnetEntry['title'].upper():
##            print 'the title is not equal'
##            continue
##        
##        numSucess = numSucess + 1
##
##        entry['arnetid'] = arnetEntry['arnetid']
##        # Write the dict to the txt
##        # The arnetid Should in the first line 
##        fileOutput.write('arnetid')
##        fileOutput.write(':')
##        fileOutput.write(str(entry['arnetid']))
##        fileOutput.write('\n')
##        for key in entry:
##            if key == 'arnetid':
##                continue
##            fileOutput.write(key)
##            fileOutput.write(':')
##            fileOutput.write(str(entry[key]))
##            fileOutput.write('\n') 
##        fileOutput.write('\n')
##
##        
##        
##
##        
##fileArent.close()    
##fileOutput.close()
##endTime = time.clock()
##print "The time of ececute is %f" % (endTime-startTime)
##print 'The start line: %d, the end line: %d' % (skipLine, nLine)
##print 'The number of arnet paper is %d' % numRead
##print 'The number of sucess is %d' % numSucess

        

        

        

        
    
    





    
    
