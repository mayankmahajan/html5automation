import unittest
from Utils.logger import *
from selenium import webdriver
from Utils.utility import *
from classes.DriverHelpers.DriverHelper import DriverHelper
from Utils.Constants import *
from Utils.SetUp import *
from classes.Components.TimeRangeComponentClass import *
from classes.Pages.MRXScreens.UDScreenClass import *
from MRXUtils.MRXConstants import *
from classes.Pages.ExplorePageClass import *
from MRXUtils import UDHelper
from MRXUtils import SegmentHelper
import os

try:
    newFilterDetails=ConfigManager().getNodeElements("savenewfilter","filter")
    for k, filterDetail in newFilterDetails.iteritems():
        setup = SetUp()
        login(setup, Constants.USERNAME, Constants.PASSWORD)
        udScreenInstance = UDScreenClass(setup.d)
        exploreHandle = getHandle(setup, MRXConstants.ExploreScreen)
        udScreenInstance.explore.exploreList.launchModule(exploreHandle, "USER DISTRIBUTION")


        timeRangeFromPopup=''
        measureFromPopup=''
        UDHelper.clearFilter(setup,MRXConstants.UDSCREEN)
        ########################################## Apply Filter ########################################################

        SegmentHelper.clickOnfilterIcon(setup,MRXConstants.UDSCREEN,'nofilterIcon')
        timeRangeFromPopup, measureFromPopup = UDHelper.setQuickLink_Measure(setup, udScreenInstance, k)
        expected_filter = {}
        expected_filter = UDHelper.setGlobalFilters(udScreenInstance, setup,k)
        udScreenInstance.clickButton("Apply", getHandle(setup, MRXConstants.UDPPOPUP, MuralConstants.ALLBUTTONS))
        isError(setup)
        screenTooltipData = UDHelper.getUDPFiltersToolTipData(MRXConstants.UDSCREEN, setup)
        udpFilterFromScreen_1 = UDHelper.getUDPFiltersFromScreen(MRXConstants.UDSCREEN,setup)
        checkEqualDict(expected_filter, screenTooltipData, message="Verify Filters Selections",doSortingBeforeCheck=True)

        ############################################ Save Filter########################################################

        h=getHandle(setup,MRXConstants.UDSCREEN,'filterArea')
        h['filterArea']['toggleicon'][0].click()
        udScreenInstance.multiDropdown.domultipleSelectionWithNameWithoutActiveDropDown(getHandle(setup,MRXConstants.UDSCREEN,'filterArea'),'Save New Filter',0,parent="filterArea", child="multiSelectDropDown")
        filterDetailFromUI=UDHelper.saveNewFilter(setup,MRXConstants.SNFPOPUP,udScreenInstance,filterDetail)
        if filterDetail['button']=='Save':
            expected_detail = [filterDetail['filtername'], filterDetail['default']]
            checkEqualAssert(expected_detail,filterDetailFromUI,message='Verify Entered detail for Save New filter')

        ############################################ Verify new added Filter############################################

        h = getHandle(setup, MRXConstants.UDSCREEN, 'filterArea')
        h['filterArea']['toggleicon'][0].click()
        udScreenInstance.multiDropdown.domultipleSelectionWithNameWithoutActiveDropDown(getHandle(setup, MRXConstants.UDSCREEN, 'filterArea'), 'Load Filter', 0, parent="filterArea",child="multiSelectDropDown")
        UDHelper.verifySaveFilterFromLoadFilter(setup, udScreenInstance, MRXConstants.LFPOPUP,filterDetail)

        ######################################### Load Filter ##########################################################

        UDHelper.clearFilter(setup,MRXConstants.UDSCREEN)
        if filterDetail['button']=='Save':
            h = getHandle(setup, MRXConstants.UDSCREEN, 'filterArea')
            h['filterArea']['toggleicon'][0].click()
            udScreenInstance.multiDropdown.domultipleSelectionWithNameWithoutActiveDropDown(getHandle(setup, MRXConstants.UDSCREEN, 'filterArea'), 'Load Filter', 0, parent="filterArea",child="multiSelectDropDown")
            UDHelper.loadFilterFormSaveFilter(setup,MRXConstants.LFPOPUP, filterDetail)

            screenHandle=getHandle(setup, MRXConstants.UDSCREEN, 'time_measure')
            timeRangeFromScreen = str(screenHandle['time_measure']['span'][0].text).strip()
            measureFromScreen = str(screenHandle['time_measure']['span'][1].text).strip()
            checkEqualAssert(timeRangeFromPopup, timeRangeFromScreen,message='After load filter verify timerange value on screen')
            checkEqualAssert(measureFromPopup, measureFromScreen,message='After load filter verify measure value on screen')
            udpFilterFromScreen_2 = UDHelper.getUDPFiltersFromScreen(MRXConstants.UDSCREEN, setup)
            checkEqualDict(udpFilterFromScreen_1, udpFilterFromScreen_2, message="Verify loaded Filters on Screen",doSortingBeforeCheck=True)

            ############################################### Check Default Filter #######################################

            UDHelper.clearFilter(setup, MRXConstants.UDSCREEN)
            UDHelper.checkDefaultFilter(setup,udScreenInstance,MRXConstants.UDSCREEN,MRXConstants.ExploreScreen,filterDetail,udpFilterFromScreen_1,timeRangeFromPopup,measureFromPopup)
    setup.d.close()

    import MRX.DeleteSaveFilter

except Exception as e:
    isError(setup)
    r = "issue_" + str(random.randint(0, 9999999)) + ".png"
    setup.d.save_screenshot(r)
    logger.debug("Got Exception from Script Level try catch :: Screenshot with name = %s is saved", r)
    raise e
    setup.d.close()
