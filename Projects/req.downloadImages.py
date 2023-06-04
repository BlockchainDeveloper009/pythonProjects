import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
   #type(res)
#    <class 'requests.models.Response'>
res.status_code == requests.codes.ok
print(len(res.text))
print(res.text[:250])
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()