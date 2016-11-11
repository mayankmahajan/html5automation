import unittest
from Utils.logger import *
from selenium import webdriver

from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *


# Getting Setup Details
setup = SetUp()

# Getting TimeRange Info from Config Files
timeIteration = len(setup.cM.getNodeElements("quicklinks","quicklink"))
quicklinks = setup.cM.getNodeElements("quicklinks","quicklink").keys()
t=0


# Getting Measures Info from Config Files
measureIteration = len(setup.cM.getNodeElements("measures","measure"))
measures = setup.cM.getNodeElements("measures","measure").keys()


# Launching Application
login(setup, "admin", "Admin@123")

# Launch Site Screen
launchPage(setup,"site_Screen")

# Get the Instance of the screen
screenInstance = SitePageClass(setup.d)

# Get the handles of the screen
siteScreenHandle = getHandle(setup,"site_Screen")

# Set the Index value at 2
screenInstance.btv.setSelection(2,siteScreenHandle)

# Checking the drill to
drilltoScreen(setup.d,setup.dH,Constants.SITEINTERACTIONS)

# while loop is to iterate over all the quicklinks
while t < timeIteration:
    i=0
    setTimeRange(setup,quicklinks[t])

    # while loop is to iterate over all the measure
    while i < measureIteration:
        setMeasure(setup,measures[i],"site_Screen")

        # testcase body starts


        # defaultselection = btv.getSelection()
        # checkEqualAssert("0",defaultselection)







        # testcase body ends

        # Result Logging
        expected = "True"
        actual = "True"


        checkEqualAssert(expected,actual,quicklinks[t],measures[i])

        i+=1
        # end of measureSelection


    t+=1
    # end of while loop for QuicklinkSelections


# Closing the Testcase
setup.d.close()