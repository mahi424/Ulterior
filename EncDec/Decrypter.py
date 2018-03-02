from simplecrypt import encrypt, decrypt
import easygui
path=easygui.fileopenbox();
# print path;
f=open(path,'r+');
# name = raw_input("Enter your name: ");
# f.write(name);
c=f.read();
p = raw_input("Enter your password: ");
# ciphertext = encrypt(p, c)
plaintext = decrypt(p, c)
print plaintext;
