openssl req -x509 -newkey rsa:2048 -keyout my_private_key.pem -out my_cert.pem -days 355 -nodes
openssl x509 -outform der -in my_cert.pem -out my_cert.der


openssl req -x509 -newkey rsa:2048 -keyout user01_private.pem -out user01_cert.pem -days 355 -nodes
openssl x509 -outform der -in user01_cert.pem -out user01_cert.der

