#Extracting Data from XML

# Example: http://www.pythonlearn.com/code/geoxml.py. 
# Prompt for a URL
# Read the XML data from that URL using urllib
# Parse and extract the comment counts from the XML data
# Compute the sum of the numbers in the file.

import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
#url = 'http://python-data.dr-chuck.net/comments_215249.xml'

item_count_int = 0
item_count_sum = 0

# User Input
url = raw_input('Enter location: ')

print 'Retrieving', url
url_object = urllib.urlopen(url)
data = url_object.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
print tree

tree_list = tree.findall('comments/comment')
# tree_list  = tree.findall ('.//comment')  # alternate. not tested.

print 'User count:', len(tree_list)

for item in tree_list:
    item_name      = item.find('name').text
    item_count     = item.find('count').text
    item_count_int = int(item_count)
    item_count_sum = item_count_sum + item_count_int
    
    #print 'Name:  ', item_name
    #print 'Count: ', item_count_int
    #print 'Running sum: ', item_count_sum
    
print 'Sum: ', item_count_sum

# Output
# Enter location: http://python-data.dr-chuck.net/comments_215249.xml
# Retrieving http://python-data.dr-chuck.net/comments_215249.xml
# Retrieved 424199 characters
# Count: 50
# Sum: 2482
