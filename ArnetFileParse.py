# Parse the Arnet file
# Author : ls
# Create : 10/26,2013
# Revised: 12/31,2013

import re

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


class Arnet:
    def __init__(self, fileName, nLine = 0):
        self.fileArent = open(fileName)
        self.bLine = True
        self.nLine = 0
        while(self.nLine < nLine and self.bLine):
            self.bLine, line = self.ReadNewLine()
            self.nLine = self.nLine + 1
            
        

    def ReadNewLine(self):
        line = self.fileArent.readline()
        bLine = True
        if not line:
            bLine = False
        return bLine, line

    def SeekBibType(self, line):
        funType = ['SeekTitle','SeekAuthors', 'SeekYear', 'SeekConf',\
               'SeekCitation', 'SeekIndex', 'SeekArnetID', 'SeekRefs', 'SeekAbstract']# should be full (Careful!!!)

        if line.isspace():
            bibType = []
            match = False
        else:
            for n in range(9):
                bibType, match = getattr(Seeks(), funType[n])(line)
                if match:
                    break

        return bibType, match

    def ReadNewBib(self): 
        arnetEntry = {}
        while self.bLine:
            bLine, line = self.ReadNewLine()
            self.nLine = self.nLine +1
            bibType, mType = self.SeekBibType(line)

            self.bLine = bLine
            if mType and bibType == 'title':
                # get a new entry
                arnetEntry['title'] = line[mType.end():-1]

                while bLine:
                    bLine, line = self.ReadNewLine()
                    self.nLine = self.nLine +1
                    # Judge the null string
                    if not (bLine and line.strip()):
                        break
                    bibType, mType = self.SeekBibType(line)
                    if not mType: # break if meet the blank(Careful!!!),
                        continue

                    if bibType == 'ref':
                        arnetEntry.setdefault('ref', [])
                        arnetEntry['ref'].append(line[mType.end():-1])
                    else:
                        arnetEntry[bibType] = line[mType.end():-1]

                # break the while self.bLine:
                break
                

        self.bLine = bLine
        return arnetEntry, self.nLine
            
            
        

    


    
        

    
