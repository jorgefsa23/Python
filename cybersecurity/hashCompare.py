import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

#generating Hash by ripemd160 and reading
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The file: {arquivo1} content is different to file: {arquivo2}')
else:
    print(f'The file: {arquivo1} content is equal to file: {arquivo2}')

print(f'The HASH to file {arquivo1} is: ', hash1.hexdigest())
print(f'The HASH to file {arquivo2} is: ', hash2.hexdigest())
