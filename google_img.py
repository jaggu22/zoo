import requests
import re
import bs4


host='https://www.google.com'
url='/search?biw=1301&bih=672&tbm=isch&sa=1&ei=a00wXIWcF8vgrQHktIXYCQ&q=lion+zoo&oq=lion+zoo&gs_l=img.3..0l8j0i5i30l2.5352.7792..8273...0.0..0.224.588.1j2j1......1....1..gws-wiz-img.......35i39j0i67.9LiN7BWSAes#imgrc=cnb62Hlh5aYVaM:'
title='images/tmp_lion/img'
count=0
while True:
	pg=requests.get(host+url)
	soup=bs4.BeautifulSoup(pg.content,'html.parser')
	imgs=soup.find_all('img')#,{'class':'rg_ic'})
	for img_tag in imgs:
		print("Reading image")
		img=requests.get(img_tag['src'])
		with open(title+str(count),'wb') as f:
			for chunk in img:
				f.write(chunk)
		count+=1
	lnks=soup.find('table',id='nav').find_all('a')
	print(re.sub('<.*?>','',str(lnks[-1])))
	if(re.sub('<.*?>','',str(lnks[-1]))!='Next'):
		break
	url=lnks[-1]['href']

print(count)
print("destroying windows")
cv2.destroyAllWindows()