import cv2

src='images/tmp_lion/img'
dest='images/lion/img'
c=0
for i in range(597):
	img=cv2.imread(src+str(i))
	print("saving..",i)
	cv2.imwrite(dest+str(i)+'.jpeg',img)
cv2.destroyAllWindows()