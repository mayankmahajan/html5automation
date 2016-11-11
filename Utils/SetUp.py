from classes.DriverHelpers.DriverHelper import *


class SetUp:
    def __init__(self):
        #self.d = webdriver.Chrome('/Users/mayank.mahajan/Downloads/chromedriver54')
        self.d = webdriver.Firefox()
        self.d.get(Constants.URL)
        self.dH = DriverHelper(self.d)
        self.cM = ConfigManager()

