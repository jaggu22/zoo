import os
import glob
annotations='annotations/lion'
file_lst=glob.glob(annotations+'/*.xml')
nm_lst=sorted([file_pth.split('.')[0].split('/')[-1] for file_pth in file_lst])

for img_pth in glob.glob('images/lion/*.jpeg'):
	nm=img_pth.split('.')[0].split('/')[-1]
	if(nm not in nm_lst):
		print(nm)
