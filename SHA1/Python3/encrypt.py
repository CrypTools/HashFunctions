import hashlib

def encrypt(initial):
    """ Use : encrypt("message")
=> '6f9b9af3cd6e8b8a73c2cdced37fe9f59226e27d'
    """
  initial = initial.encode('utf-8')
  output = hashlib.sha1(initial.encode())
  return output.hexdigest()
