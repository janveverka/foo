# -*- coding: utf-8 -*-
'''
The purpose of this module is to figure out the full path name to the
file containing it and pring it.  It should work both when it runs as a main and
when it is imported.  It should work independent from the current directory
of the caller.
'''

import os
print __file__
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))