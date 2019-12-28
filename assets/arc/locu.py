# #!/usr/bin/env python
# #Learn how this works here: http://youtu.be/pxofwuWTs7c
 
# import urllib2
# import json
 
# locu_api = 'YOUR KEY HERE'
 
# def locu_search(query):
#     api_key = locu_api
#     url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
#     locality = query.replace(' ', '%20')
#     final_url = url + "&locality=" + locality + "&category=restaurant"
#     json_obj = urllib2.urlopen(final_url)
#     data = json.load(json_obj)
   
#     for item in data['objects']:
#         print item['name'], item['phone']



# #A NOTE FOR PEOPLE USING PYTHON 3.5:

# #import urllib.request

# #you would have to use 
# #urllib.request.urlopen(url).read() 

# #instead of urllib2.urlopen(url)

# #and you would have to convert it into a string like so

# #response = urllib.request.urlopen(url).read()

# #json_obj = str(response, 'utf-8')

# #then use json.loads instead of json.load. load did not work for me.

# #data = json.loads(json_obj)