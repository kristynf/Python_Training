import urllib2
file = urllib2.urlopen('http://dl.thehellings.com/sword-release-procedures.txt')
message = file.read()
print message
                       
