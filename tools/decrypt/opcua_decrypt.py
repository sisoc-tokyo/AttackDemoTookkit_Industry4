from opcua.crypto import security_policies, uacrypto
from scapy.all import *

pk = uacrypto.load_private_key('my_private_key.pem')
dcry = security_policies.DecryptorRsa(pk, uacrypto.decrypt_rsa_oaep, 42)
cl_dec_rsa = security_policies.DecryptorRsa(pk, uacrypto.decrypt_rsa15, 11)


p = rdpcap('gam.pcapng')
f=p.res

for n in range(len(f)-2):
        try:
            target = f[n].original+f[n+1].original+f[n+2].original
            enc = target[-512:]
            print('-----------')
            x = dcry.decrypt(enc)
            print(enc)
            print(x)
            print('+++++++++++')
            print(x.decode())
        except ValueError as e:
            print(e)
        except TypeError:
            print('typeerror')

