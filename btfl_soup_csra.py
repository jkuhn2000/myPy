# Scraping Numbers from HTML using BeautifulSoup
# Use urllib to read the HTML from the data files below
# Parse the data and find all the <span> tags in the file
# Extract the numbers from the tag
# Compute the sum of the numbers.

# http://www.pythonlearn.com/code/urllink2.py (sample code)

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# Use data http://python-data.dr-chuck.net/comments_215252.html
# tag is an object

# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_215252.html (Sum ends with 64)

import urllib
from BeautifulSoup import *

tag_count = 0
tag_sum   = 0
url  = raw_input('Enter URL - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')                         #find all the "span" tags
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    num_str_found = tag.contents[0]         #extract the number from the tag
    num_true      = int(num_str_found)      #convert it to an integer
    # print 'num_str_found', num_str_found
    print 'num_true: ', num_true
    # print 'URL:',tag.get('href', None)
    # print 'Contents:',tag.contents[0]
    # print 'Attrs:',tag.attrs
    tag_count = tag_count + 1
    tag_sum   = tag_sum + num_true
    print 'Tag sum   = ', tag_sum
    print '---------------'

print 'Tag count = ', tag_count
print 'Tag sum   = ', tag_sum

# Output
#---------------
#TAG: <span class="comments">3</span>
#num_true:  3
#Tag sum   =  2362
#---------------
#TAG: <span class="comments">2</span>
#num_true:  2
#Tag sum   =  2364
#---------------
#Tag count =  50
#Tag sum   =  2364

#Data Format

#The file is a table of names and comment counts. You can ignore most of the data in the #file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

#You need to adjust this code to look for span tags and pull out the text content of the span #tag, convert them to integers and add them up to complete the assignment.

#Sample Execution

#$ python solution.py 
#Enter - http://python-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2482

