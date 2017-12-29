import hashlib

def encrypt(initial):
    """ Use : encrypt("message")
=> 'ff51ddfabb180148583ba6ac23483acd2d049e7c4fdba6a891419320'
  """
  initial = initial.encode('utf-8')
  output = hashlib.sha224(initial.encode())
  return output.hexdigest()
