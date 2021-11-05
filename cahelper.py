#!/usr/bin/env python3
import os

def genkey(name, usage):
    print("Generating " + usage + " key...")
    os.system("openssl genpkey -algorithm RSA -out " + name + " -outform PEM -pkeyopt rsa_keygen_bits:2048")
    return True

genkey("root.key", "Root")
days = input("Root CA valid period: ")
os.system("openssl req -x509 -new -nodes -sha256 -days " + str(days) + " -key root.key -out root.crt")
print("\n\n\n")
genkey("org.key", "Issuer")
days = input("Issuer CA valid period: ")
os.system("openssl req -new -key org.key -out org.csr")
with open("org.ext", 'w') as f:
    f.write("basicConstraints=CA:TRUE")
os.system("openssl x509 -req -in org.csr -CA root.crt -CAkey root.key -CAcreateserial -out org.crt -days " + str(days) + " -sha256 -extfile org.ext")
print("Please enter your 'issued to'(AKA. server domain/ip) in 'common name'")
print("Press enter to continue.")
pmpt = input("")
genkey("server", "Server")
days = input("Server CA valid period: ")
os.system("openssl req -new -key server.key -out server.csr")
os.system("openssl x509 -req -in server.csr -CA org.crt -CAkey org.key -CAcreateserial -out server.crt -days " + str(days) + " -sha256")
print("\n\n\n")
print("That's it!")
print("root.key/csr/crt is Root CA")
print("org.key/csr/crt is Issuer CA")
print("server.key/csr/crt is Server CA!")
