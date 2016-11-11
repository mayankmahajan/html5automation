import unittest
from Utils.logger import *
from selenium import webdriver

from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *



######################## TEST FOR THE LOGIN PAGE #########################

# Getting Setup Details and launching the application
setup = SetUp()


# Logging into the setup
result = login(setup, "admin", "Admin@123")
sleep(2)


#Result logging
checkEqualAssert("True",str(result),)

# Logging out of the application
setup.d.close()