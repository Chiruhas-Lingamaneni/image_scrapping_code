import requests 
from bs4 import BeautifulSoup 
count=1
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
for x in range(1,161):
    weblink='https://expressexpense.com/view-receipts.php?page='+str(x)
    htmldata=getdata(weblink)
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img')[1:]:
        with open('images/image_'+str(count)+'.jpg','wb') as f:
            im=requests.get('https://expressexpense.com/'+item['src'])
            print('https://expressexpense.com/'+item['src'])
            f.write(im.content)
