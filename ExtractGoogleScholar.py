# Crawl The contents of Google Scholar
# Author : ls
# Create : 10/26,2013
# Revised: 01/12,2013
import random,re
import time
import LoadIpTxt
from GoogleScholarParse import GoogleScholar
from ArnetFileParse import Arnet



##title = 'A Coarse-to-fine approach for fast deformable object detection'
##api = GoogleScholar()
##entry = api.searchTitle(title, False, '61.144.48.169:3128')
##print entry

skipLine = 6442
arnet = Arnet('F:/www/ArnetData/DBLP-citation-Feb21.txt', skipLine)
api = GoogleScholar()
# Write the bibEntry of google
fileOutput = open('googleBibEntry.txt', 'a')

ip, numIp = LoadIpTxt.PraseTxtIP('0107Proxy.txt')
validMax = 1
ipValid = [validMax for i in range(numIp)]
ipRange = [i for i in range(0, numIp)]

numFail = 0
numSucess = 0
numRead = 0
startTime = time.clock()
arnetEntry = 1
nline = skipLine 
while(arnetEntry):    
    ###---- Skip lines ----
    print 'the nline is %d' % nline
    print 'The number of arnet paper is %d' % numRead
    print 'The number of sucess is %d' % numSucess

    ##    #--- Reach the 5 times error ---
    if numFail > 5:
        print 'The next skipLine should be %d' % nline
        break
    # -----------------------------------
    
    arnetEntry, nline = arnet.ReadNewBib()
    numRead = numRead + 1

    # Search a new paper
    random.shuffle(ipRange)
    ipN = 0
    for ii in ipRange:
        ipN = ipN + 1
        print 'The %d-th ip :%s' % (ipN, ip[ii])
        if not ipValid[ii]:
            print 'coninue'
            continue
        entry = api.searchTitle(arnetEntry['title'], False, ip[ii])
        if entry:
            break
        ipValid[ii] = ipValid[ii]-1
    
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
    

    if re.search('\.\Z', arnetEntry['title']):
        arnetEntry['title'] = arnetEntry['title'][:-1] # delete the end of .
    if re.search('\.\Z', entry['title']):
        entry['title'] = entry['title'][:-1] # delete the end of .
    
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

  
fileOutput.close()
endTime = time.clock()
print "The time of ececute is %f" % (endTime-startTime)
print 'The start line: %d, the end line: %d' % (skipLine, nline)
print 'The number of arnet paper is %d' % numRead
print 'The number of sucess is %d' % numSucess

        

        

        

        
    
    





    
    
