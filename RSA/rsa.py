# -*- coding: utf-8 -*-
"""RSA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13OQCouigB4P_ZKaKeB4v_Yx9nMEoMtAt
"""

import math
 
 
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)
 
while (e < phi):
 
    # e debe ser co-prime a phi y
    # mas pequeño que phi.
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
print(e)
# Private key (d para desencriptar)
# escoje d tal que satisfaga
# d*e = 1 + k * phi
 
k = 2
d = (1 + (k*phi))/e
print(d)
# Mensaje a encriptar
msg = 12.0

print("Mensaje = ", msg)
 
# Encriptar c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("Mensaje encriptado = ", c)
 
# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Mensaje original desencriptado = ", m)