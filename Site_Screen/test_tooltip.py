import unittest
from Utils.logger import *
from selenium import webdriver

from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *
from classes.Components.BTVComponentClass import *


#### NOT RUNNING DUE TO BUG

############################## TESTING FOR THE TOOLTIP #####################
data = {}
# Getting Setup Details and Launching the application
setup = SetUp()

# Logging into the appliction
login(setup, "admin", "Admin@123")

# Launch Site Screen
launchPage(setup,"site_Screen")
sleep(5)

# Get the Instance of the screen
screenInstance = SitePageClass(setup.d)


setMeasure(setup,"Bitrate_downlink_absolute_peak","site_Screen")

# Get the handles of the screen
siteScreenHandle = getHandle(setup,"site_Screen")

btvData = screenInstance.btv.getData(siteScreenHandle)
data['btvData'] = {}
for key,value in btvData.iteritems():
    pv = value.pop(0)
    if len(data['btvData']) == 0:
        data['btvData']['dimension'] = value
    else:
        data['btvData']['value'] = value
    logger.debug('Col1 : %s  and Col2 : %s',key,value)
data['btvTooltipData'] = screenInstance.btv.getToolTipInfo(setup.d,setup.dH,siteScreenHandle)
for i in range(0,len(data['btvTooltipData'])):
    logger.debug('Tooltip %s : %s ',i,data['btvTooltipData'][i])

result1 = screenInstance.btv.validateToolTipData(data)
for key,value in result1.iteritems():
    logger.debug('DIMENSION : %s  and RESULT : %s',key,value)
#screenInstance.btv.launchToolTip(setup,setup.d,setup.dH,siteScreenHandle)
#screenInstance.btv.getToolTipInfo(setup.d,setup.dH,siteScreenHandle)

# screenInstance.btv.validateToolTipData(btvdata,btvtooltipdata)



#checkEqualAssert("true","true")
# Logging out of the application
setup.d.close()
