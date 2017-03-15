from Utils.SetUp import *
from MuralUtils.MuralConstants import *
from Utils.utility import *
from classes.Pages.MuralScreens.NetworkScreenClass import *
from classes.Components.WorkflowStartComponent import *
from classes.Components.TimeRangeComponentClass import *
from classes.Pages.MuralScreens.AccessTechnologyClass import *
from suitemural_network.test_accesstechnology_general import *
import sys


try:
    setup = SetUp()
    wfstart = WorkflowStartComponentClass()
    sleep(8)
    wfstart.launchScreen("Network",getHandle(setup,MuralConstants.WFSTARTSCREEN))
    networkScreenInstance = NetworkScreenClass(setup.d)
    networkScreenInstance.cm.activate(getHandle(setup, MuralConstants.NWSCREEN, "exploreBar"))
    networkScreenInstance.cm.goto("Access Technology", getHandle(setup, MuralConstants.NWSCREEN, "exploreBar"))
    accesstechnologyScreenInstance = AccessTechnolohyScreenClass(setup.d)

    qs = setup.cM.getNodeElements("wizardquicklinks1", "wizardquicklink")
    quicklink = setup.cM.getAllNodeElements("wizardquicklinks1", "wizardquicklink")

    for e in quicklink:
        #print qs[e]['locatorText']
        #for q in quicklink:

        #accesstechnologyScreenInstance.timeBar.getLabel(getHandle(setup, MuralConstants.ATSCREEN, "ktrs"))
        #accesstechnologyScreenInstance.timeBar.getSelectedQuickLink(getHandle(setup, MuralConstants.ATSCREEN, "ktrs"))
        accesstechnologyScreenInstance.timeBar.setQuickLink(qs[e]['locatorText'],getHandle(setup, MuralConstants.ATSCREEN, "ktrs"))
        selectedQuicklink = networkScreenInstance.timeBar.getSelectedQuickLink(getHandle(setup, MuralConstants.ATSCREEN, "ktrs"))

        screenName = accesstechnologyScreenInstance.cm.getScreenName(getHandle(setup, MuralConstants.ATSCREEN, "exploreBar"))
        breadCrumbLabel = accesstechnologyScreenInstance.cm.getRHSBreadCrumbLabel(getHandle(setup, MuralConstants.ATSCREEN, "exploreBar"))

        measures = setup.cM.getNodeElements("networkdimeas", "measure")

        for k, measure in measures.iteritems():
            if not hasattr(measure,"summaryCard"):
                measureSelected = accesstechnologyScreenInstance.picker.domultipleSelectionWithName(getHandle(setup,MuralConstants.NWSCREEN,"measureChangeSection"),measure['locatorText'],0,"measureChangeSection","measure")
                checkEqualAssert(measure['locatorText'],measureSelected,"","","Verify Selected measure")

                if hasattr(measure,"options") and 'direction' in measure['options']:
                    isDirectionsPresent = accesstechnologyScreenInstance.switcher.getMeasureChangeSelectedSwitcher(getHandle(setup, MuralConstants.NWSCREEN, "measureChangeSection"))
                    checkEqualAssert(not False, isDirectionsPresent, "", "","Verify presence of Directions for Measure = " + measureSelected)

                for d in range(0,3):
                    if accesstechnologyScreenInstance.switcher.measureChangeSwitcher(d,getHandle(setup,MuralConstants.ATSCREEN,"measureChangeSection")):
                        selectedSwitcher = accesstechnologyScreenInstance.switcher.getMeasureChangeSelectedSwitcher(getHandle(setup,MuralConstants.ATSCREEN,"measureChangeSection"))
                        checkEqualAssert([d],selectedSwitcher,"","","Verify Selected Measure Direction")
                        checkAllComponentRelatedToPie(setup, accesstechnologyScreenInstance, measure, False)
                        toolTipPieAndPieLegend(setup,accesstechnologyScreenInstance)

                        p = accesstechnologyScreenInstance.pielegend.getData(getHandle(setup, MuralConstants.ATSCREEN, "pielegend"))
                        for i in range(len(p['legendText'])):
                            accesstechnologyScreenInstance.pielegend.setSelection(setup.dH, [i],getHandle(setup, MuralConstants.ATSCREEN, "pielegend"), True)
                            checkAllComponentRelatedToPie(setup, accesstechnologyScreenInstance, measure,i,True)
                else:
                    isDirectionsPresent = accesstechnologyScreenInstance.switcher.getMeasureChangeSelectedSwitcher(getHandle(setup, MuralConstants.NWSCREEN, "measureChangeSection"))
                    checkEqualAssert(False, isDirectionsPresent, "", "","Verify presence of Directions for Measure = " + measureSelected)
                    d = None
                    checkAllComponentRelatedToPie(setup, accesstechnologyScreenInstance, measure, False)

                    toolTipPieAndPieLegend(setup, accesstechnologyScreenInstance)
                    p = accesstechnologyScreenInstance.pielegend.getData(getHandle(setup, MuralConstants.ATSCREEN, "pielegend"))
                    for i in range(len(p['legendText'])):
                        accesstechnologyScreenInstance.pielegend.setSelection(setup.dH, [i],getHandle(setup, MuralConstants.ATSCREEN,"pielegend"), True)
                        checkAllComponentRelatedToPie(setup, accesstechnologyScreenInstance, measure, i, True)

    accesstechnologyScreenInstance.cm.activate(getHandle(setup, MuralConstants.NWSCREEN, "exploreBar"), child="export")
    accesstechnologyScreenInstance.cm.goto(MuralConstants.TandMScreen, getHandle(setup, MuralConstants.NWSCREEN, "exploreBar"))

    #accesstechnologyScreenInstance.cm.gotoScreenViaBreadCrumb("Network",getHandle(setup, MuralConstants.NWSCREEN, "breadcrumb"))
    #accesstechnologyScreenInstance.cm.activateWorkFlowDropDown(getHandle(setup, MuralConstants.NWSCREEN, "breadcrumb"))
    #accesstechnologyScreenInstance.cm.gotoScreenViaWorkFlowDrop("Trend & Monitoring",getHandle(setup, MuralConstants.NWSCREEN, "breadcrumb"))

except Exception as e:
    print str(e)
    # sys._current_frames()
    setup.d.close()
