# Use urllib to read the HTML from the data files below
# extract the href= vaues from the anchor tags
# scan for a tag that is in a particular position from the top and follow that link
# repeat the process a number of times
# report the last name you find.
#
# Sample code http://www.pythonlearn.com/code/urllinks.py
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
#
# Two files were provided for this assignment.
# One sample file and one actual data to process for the assignment
# Sample data URL https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). 
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Answer: Anayah
#
# Actual data https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Nevada.html
# Find the link at position 18 (the first name is 1). 
# Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Answer: Sylvanna

import urllib
from BeautifulSoup import *

count_pos      = 0  #User input
count_pos_real = 0  #Adjusted line position
count_process  = 0  #Number of times to repeat

# User inputs
url = raw_input('Enter URL: ')
count_process_raw = raw_input('Enter count:    ')
count_pos_raw     = raw_input('Enter position: ')
count_process     = int(count_process_raw)      #convert to integer
count_pos         = int(count_pos_raw)
count_pos_real    = count_pos - 1               #array element starts at 0.  Third pos = 2.
#url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
#url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Nevada.html'

while count_process > 0:
    print 'count_process = ', count_process
    print 'Retrieving: ', url
    count_process -= 1
    
# Soup it
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
    tags = soup('a')                 # Get all lines with <a> into "tags"
    url_tag = tags[count_pos_real]   # 3rd tag.
    url_new = url_tag.get('href', None)   #Extract new URL from 3rd tag.
    url     = url_new
    #print 'tags1 = ', tags[0]
    #print 'tags2 = ', tags[1]
    #print 'tags3 = ', tags[2]
    #print 'tags4 = ', tags[3]
    #print 'url_tag   = ', url_tag
    #print 'url_new   = ', url_new
    #print 'content 3 = ', url_tag.contents[0] #name (content of URL)
    
print 'Final name = ', url_tag.contents[0]
