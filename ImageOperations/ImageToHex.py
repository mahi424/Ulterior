from PIL import Image
import io

# phone_img = Image.open("airplane.png")

# pi=open("pi.txt","w+")
# pi.write(phone_img.tobytes())
# pi.close()

# pi=open("pi.txt","r")
# data=pi.read()
# # phone_img1 = Image.frombytes(phone_img.mode,phone_img.size, phone_img.tobytes())
# phone_img1 = Image.frombytes(phone_img.mode,phone_img.size, data)
# phone_img1.save("my.png","PNG")
# pi.close()

# fid = open('data.txt','r');
# data = fid.read()
# fid.close()
# fid = open('test.jpg','wb');
# fid.write(data);
# fid.close()


im=Image.open('airplane.png')
# im.show()
# im.tobytes()
f=open('data.txt','w')
f.write(im.tobytes('raw'))
f.close()
# f2=open('res.txt','r')
# photo_data =f2.read()
# f3=open('qq.txt','w')
# f3.write(photo_data)
# photo_infile = io.StringIO(photo_data)
# photo_image = PIL.Image.frombytes(photo_infile)
# photo_image.show()



# from PIL import Image
# import io
# f=open('data.txt','r')
# image_data = f.read()
# f2=open('data2.txt','w')
# f2.write(image_data)
# image = Image.open(io.BytesIO(image_data))
# image.show()