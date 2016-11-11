import unittest
from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *

class SiteScreen(unittest.TestCase):
    def setUp(self):
        #sleep(5)
        logger.info('**************SiteScreen****************')
        # self.driver = webdriver.Chrome('/Users/deepanshu.ahuja/Downloads/chromedriver')
        self.driver = webdriver.Firefox()
        self.driver.get(Constants.URL)
        self.driverHelper = DriverHelper(self.driver)

    def test_measures(self):
        login(self.driver, self.driverHelper, Constants.USERNAME, Constants.PASSWORD)
        configManager = launchPage(self.driver, self.driverHelper, Constants.SITES)
        screeninstance = getScreenInstance(self.driver,Constants.SITES)
        parenthandles = getHandlersForParentComponent(self.driver,self.driverHelper,configManager,Constants.SITES)
        handles = getHandlesForEachComponent(self.driver,self.driverHelper,configManager,Constants.SITES,parenthandles)
        #measure_tonnage = "Tonnage_AVG"
        measure_tonnage = "Tonnage"
        screeninstance.measure.doSelection(handles,measure_tonnage)
        #sleep(2)
        #measure_tonnage = "Tonnage_PEAK"
        #screeninstance.measure.doSelection(handles,measure_tonnage)

        sleep(2)
        measure_flows = "Flows"
        screeninstance.measure.doSelection(handles,measure_flows)
        measure_wancost = "Wan-Cost($)"
        sleep(2)
        screeninstance.measure.doSelection(handles,measure_wancost)


