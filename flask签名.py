import hmac,hashlib,base64
def a(b):
    return base64.urlsafe_b64encode(b).decode().rstrip('=')
k = b"EasyMeme2026!"
# k=input().encode()
m = b"eyJhZG1pbiI6dHJ1ZSwidXNlciI6IjEyMyJ9.awFfwA"
# m==input().encode()
raw = hmac.new(k, b'cookie-session', hashlib.sha1).digest()
raw=hmac.new(raw,m,hashlib.sha1).digest()
sig = a(raw)
print(sig)