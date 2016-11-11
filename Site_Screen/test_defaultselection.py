import unittest
from Utils.logger import *
from selenium import webdriver

from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *

############################ CHECK FOR THE DEFAULT SELECTION BY MULTIPLE MEASURES #######################

# Getting Setup Details and Launching the application
setup = SetUp()

# Logging into the appliction
login(setup, "admin", "Admin@123")

# Launch Site Screen
launchPage(setup,"site_Screen")
sleep(5)

# Get the Instance of the screen
screenInstance = SitePageClass(setup.d)

# Get the handles of the screen
siteScreenHandle = getHandle(setup,"site_Screen")

# Get the default selection
defSelection = screenInstance.btv.getSelection(siteScreenHandle)


# Validating the result
checkEqualAssert(str(1),str(defSelection['selIndex']))

# Set the bar Table view to the 2 index
screenInstance.btv.setSelection(2,siteScreenHandle)


#Changing the measure
setMeasure(setup,"Bitrate_downlink_absolute_average","site_Screen")

# Get the new handles of the screen
handles = getHandle(setup,Constants.SITES) # Everytime we need to get handles when the btv is redrawing

# Get the selection after changing the measures
changeselection =  screenInstance.btv.getSelection(handles)


# Validating the result after changing the measure
checkEqualAssert(str(1),str(changeselection['selIndex']))


# Logging out of the application
setup.d.close()


