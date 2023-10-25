"""
  >>> whatsthis[2]
  42
  >>> type(whatsthis[4])
  <class 'list'>
  >>> whatsthis[6:8]
  [11, 'what is this?']
  >>> len(whatsthis)
  10
"""
whatsthis = ["hi", 0.4, 42, 0.45454,  [], True,  11, 'what is this?', "c", 134]



if __name__ == "__main__":
    import doctest
    doctest.testmod()

