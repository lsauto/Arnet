# Prase The IP form the txt
# Author : ls
# Create : 12/22,2013
# Revised: 12/22,2013

import re

def PraseTxtIP(txtName):

    ip = []
    numIp = 0
    ipRule = re.compile(r'\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}:\d{2,4}')
    fileTxt = open(txtName)
    for line in fileTxt:
        mm = ipRule.match(line)
        if mm:
            ip.append(mm.group())
            numIp = numIp +1
    print 'The number of IP is %d' % numIp
    return ip, numIp
        
    
