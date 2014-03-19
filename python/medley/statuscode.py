import requests


url = 'http://www.duffnerengineering.com/'
r = requests.get(url, allow_redirects=False)
print r.status_code
print r.url
