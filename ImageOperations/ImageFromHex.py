from PIL import Image
import io
from shutil import copyfile
im = Image.open("airplane.png")

# copyfile('data.txt','new.txt')
# f=open('new.txt','w')



# f=open('data.txt','w')
# f.write(im.tobytes('raw'))
# f.close()
# pi=open('data.txt','r')
# pi=open('res.txt','r')
# pi=open('testdata.txt','r')
# pi=open('new.txt','w')
# res=open('res.txt','r')
pi=open('dataCopied','r')
# for line in res.readlines():
# 	pi.write(line)
# res.close()
# pi.close()
# xxx=res.read()
# pi.write(xxx)
# pi.close()

# pi=open('new.txt','r')
data=pi.read()
# im1 = Image.frombytes(im.mode,im.size, im.tobytes())
im1 = Image.frombytes(im.mode,im.size, data)
im1.save("my.png","PNG")

# res.close()
pi.close()

