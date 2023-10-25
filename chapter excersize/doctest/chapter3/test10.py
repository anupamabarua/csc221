
"""
  >>> type(thing)
  <class 'list'>
  >>> type(thing[3])
  <class 'tuple'>
  >>> type(thing[0])
  <class 'str'>
  >>> type(thing[2])
  <class 'list'>
  >>> len(thing)
  4
  >>> 8 in thing
  True
"""
thing=["s",8,[2,3],(1,2)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
