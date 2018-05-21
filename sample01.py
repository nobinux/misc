import hashlib

print('input Data :')
_input_string = input()

print('Data D : ' + str(_input_string))

print('sha1(D) : ' + hashlib.sha1(
    str(_input_string).encode()).hexdigest())

sha256_digest = hashlib.sha256(str(_input_string).encode()).hexdigest()
print('sha256(D) : ' + sha256_digest)

print('sha512(D) : ' + hashlib.sha512(
    str(_input_string).encode()).hexdigest())

print('sha256(sha256(D)) : ' + hashlib.sha256(
    bytes.fromhex(sha256_digest)).hexdigest())

ripemd160_digest = hashlib.new('ripemd160')
ripemd160_digest.update(str(_input_string).encode())
print('ripemd160(D) : ' + ripemd160_digest.hexdigest())

ripemd160_digest.update(bytes.fromhex(sha256_digest))
print('ripemd160(sha256(D)) : ' + ripemd160_digest.hexdigest())
