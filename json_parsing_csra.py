# The program will prompt for a URL
# Read the JSON data from that URL using urllib
# Parse and extract the comment counts from the JSON data
# Compute the sum of the numbers in the file and enter the sum below:

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_215253.json (Sum ends with 94)

import urllib
import json

item_count_name = 0
item_count_sum  = 0

# User Input
url = raw_input('Enter location: ')
#url = 'http://python-data.dr-chuck.net/comments_42.json'

print 'Retrieving', url
url_object = urllib.urlopen(url)
data       = url_object.read()
data_dict  = json.loads(str(data))

#print data
print 'Retrieved', len(data), 'characters'
#print 'Dump data_dict:'
#print json.dumps(data_dict, indent=4) #pretty print with indentation


for item in data_dict['comments']:  
    item_count = item["count"]
    item_name  = item["name"]
    item_count_sum = item_count_sum + item_count
    item_count_name= item_count_name + 1
    #print 'Count: ', item_count
    #print 'Name:  ', item_name
    #print 'Running name count: ', item_count_name
    #print 'Running sum: ', item_count_sum

print 'Count: ', item_count_name
print 'Sum: ', item_count_sum

# Output
# Count: 50
# Sum: 2294
