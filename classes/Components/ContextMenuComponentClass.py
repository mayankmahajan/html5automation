#!/usr/bin/env python
##############################################################
'''
CM Component Handler
'''
__author__      = "Mayank Mahajan"
__email__       = 'mayank.mahajan@guavus.com'
__version__     = "1.0"
__maintainer__  = "Mayank Mahajan"
##############################################################


from BaseComponentClass import BaseComponentClass
from classes.DriverHelpers.locators import *
from Utils.Constants import *
class ContextMenuComponentClass(BaseComponentClass):

    def activateContextMenuOptions(self,handle):
        handle[Constants.CONTEXTMENU][0].click()
        # self.handle.
    def drillTo(self,driver,driverHelper,handles,pageName):
        try:
            if pageName == Constants.NETWORKFUNCTIONS:
                handles[Constants.DRILLTONF][0].click()
            elif pageName == Constants.SITEINTERACTIONS:
                handles[Constants.DRILLTOSITEINTERACTION][0].click()
            elif pageName == Constants.SITES:
                handles[Constants.DRILLTOSITE][0].click()
            elif pageName == Constants.VRF:
                handles[Constants.DRILLTOVRF][0].click()
            elif pageName == Constants.DRILLTO:
                handles[Constants.DRILLTO][0].click()
            return True
        except Exception:
            return Exception
