import hashlib

def encrypt(initial):
    """ Use : encrypt("message")
=> '78e731027d8fd50ed642340b7c9a63b3'
  """
  initial = initial.encode('utf-8')
  output = hashlib.md5(initial.encode())
  return output.hexdigest()
