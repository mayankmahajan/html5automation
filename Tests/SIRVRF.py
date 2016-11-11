import unittest
from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *


class SIRVRF(unittest.TestCase):
    def setUp(self):
        #sleep(5)
        logger.info('**************Site-->Site-Interactions-->VRF****************')
        # self.driver = webdriver.Chrome('/Users/deepanshu.ahuja/Downloads/chromedriver')
        self.driver = webdriver.Firefox()
        self.driver.get(Constants.URL)
        self.driverHelper = DriverHelper(self.driver)

    def test_login(self):
        data = {}

        login(self.driver, self.driverHelper, Constants.USERNAME, Constants.PASSWORD)

        configManager = launchPage(self.driver, self.driverHelper, Constants.SITES)

        #data = getBTVData(self.driver,self.driverHelper)
        # configManager = ConfigManager()
        # configManager = launchPage(self.driver,self.driverHelper,Constants.SITES)
        parenthandles = getHandlersForParentComponent(self.driver,self.driverHelper,configManager,Constants.SITES)
        handles = getHandlesForEachComponent(self.driver,self.driverHelper,configManager,Constants.SITES,parenthandles)

        screenInstance = getScreenInstance(self.driver,Constants.SITES)

        screenInstance.btv.setSelection(2,handles)



        #***************SITE INTERACTIONS***************
        drilltoScreen(self.driver,self.driverHelper,Constants.SITEINTERACTIONS)
        configManagerinteraction = ConfigManager()
        parenthandles = getHandlersForParentComponent(self.driver, self.driverHelper, configManagerinteraction,Constants.SITEINTERACTIONS)
        handles = getHandlesForEachComponent(self.driver, self.driverHelper, configManagerinteraction,Constants.SITEINTERACTIONS,parenthandles)
        screenInstanceinteraction = getScreenInstance(self.driver,Constants.SITEINTERACTIONS)
        screenInstanceinteraction.btv.setSelection(2, handles)

        #********************VRF SCREEN******************
        drilltoScreen(self.driver, self.driverHelper, Constants.VRF)
        configManagervrf = ConfigManager()
        parenthandles = getHandlersForParentComponent(self.driver, self.driverHelper, configManagervrf,Constants.VRF)
        handles = getHandlesForEachComponent(self.driver, self.driverHelper, configManagervrf, Constants.VRF,parenthandles)
        screenInstancevrf = getScreenInstance(self.driver, Constants.VRF)
        screenInstancevrf.btv.setSelection(2, handles)

    def tearDown(self):
        self.driver.close()
        logger.info('**************Site-->Site-Interactions-->VRF Completed*************')


if __name__ == "__main__":
    unittest.main(exit=False)
