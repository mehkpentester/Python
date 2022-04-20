from fileinput import filename

from urllib.request import urlretrieve

link=input('Image download link: ') #This is you want to download photo's link.

filename=input('File Name : ') # This is downloaded photo to set file name.

urlretrieve(link,'image/' +filename+'.jpg')
