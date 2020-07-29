# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# CallOtherPythonFiles_logErrors.py
# Created on: 9/30/2016
#   (generated by micahwilli)
#  A work of Cloudpoint Geographics Inc. 
# Description: this runs and kicks off Multiple Python Scripts within the SAME folder
# if a particular scripr errors out, and exception is raised and Error Logged
# then the script exits there. All Pythong Scripts need to be in the same folder
# the log text file is created in the same folder
# ---------------------------------------------------------------------------

import sys
import os
import logging

##NOTE## Just use the Names of the script not the ".py" extension!
try:
    import test1 #first Python file here that ou run
except Exception as e:
    f = open('log.txt', 'w')
    f.write('An Error fpr test 1 Was logged - %s' % e)
    f.close() 
    sys.exit(0)
try:
    import test2 #Next Python file here
except Exception as e:
    f = open('log.txt', 'w')
    f.write('An Error for test2 Was logged - %s' % e)
    f.close()
    sys.exit(0)
	
try:
    import test3 #Third Python file here
except Exception as e:
    f = open('log.txt', 'w')
    f.write('An Error for test3 Was logged - %s' % e)
    f.close()
    sys.exit(0)

#Successful Log Entry	
f = open('log.txt', 'w')
f.write('The Whole Update Process worked well and finished')
f.close()
