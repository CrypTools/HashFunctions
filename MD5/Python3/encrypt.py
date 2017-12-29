import hashlib

def encrypt(initial):
  initial = initial.encode('utf-8')
  output = hashlib.md5(initial.encode())
  return output.hexdigest()
