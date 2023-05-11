from hashlib import sha256

hash_1 = sha256()
hash_2 = sha256()

with open('image_1.bmp', 'rb') as file:
    image_1 = file.read()

with open('image_2.bmp', 'rb') as file:
    image_2 = file.read()

hash_1.update(image_1)
hash_2.update(image_2)
print(
    hash_1.hexdigest(),
    hash_2.hexdigest(),
    sep='\n\n'
)
