from BaseComponentClass import BaseComponentClass
from Utils.ConfigManager import ConfigManager
from Utils.logger import *

class AlertsComponentClass(BaseComponentClass):

    def __init__(self):
        BaseComponentClass.__init__(self)
        self.configmanager = ConfigManager()


    def getAlertList(self,h,parent,child):
        list = []
        for row in h[parent][child].find_elements_by_css_selector(".child,.evenChild"):
            list.append(self.createAlertListObject(row))
            # list[temp['header']+"$$"+temp['duration']] = temp
        return list


    def selectAlert(self,index,h,parent='alertlist',child="list"):
        try:
            h[parent][child][index].click()
            return True
        except:
            return False


    def getSelectedAlert(self,h,parent,child):
        return self.getAlertList(h,parent,child)

    def createAlertListObject(self,h):
        alertObject={}
        alertObject['handled'] = self.getAlertHandledIcon(h)
        alertObject['header'] = self.getAlertLabels(h)[0]
        alertObject['duration'] = self.getAlertLabels(h)[1]
        alertObject['alarmcount'] = self.getAlertLabels(h)[2]
        alertObject['measure'] = self.getAlertLabels(h)[3]
        alertObject['color'] = self.getThresholdIconColor(h)
        return alertObject

    def getAlertHandledIcon(self,h):
        return False if "UnHandled".upper() in h.find_element_by_tag_name("img").get_attribute("class").upper() else True

    def getAlertLabels(self,h):
        return [el.text.strip() for el in h.find_elements_by_tag_name("label")]

    def getThresholdIconColor(self,h):
        return h.find_element_by_tag_name("circle").get_attribute("fill").strip()

    def getAlertFullBody(self,h,parent="alertinfo",child=""):
        alertBOdyObject = self.createAlertBodyObject(h[parent])

        pass

    def createAlertBodyObject(self,h):

        alertBOdyObject = {}
        alertBOdyObject['handled'] = self.getAlertHandledIcon(h)
        alertBOdyObject['header'] = self.getAlertHeader(h)
        alertBOdyObject['range'],alertBOdyObject['alarmcount'] = self.getAlertDuration(h)


        alertBOdyObject['measure'] = self.getAlertHandledIcon(h)
        alertBOdyObject['color'] = self.getAlertHandledIcon(h)
        alertBOdyObject['alarmrows'] = self.getAlarmRows(h)
        alertBOdyObject['ruleName'],alertBOdyObject['gran'],alertBOdyObject['type'] = self.getRuleInfo(h)

        alertBOdyObject['state']
        alertBOdyObject['links']
        alertBOdyObject['alerttable']


    def getAlarmRows(self,h):
        alarmsrows = []
        for el in h['kiwik-threshold-alarm-row']:
            alarmsrows.append(el.text)
        return alarmsrows

    def getAlertHeader(self,h,child="header"):
        return h[child].text

    def getAlertDuration(self,h,child="timecount"):
        time = h[child].find_elements_by_class_name("time")[0].text
        count = h[child].find_elements_by_class_name("count")[0].text
        return time,count

    def getRuleInfo(self,h,child=""):
        handleTosiblings = self.getAllRuleSiblings(h)
        siblings = []
        for el in handleTosiblings:
            siblings.append(el.text)
        return siblings

    def getAllRuleSiblings(self,h,child=""):
        for el in h.find_elements_by_tag_name("span"):
            if el.text == "Rule":
                return el.find_elements_by_xpath("..//span")


    def getAlertHeader(self,h):
        pass


