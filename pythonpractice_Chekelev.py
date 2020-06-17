import zipfile 
import time 
import os 

way = 'C://Program Files (x86)/Python1'
os.chdir(way)

file_list = os.listdir(way)

purpose = 'C://Program Files (x86)/Python2'

KOMENT = input('Comment: ')
if len(KOMENT) == 0:
    filename = purpose + time.strftime('%Y%m%d') + '.zip'
else:
    filename = purpose + KOMENT.capitalize() + time.strftime('%Y%m%d') + '.zip'

created_zip = zipfile.ZipFile(filename, 'w')

for i in file_list:
    created_zip.write(i)

created_zip.close()