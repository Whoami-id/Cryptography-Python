import rsa

with open("sample.txt", "rb") as f:
    pdf = f.read()


with open("private_key_file.pem", "rb") as pr:
    private_key = rsa.PrivateKey.load_pkcs1(pr.read())


signature_file = rsa.sign(pdf, private_key, "SHA-1")

print(len(signature_file))

with open("signature_file", 'wb') as sf:
    sf.write(signature_file)

