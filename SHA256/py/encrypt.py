import hashlib

def encrypt(initial) :
    """ Use : encrypt("message")
=> 'ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d'
  """
  initial = initial.encode('utf-8')
  output = hashlib.sha256(initial.encode())
  return output.hexdigest()
