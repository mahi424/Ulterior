from PIL import Image
import io
phone_img = Image.open("airplane.png")
# f=open('testdata.txt','r')
f=open('data.txt','r')
# image_data = f.read()
# f2=open('data2.txt','w')
# f2.write(image_data)
# import binascii
# from simplecrypt import encrypt, decrypt
# import easygui
# path=easygui.fileopenbox();
# print path;
# f=open(path,'r+');
f2=open('hexM.txt','r')
f3=open('res.txt','w')
k='';
s=''
i=1;
j=0;
# for j in range(0,49152):
# 	l=f.readline();
# 	# l = l.rstrip("\n\r")
# 	f3.write(l)
	# f3.write('\n');


l=f.readline();
while l:
	# l = l.rstrip("\n\r")
	# print l
	i=1
	temp=""
	for  c in l:
		if i%5==4:
			
			x=f2.read(1);
			j=j+1
			# print i
			# x='k';
			if not x:
				temp=temp+c;
				# j=j+1

				# break
				# temp=temp+' ';
			else:
				if str(x).isalnum():
					# print 'hi'
					temp=temp+x
				elif x==' ':
					x=f2.read(1);
					temp=temp+x
				elif x=='\r':
					# f2.read(1);
					# f2.read(1);
					x=f2.read(1);
					temp=temp+x
				else:
					f2.read(2);
					x=f2.read(1);
					temp=temp+x
		else:
			temp=temp+c;
			# temp=temp+' ';
		i=i+1;
	f3.write(temp)
	# f3.write('\r');
	l=f.readline();
f3.close()
# print j

# pi=open('res.txt','r')
# data=pi.read()
# # phone_img1 = Image.frombytes(phone_img.mode,phone_img.size, phone_img.tobytes())
# phone_img1 = Image.frombytes(phone_img.mode,phone_img.size, data)
# phone_img1.save("my.png","PNG")
# pi.close()

# l=f.readline();

# l = l.rstrip("\n\r")
# print l


# while True:
#     c = f.read(1)
#     if ( i%5==4):
#     	j=j+1
#     	n=f2.read(1)
#     	if (j%40==0):
#     		f2.read(1)

#     	# print n
#     	if not n:
#     		f3.write(c)
#     	else:
#     		if str(n).isalnum():
#     			f3.write(n)
#     		# if n==' ' or n=='\n':
#     		if n==' ':

#     		# 	# f3.write(f.read(1))
#     		# 	f3.write('z')
#     		# else:
#     			f3.write(f2.read(1))
#     			j=j+1
#     			if (j%40==0):
#     				f2.read(1)
#     		# if n=='EOL':
#     		# 	print 'eol'
#     		# else:
#     		# 	f3.write(n)
#     		# f3.write(n)

#     else:
#     	f3.write(c)
#     	# print c

#     if not c:
#       # print "End of file"
#       break
#     i=i+1
f.close();
f2.close();
# f3.close();
