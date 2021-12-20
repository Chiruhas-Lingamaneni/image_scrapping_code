import requests 
from bs4 import BeautifulSoup 

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://expressexpense.com/view-receipts.php") 
soup = BeautifulSoup(htmldata, 'html.parser') 
n=1
for item in soup.find_all('img')[1:]:
    print(item['src'])
    with open('images/image_'+str(n)+'.jpg','wb') as f:
       im=requests.get('https://expressexpense.com/'+item['src'])
       print('**************')
       print('https://expressexpense.com/'+item['src'])
       f.write(im.content)
    n+=1
