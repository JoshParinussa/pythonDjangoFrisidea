Note: Install sudo apt install httpie (curl work as well)

# Register
http post http://127.0.0.1:8000/v1/users username=jopa password=pindai123 email=jopa@mail.com

# Request token before login
http post http://127.0.0.1:8000/v1/api-token-auth/ username=jopa password=pindai123

# Login
http http://127.0.0.1:8000/v1/auth/login 'Authorization: Token 99a2d119871cfdc1cfdb5bc282d079f9c6d50e70'