import unittest
from Utils.logger import *
from selenium import webdriver

from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *

# Getting Setup Details and Launching the application
setup = SetUp()

# Logging into the appliction
login(setup, "admin", "Admin@123")

# Launch Site Screen
launchPage(setup,"site_Screen")


# Get the Instance of the screen
screenInstance = SitePageClass(setup.d)

# Get the handles of the screen
siteScreenHandle = getHandle(setup,"site_Screen")

# Set the Index value at 2
screenInstance.btv.setSelection(2,siteScreenHandle)

# Checking drill to the Site Interaction Screen
drilltoScreen(setup.d,setup.dH,Constants.SITEINTERACTIONS)

#Get the screen instance of the site interaction screen
screenInstance = SitePageClass(setup.d)

# Get the handles of the screen
siteScreenHandle = getHandle(setup,Constants.SITEINTERACTIONS)

# CHECKING THE DRILL TO FUNCTION FOR THE ALL WDC
drill = drilltoScreen(setup.d,setup.dH,Constants.NETWORKFUNCTIONS)

# Validate the result
checkEqualAssert(True,drill)

# LOGGINGING OUT THE APPLICATION
setup.d.close()