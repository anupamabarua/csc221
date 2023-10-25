"""
  >>> type(thing1)
  <class 'list'>
  >>> type(thing2)
  <class 'tuple'>
  >>> type(thing3)
  <class 'str'>
"""
thing1=[1,2]
thing2=1,2,3
thing3="1,2,3,4"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
