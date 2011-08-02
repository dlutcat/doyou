#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from doyou import app

def clear_pyc():
  '''
  Remove .pyc files
  '''

  print '>>>>> remove .pyc files...'
  for root, dirs, files in os.walk(os.path.dirname(__file__)):
    for fname in files:
      if os.path.spliext(fname) == '.pyc':
        del_file = os.path.join(root,fname)
        os.remove(del_file)
        print '>>>>> %s deleted.' % del_file
        
if __name__ == '__main__':
  clear_pyc()
  app.run(debug=True, host='0.0.0.0')
