import requests
import cv2

label=title+str(1)

path='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIfZ7-e0Tf2WqVixhKm8ezrRFZKudzZE67E63ARKrYDhUEfKpI-A'
print("opening",label,"url")
img=requests.get(path)
print("coping  to 'image' file")
with open('image','wb') as f:
	for chunk in img:
		f.write(chunk)

print("reading  to cv2")
img=cv2.imread('image')
print("showing",label)
cv2.imshow('image',img)
if cv2.waitKey() & 0xff == ord('s'):
	print("saving",label)
	cv2.imwrite(label+".jpeg",img)
print("destroying windows")
cv2.destroyAllWindows()
