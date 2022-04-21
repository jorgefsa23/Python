import hashlib

string = input("Input a text to generate HASH:")


menu = int(input('''***** CHOOSE THE KIND OF HASH ****
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            Type your HASH number:'''))

if menu ==1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('The MD5 HASH for the string is: ', resultado.hexdigest())
elif menu ==2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('The SHA1 HASH for the string is: ', resultado.hexdigest())
elif menu ==3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('The SHA256 HASH for the string is: ', resultado.hexdigest())
elif menu==4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('The SHA512 HASH for the string is: ', resultado.hexdigest())
else:
    print("Invalid option!!! Try again")

