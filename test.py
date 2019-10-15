#Caden Davenport
#cdavenport@ozarkorthopaedic.com
#Updates NPI Forms in Athenanet using Python
import requests
import json

npiNum = input('Enter the NPI Number: ')

payload = {'version': '2.0', 'number': npiNum, 'enumeration_type': 'NPI-1', 'pretty': 'on'}

npiData = requests.get("https://npiregistry.cms.hhs.gov/api/?version=2.0", params = payload)

f = open('reqOutput.json', 'w')
print(npiData.json(), file = f)
print(npiData.status_code, file = f)
f.close()