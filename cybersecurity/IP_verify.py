#to verify external IP adress

import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

open = urlopen(url) #open url and store data

data = json.load(open) #upload json file from url

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('Data from external IP\n')
print('IP: {4}\n Region: {1}\nCountry: {2}\nCity: {3}\nOrg: {0}'.format(org, region, country,city,ip))


