import evt_ecc

#get a pair of key
public_key,private_key=evt_ecc.evt_generate_new_pair()
#print public_key
print(public_key)
#print evt_private_key
print(private_key)
#get the public_key from private_key
print(private_key.evt_get_public_key())
#construct the public_key from string
public_key2=evt_ecc.evt_public_key(public_key.evt_public_key_string())
#print the public key2 it should be as the same as the public key1
print(public_key2)
#construct the private_key from string
private_key2=evt_ecc.evt_private_key(private_key.evt_private_key_string())
#print the private key2 it should be as the same as the private key1
print(private_key2)

#create a hash here
hash=evt_ecc.evt_hash("hello world")
#make a signature
sign=evt_ecc.evt_sign_hash(private_key,hash)
#recover the public key
public_key3=evt_ecc.evt_recover(sign,hash)
print(public_key3)

#make a error exception example
try:
    pk=evt_ecc.evt_private_key("12345")
except Exception as e:
    print("here catch an exception")
    print(e)
