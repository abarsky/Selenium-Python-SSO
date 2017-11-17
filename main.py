#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from multiprocessing import Process
from multiprocessing import Manager
from threading import Thread
from selenium.webdriver.common.action_chains import ActionChains
import multiprocessing
from time import sleep
import threading
from threading import Thread
from random import randint
import random
import string
import time
import datetime
import os
import sys

currentStep=''
currentCase=''
screenshotCount=1
folderName="none"
userVariables={}
superFoundElement=0
superFoundWrite=0
elementsList={}
test_results="none"
driver="none"
currentTab=0
test_results=''

def createFolder():
    try:
        global folderName
        folderName = time.strftime("%m.%d-%H.%M")
        os.mkdir(folderName)
        # return folderName
    except:
        test_results.write("[ERROR] Could not create the folder for screenshots\n")

def createFileForTestResults():
    try:
        global test_results
        test_results_name = (folderName + "_" + "test_results.txt")
        # test_results = open(test_results_name, "w")
        timestamp_for_file = time.strftime("%Y-%m-%d %H:%M:%S")
        test_results = open(test_results_name, "w")
        test_results.write("Started test " + timestamp_for_file + "\n")
    except:
        print "Something went wrong while trying to create the file for test results"

def startDriver():
    try:
        global driver
        driver=webdriver.Chrome('chromedriver')
        driver.maximize_window()
    except:
        test_results.write("[ERROR] Could not find the ChromeDriver in the current directory\n")

def closeFileForTestResults():
    try:
        global test_results
        timestamp_for_end=time.strftime("%Y-%m-%d %H:%M:%S")
        test_results.write("Finished test "+timestamp_for_end+"\n")
        test_results.close()
    except:
        print "Something went wrong while trying to close the file for test results"

def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except:
        pass

def findElement(ElementLocatorName, LocateBy, assertNot="no"):
    try:
        pauseForDuration(2)
        try:
            driver.execute_script("var abc=document.getElementsByTagName('div').length;")
            WebDriverWait(driver, 4).until(
            ajax_complete,  "Timeout waiting for page to load")
        except:
            pass
        global elementsList
        if LocateBy=="id":
            waitForId=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ElementLocatorName)))
            elementsList=driver.find_elements_by_id(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="name":
            waitForName=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, ElementLocatorName)))
            elementsList=driver.find_elements_by_name(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="xpath":
            waitForXpath=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ElementLocatorName)))
            elementsList=driver.find_elements_by_xpath(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="link":
            waitForLink=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, ElementLocatorName)))
            elementsList=driver.find_elements_by_link_text(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="partial_link":
            waitForPartialLink=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ElementLocatorName)))
            elementsList=driver.find_elements_by_partial_link_text(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="tag_name":


            textinside=ElementLocatorName
            textinsidelower=textinside.lower()
            textinsidetitle=textinside.title()
            textinsideupper=textinside.upper()
            textinsidecapitzalized=textinside.capitalize()

            elementsListBasic=[]
            elementsListCapitalized=[]
            elementsListTitle=[]
            elementsListUpper=[]
            elementsListLower=[]
            time.sleep(5)
            waitForCss = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*")))

            elementsListBasic=driver.find_elements_by_xpath("//*[contains(text(),'"   +  textinside   + "')]")
            if len(elementsListBasic)==1:
                for element in elementsListBasic:
                    scannedElement=element.text
                    if textinside in scannedElement:
                        return element
            if len(elementsListBasic) > 1:
                for element in elementsListBasic:
                    scannedElement=element.text
                    if textinside==scannedElement:
                        return element
                    else:
                        if textinside in scannedElement:
                            return element

            if not elementsListBasic:
                elementsListLower = driver.find_elements_by_xpath("//*[contains(text(),'" + textinsidelower + "')]")
                if len(elementsListLower)==1:
                    for element in elementsListLower:
                        scannedElement = element.text
                        if textinsidelower in scannedElement:
                            return element
                if len(elementsListLower)>1:
                    for element in elementsListLower:
                        scannedElement = element.text
                        if textinsidelower==scannedElement:
                            return element
                        else:
                            if textinsidelower in scannedElement:
                                return element

            if not elementsListLower:
                elementsListCapitalized = driver.find_elements_by_xpath("//*[contains(text(),'" + textinsidecapitzalized + "')]")
                if len(elementsListCapitalized)==1:
                    for element in elementsListCapitalized:
                        scannedElement = element.text
                        if textinsidecapitzalized in scannedElement:
                            return element
                if len(elementsListCapitalized)>1:
                    for element in elementsListCapitalized:
                        scannedElement = element.text
                        if textinsidecapitzalized==scannedElement:
                            return element
                        else:
                            if textinsidecapitzalized in scannedElement:
                                return element

            if not elementsListCapitalized:
                elementsListUpper = driver.find_elements_by_xpath("//*[contains(text(),'" + textinsideupper + "')]")
                if len(elementsListUpper)==1:
                    for element in elementsListUpper:
                        scannedElement = element.text
                        if textinsideupper in scannedElement:
                            return element
                if len(elementsListUpper) > 1:
                    for element in elementsListUpper:
                        scannedElement = element.text
                        if textinsideupper==scannedElement:
                            return element
                        else:
                            if textinsideupper in scannedElement:
                                return element

            if not elementsListUpper:
                elementsListTitle = driver.find_elements_by_xpath("//*[contains(text(),'" + textinsidetitle + "')]")
                if len(elementsListTitle)==1:
                    for element in elementsListTitle:
                        scannedElement = element.text
                        if textinsidetitle in scannedElement:
                            return element
                if len(elementsListTitle) > 1:
                    for element in elementsListTitle:
                        scannedElement = element.text
                        if textinsidetitle==scannedElement:
                            return element
                        else:
                            if textinsidetitle in scannedElement:
                                return element


        if LocateBy=="class_name":
            waitForClass=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, ElementLocatorName)))
            elementsList=driver.find_elements_by_class_name(ElementLocatorName)
            return elementsList[0]
        if LocateBy=="css_selector":
            waitForCss=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ElementLocatorName)))
            elementsList=driver.find_elements_by_css_selector(ElementLocatorName)
            return elementsList[0]
    except:
        if assertNot=="no":
            test_results.write("[ERROR] Could not find web element with the locator '" + ElementLocatorName + "'\n")
        if assertNot=="yes":
            print ""
        return 0

def clickOn(ElementLocatorName,LocateBy):
    try:
        elementToClickOn=findElement(ElementLocatorName,LocateBy)
        if (elementToClickOn!=0):
            elementToClickOn.click()
    except:
        test_results.write("[ERROR] Could not click on the web element with the locator '"+ElementLocatorName+"'\n")


def hover(ElementLocatorName,LocateBy):
    try:
        global test_results
        elementToHoverOver=findElement(ElementLocatorName,LocateBy)
        if (elementToHoverOver!=0):
            hov = ActionChains(driver).move_to_element(elementToHoverOver)
            hov.perform()
            pauseForDuration(3)
    except:
        test_results.write("[ERROR] Could not hover over the web element with the locator '" + ElementLocatorName + "'\n")

def writeIn(ElementLocatorName,Text,LocateBy):
    try:
        elementToWriteIn=findElement(ElementLocatorName,LocateBy)
        if (elementToWriteIn!=0):
            elementToWriteIn.clear()
            elementToWriteIn.send_keys(Text)
    except:
        test_results.write("[ERROR] Could not write text in the web element with the locator '" + ElementLocatorName + "'\n")

        '''
        try:
            if LocateBy=="id":
                pauseForDuration(3)
                jsScriptToExecuteForId='document.getElementById("'+ElementLocatorName+'").value ="' + Text + '";'
                driver.execute_script(jsScriptToExecuteForId)
                pauseForDuration(3)
            if LocateBy=="name":
                pauseForDuration(3)
                jsScriptToExecuteForName='var elementsWithThatName=document.getElementsByName("'+ElementLocatorName+'");elementsWithThatName[0].value ="' + Text + '";'
                driver.execute_script(jsScriptToExecuteForName)
                pauseForDuration(3)
            if LocateBy=="xpath":
                pauseForDuration(3)
                jsScriptToExecuteForXpath='var element = document.evaluate("' + ElementLocatorName +'" ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue;if (element != null) {element.value="'+ Text +'";}'
                driver.execute_script(jsScriptToExecuteForXpath)
                pauseForDuration(3)
            if LocateBy=="link":
                pauseForDuration(3)
                jsScriptToExecuteForLink='var els = document.getElementsByTagName("a");for (var i = 0, l = els.length; i < l; i++) {var el = els[i];if (el.innerHTML == "' + ElementLocatorName + '") {el.value="'+ Text +'";}}'
                driver.execute_script(jsScriptToExecuteForLink)
                pauseForDuration(3)
            if LocateBy=="partial_link":
                pauseForDuration(3)
                jsScriptToExecuteForPartialLink='var els = document.getElementsByTagName("a");for (var i = 0, l = els.length; i < l; i++) {var el = els[i];var val_el=el.innerHTML;if (val_el.toLowerCase().indexOf("'+ ElementLocatorName +'") >= 0) {val_el.value="'+ Text +'";}}'
                driver.execute_script(jsScriptToExecuteForPartialLink)
                pauseForDuration(3)
            if LocateBy=="tag":
                pauseForDuration(3)
                jsScriptToExecuteForTagName='document.getElementByTagName("'+ElementLocatorName+'").value ="' + Text + '";'
                driver.execute_script(jsScriptToExecuteForTagName)
                pauseForDuration(3)
            if LocateBy=="class_name":
                pauseForDuration(3)
                jsScriptToExecuteForClassName='document.getElementByClassName("'+ElementLocatorName+'").value ="' + Text + '";'
                driver.execute_script(jsScriptToExecuteForClassName)
                pauseForDuration(3)
            if LocateBy=="css_selector":
                pauseForDuration(3)
                jsScriptToExecuteForCss='element = document.querySelector("'+ElementLocatorName+'");element.value="'+ Text +'";'
                driver.execute_script(jsScriptToExecuteForCss)
                pauseForDuration(3)
        except:
            test_results.write("[ERROR] Could not write text in the web element with the locator '"+ElementLocatorName+"'\n")
        '''

def uploadIn(ElementLocatorName,Text,LocateBy):
    try:
        elementToWriteIn=findElement(ElementLocatorName,LocateBy)
        if (elementToWriteIn!=0):
            elementToWriteIn.clear()
            absoluteFilePath=os.path.abspath(Text)
            elementToWriteIn.send_keys(absoluteFilePath)
    except:
        test_results.write("[ERROR] Could not upload file in the web element with the locator '"+ElementLocatorName+"'\n")

def pressKey(keyToPress):
    def pressKey(keyToPress, ElementLocatorName, LocateBy):
        try:
            global test_results
            genericSelector = findElement(ElementLocatorName, LocateBy)
            if (keyToPress is "RETURN"):
                genericSelector.send_keys(Keys.RETURN);
            if (keyToPress is "ADD"):
                genericSelector.send_keys(Keys.ADD);
            if (keyToPress is "ALT"):
                genericSelector.send_keys(Keys.ALT);
            if (keyToPress is "ARROW_DOWN"):
                genericSelector.send_keys(Keys.ARROW_DOWN);
            if (keyToPress is "ARROW_LEFT"):
                genericSelector.send_keys(Keys.ARROW_LEFT);
            if (keyToPress is "ARROW_RIGHT"):
                genericSelector.send_keys(Keys.ARROW_RIGHT);
            if (keyToPress is "ARROW_UP"):
                genericSelector.send_keys(Keys.ARROW_UP);
            if (keyToPress is "BACKSPACE"):
                genericSelector.send_keys(Keys.BACKSPACE);
            if (keyToPress is "BACK_SPACE"):
                genericSelector.send_keys(Keys.BACK_SPACE);
            if (keyToPress is "CANCEL"):
                genericSelector.send_keys(Keys.CANCEL);
            if (keyToPress is "CLEAR"):
                genericSelector.send_keys(Keys.CLEAR);
            if (keyToPress is "COMMAND"):
                genericSelector.send_keys(Keys.COMMAND);
            if (keyToPress is "CONTROL"):
                genericSelector.send_keys(Keys.CONTROL);
            if (keyToPress is "DECIMAL"):
                genericSelector.send_keys(Keys.DECIMAL);
            if (keyToPress is "DELETE"):
                genericSelector.send_keys(Keys.DELETE);
            if (keyToPress is "DIVIDE"):
                genericSelector.send_keys(Keys.DIVIDE);
            if (keyToPress is "DOWN"):
                genericSelector.send_keys(Keys.DOWN);
            if (keyToPress is "END"):
                genericSelector.send_keys(Keys.END);
            if (keyToPress is "EQUALS"):
                genericSelector.send_keys(Keys.EQUALS);
            if (keyToPress is "ENTER"):
                genericSelector.send_keys(Keys.ENTER);
            if (keyToPress is "ESCAPE"):
                genericSelector.send_keys(Keys.ESCAPE);
            if (keyToPress is "F1"):
                genericSelector.send_keys(Keys.F1);
            if (keyToPress is "F2"):
                genericSelector.send_keys(Keys.F2);
            if (keyToPress is "F3"):
                genericSelector.send_keys(Keys.F3);
            if (keyToPress is "F4"):
                genericSelector.send_keys(Keys.F4);
            if (keyToPress is "F5"):
                genericSelector.send_keys(Keys.F5);
            if (keyToPress is "F6"):
                genericSelector.send_keys(Keys.F6);
            if (keyToPress is "F7"):
                genericSelector.send_keys(Keys.F7);
            if (keyToPress is "F8"):
                genericSelector.send_keys(Keys.F8);
            if (keyToPress is "F9"):
                genericSelector.send_keys(Keys.F9);
            if (keyToPress is "F10"):
                genericSelector.send_keys(Keys.F10);
            if (keyToPress is "F11"):
                genericSelector.send_keys(Keys.F11);
            if (keyToPress is "F12"):
                genericSelector.send_keys(Keys.F12);
            if (keyToPress is "HELP"):
                genericSelector.send_keys(Keys.HELP);
            if (keyToPress is "INSERT"):
                genericSelector.send_keys(Keys.INSERT);
            if (keyToPress is "LEFT"):
                genericSelector.send_keys(Keys.LEFT);
            if (keyToPress is "LEFT_ALT"):
                genericSelector.send_keys(Keys.LEFT_ALT);
            if (keyToPress is "LEFT_CONTROL"):
                genericSelector.send_keys(Keys.LEFT_CONTROL);
            if (keyToPress is "LEFT_SHIFT"):
                genericSelector.send_keys(Keys.LEFT_SHIFT);
            if (keyToPress is "META"):
                genericSelector.send_keys(Keys.META);
            if (keyToPress is "MULTIPLY"):
                genericSelector.send_keys(Keys.MULTIPLY);
            if (keyToPress is "NULL"):
                genericSelector.send_keys(Keys.NULL);
            if (keyToPress is "NUMPAD0"):
                genericSelector.send_keys(Keys.NUMPAD0);
            if (keyToPress is "NUMPAD1"):
                genericSelector.send_keys(Keys.NUMPAD1);
            if (keyToPress is "NUMPAD2"):
                genericSelector.send_keys(Keys.NUMPAD2);
            if (keyToPress is "NUMPAD3"):
                genericSelector.send_keys(Keys.NUMPAD3);
            if (keyToPress is "NUMPAD4"):
                genericSelector.send_keys(Keys.NUMPAD4);
            if (keyToPress is "NUMPAD5"):
                genericSelector.send_keys(Keys.NUMPAD5);
            if (keyToPress is "NUMPAD6"):
                genericSelector.send_keys(Keys.NUMPAD6);
            if (keyToPress is "NUMPAD7"):
                genericSelector.send_keys(Keys.NUMPAD7);
            if (keyToPress is "NUMPAD8"):
                genericSelector.send_keys(Keys.NUMPAD8);
            if (keyToPress is "NUMPAD9"):
                genericSelector.send_keys(Keys.NUMPAD9);
            if (keyToPress is "PAGE_DOWN"):
                genericSelector.send_keys(Keys.PAGE_DOWN);
            if (keyToPress is "PAGE_UP"):
                genericSelector.send_keys(Keys.PAGE_UP);
            if (keyToPress is "PAUSE"):
                genericSelector.send_keys(Keys.PAUSE);
            if (keyToPress is "RIGHT"):
                genericSelector.send_keys(Keys.RIGHT);
            if (keyToPress is "SEMICOLON"):
                genericSelector.send_keys(Keys.SEMICOLON);
            if (keyToPress is "SEPARATOR"):
                genericSelector.send_keys(Keys.SEPARATOR);
            if (keyToPress is "SHIFT"):
                genericSelector.send_keys(Keys.SHIFT);
            if (keyToPress is "SPACE"):
                genericSelector.send_keys(Keys.SPACE);
            if (keyToPress is "SUBTRACT"):
                genericSelector.send_keys(Keys.SUBTRACT);
            if (keyToPress is "TAB"):
                genericSelector.send_keys(Keys.TAB);
            if (keyToPress is "UP"):
                genericSelector.send_keys(Keys.UP);
        except:
            test_results.write("[ERROR] Could not press '"+keyToPress+"\n")

def pauseForDuration(duration):
    try:
        #driver.implicitly_wait(duration)
        time.sleep(duration)
    except:
        test_results.write("[ERROR] Could not pause for '"+duration+"'\n")

def refreshPage():
    try:
        driver.refresh()
    except:
        test_results.write("[ERROR] Could not refresh page\n")

def takeScreenshot(currentCase):
    try:
        global folderName
        global screenshotCount
        driver.save_screenshot(folderName+"/"+str(screenshotCount)+". "+currentCase+".png")
        screenshotCount=screenshotCount+1
    except:
        pass
        test_results.write("[ERROR] Could not take screenshot\n")

def closeAlert(currentCase):
    global test_results
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
        driver.switch_to.alert.accept()
        if currentCase=="in_case_it_gets_stuck":
            test_results.write("[ERROR] An alert box was detected, the test was interrupted.</br>Add a Close " \
                            "Alert Box step to prevent this from happening.\n")
            takeScreenshot("alert_detected")
    except:
        if currentCase!="in_case_it_gets_stuck":
            test_results.write("[ERROR] No alert box detected\n")


def closeTab():
    global test_results
    global currentTab
    try:
        driver.close()
        test_results.write("Closed tab\n")
        switchToPreviousTab()
    except:
        test_results.write("[ERROR] Could not close tab\n")



def switchToNextTab():
    global test_results
    global currentTab
    try:
        len(driver.window_handles)
        nextTab=currentTab+1
        currentTab=currentTab+1
        driver.switch_to_window(driver.window_handles[nextTab])
        test_results.write("Switched to next tab\n")
    except:
        test_results.write("[ERROR] Could not switch to next tab\n")


def switchToPreviousTab():
    global test_results
    global currentTab
    try:
        len(driver.window_handles)
        previousTab = currentTab-1
        currentTab = currentTab-1
        driver.switch_to_window(driver.window_handles[previousTab])
        test_results.write("Switched to previous tab\n")
    except:
        test_results.write("[ERROR] Could not switch to previous tab\n")

			
def switchToFrame(ElementLocatorName, LocateBy):
    global test_results
    frameToSwitchTo = findElement(ElementLocatorName, LocateBy)
    try:
        driver.switch_to.frame(frameToSwitchTo)
        currentTitle=driver.title
        test_results.write("Switched to " + currentTitle + " frame\n")
    except:
        test_results.write("[ERROR] Frame could not be detected\n")


def switchBack():
    global test_results
    try:
        driver.switch_to.default_content()
        test_results.write("Switched back to default content\n")
    except:
        test_results.write("[ERROR] Could not switch back to default content\n")


def scroll(scrollType,scrollDistance):
    try:
        global test_results
        if(scrollType=='ScrollDown'):
            jsCodeScrollDown="window.scrollBy(0,"+scrollDistance+");"
            driver.execute_script(jsCodeScrollDown)
            pauseForDuration(3)
        if(scrollType=='ScrollUp'):
            jsCodeScrollUp="window.scrollBy(0,-"+scrollDistance+");"
            driver.execute_script(jsCodeScrollUp)
            pauseForDuration(3)
        if(scrollType=='ScrollLeft'):
            jsCodeScrollLeft="window.scrollBy(-"+scrollDistance+",0);"
            driver.execute_script(jsCodeScrollLeft)
            pauseForDuration(3)
        if(scrollType=='ScrollRight'):
            jsCodeScrollRight="window.scrollBy("+scrollDistance+",0);"
            driver.execute_script(jsCodeScrollRight)
            pauseForDuration(3)
        if(scrollType=='ScrollElem'):
            jsCodeScrollToElement="$('html, body').animate({scrollTop: $('" + scrollDistance + "').offset().top}, 1000);"
            driver.execute_script(jsCodeScrollToElement)
            pauseForDuration(3)
            takeScreenshotForMovie()
        if(scrollType=='ScrollBottom'):
            jsCodeScrollBottom="window.scrollTo(0,document.body.scrollHeight);"
            driver.execute_script(jsCodeScrollBottom)
            pauseForDuration(3)
        if(scrollType=='ScrollTop'):
            jsCodeScrollTop="window.scrollTo(0, 0);"
            driver.execute_script(jsCodeScrollTop)
            pauseForDuration(3)
    except:
        pass
        test_results.write("[ERROR] Could not scroll\n")


def echo(scrollType,scrollDistance):
    try:
        global test_results
        if (scrollType=="PrintTitle"):
            currentTitle = driver.title
            test_results.write("Current Title: " + currentTitle  +"\n")
        if (scrollType=="PrintUrl"):
            currentUrl = driver.current_url
            test_results.write("Current URL: " + currentUrl + "\n")
    except:
        test_results.write("[ERROR] Could not print to Results.\n")

def getValue(ElementLocatorName,LocateBy):
    try:
        global test_results
        elementToGetValueFrom=findElement(ElementLocatorName,LocateBy)
        if (elementToGetValueFrom.tag_name=="input" or elementToGetValueFrom.tag_name=='textarea'):
            valueFromElement=elementToGetValueFrom.get_attribute("value")
        else:
            valueFromElement=elementToGetValueFrom.text
        return valueFromElement
    except:
        test_results.write("[ERROR] Could not get the value from the web element with the locator '"+ElementLocatorName+"\n")

def pickOptionFromSelect(ElementLocatorName,LocateBy,input,index=0):
    try:
        selectElement=Select(findElement(ElementLocatorName,LocateBy))
        if index==0:
            try:
                selectElement.select_by_visible_text(input)
            except:
                pass
            try:
                selectElement.select_by_value(input)
            except:
                pass
        else:
             selectElement.select_by_index(input)
    except:
        test_results.write("[ERROR] Could not select the option '"+input+"' from the Select with the locator '"+ElementLocatorName+"\n")

def executeJS(jsCode):
    try:
        jsCodeFull=""+jsCode+""
        driver.execute_script(jsCodeFull)
        pauseForDuration(3)
    except:
        test_results.write("[ERROR] Could not execute the following JavaScript code: "+jsCodeFull+ " \n")

def assertElementIsPresent(elementToCheck,LocateBy,currentCase):
    try:
        elementToCheck=findElement(elementToCheck,LocateBy)
        if(elementToCheck!=0):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+elementToCheck+ "' is present \n")

def assertTitle(titleToCheck,currentCase):
    try:
        global test_results
        global test_results
        expectedTitle=titleToCheck
        currentTitle=driver.title
        if expectedTitle in currentTitle:
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the title contains the following value "+titleToCheck+ "\n")



def assertUrlContains(titleToCheck,currentCase):
    try:
        global test_results
        global test_results
        expectedTitle=titleToCheck
        currentTitle=driver.current_url
        if expectedTitle in currentTitle:
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the URL contains the value "+titleToCheck+ "\n")

def assertElementIsNotPresent(elementToCheck,LocateBy,currentCase):
    try:
        elementToCheck=findElement(elementToCheck,LocateBy,"yes")
        if(elementToCheck==0  or str(elementToCheck)=='None'):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+elementToCheck+ "' is not present \n")

def assertMatchesValue(valueContainer,LocateBy,expectedValue,currentCase):
    try:
        valueContainerOne=findElement(valueContainer,LocateBy)
        if (valueContainerOne.tag_name=="input" or valueContainerOne.tag_name=="textarea"):
            actualValue=valueContainerOne.get_attribute("value")
        else:
            actualValue=valueContainerOne.text
        if (actualValue == expectedValue):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+valueContainer+ "' has the value '"+expectedValue + "'\n")

def assertNotMatchesValue(valueContainer,LocateBy,expectedValue,currentCase):
    try:
        valueContainerOne=findElement(valueContainer,LocateBy)
        if (valueContainerOne.tag_name=="input" or valueContainerOne.tag_name=="textarea"):
            actualValue=valueContainerOne.get_attribute("value")
        else:
            actualValue=valueContainerOne.text
        if (actualValue != expectedValue):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+valueContainer+ "' does not have the value '"+expectedValue + "'\n")

def assertContainsValue(valueContainer,LocateBy, expectedValue,currentCase):
    try:
        valueContainerOne=findElement(valueContainer,LocateBy)
        if (valueContainerOne.tag_name=="input" or valueContainerOne.tag_name=="textarea"):
            actualValue=valueContainerOne.text
        else:
            actualValue=valueContainerOne.text
        if(expectedValue in actualValue):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+valueContainer+ "' contains the value '"+expectedValue + "'\n")

def assertNotContainsValue(valueContainer,LocateBy,expectedValue,currentCase):
    try:
        valueContainerOne=findElement(valueContainer,LocateBy)
        if (valueContainerOne.tag_name=="input" or valueContainerOne.tag_name=="textarea"):
            actualValue=valueContainerOne.text
        else:
            actualValue=valueContainerOne.text
        if(expectedValue not in actualValue):
            test_results.write("[PASSED] "+currentCase +"\n")
        else:
            test_results.write("[FAILED] "+currentCase +"\n")
    except:
        test_results.write("[ERROR] "+ currentCase + " - Could not check if the web element with the locator '"+valueContainer+ "' does not contain the value '"+expectedValue + "'\n")


def generateRandomNumber(length):
    try:
        if length==1:
            randomNumber = randint(1, 9)
        if length==2:
            randomNumber = randint(10, 99)
        if length==3:
            randomNumber = randint(100,999)
        if length==4:
            randomNumber = randint(1000,9999)
        return randomNumber
    except:
        test_results.write("[ERROR] Could not generate random number\n")

def generateRandomString(length):
    try:
        return ''.join(random.choice(string.lowercase) for i in range(length))
    except:
        test_results.write("[ERROR] Could not generate random string\n")

def enterVariable(userVariableName,userVariableValue):
    try:
        global userVariables
        userVariables[userVariableName]=userVariableValue
    except:
        test_results.write("[ERROR] Could not save the variable '"+userVariableName+"' with the value '"+userVariableValue+"'\n")

def setRandomNumberVariable(userVariableName,numberLength):
    try:
        global userVariables
        userVariables[userVariableName]=generateRandomNumber(numberLength)
    except:
        test_results.write("[ERROR] Could not save the random number variable '"+userVariableName+"' with the length '"+numberLength+"'\n")

def setRandomStringVariable(userVariableName,stringLength):
    try:
        global userVariables
        userVariables[userVariableName]=generateRandomString(stringLength)
    except:
        test_results.write("[ERROR] Could not save the random string variable '"+userVariableName+"' with the length '"+stringLength+"'\n")

def setRandomEmailVariable(userVariableName,emailDomain):
    try:
        global test_results
        textPart=generateRandomString(4)
        numberPart=generateRandomNumber(4)
        randomEmail=textPart+str(numberPart)+"@"+emailDomain
        global userVariables
        userVariables[userVariableName]=randomEmail
    except:
        test_results.write("[ERROR] Could not save the random email variable '"+userVariableName+"' with the domain '"+emailDomain+"'\n")

def setTimestampVariable(userVariableName,timestampFormat):
    try:
        if(timestampFormat=='t1'):
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
        if(timestampFormat=='t2'):
            timestamp=time.strftime("%Y-%m-%d")
        if(timestampFormat=='t3'):
            timestamp=time.strftime("%H:%M:%S")
        if(timestampFormat=='t4'):
            timestamp=time.strftime("%m-%d %H:%M:%S")
        global userVariables
        userVariables[userVariableName]=timestamp
    except:
        test_results.write("[ERROR] Could not save the random timestamp variable '"+userVariableName+"' with the format '"+timestampFormat+"'\n")

def extractVariableFromElement(userVariableName,LocateBy,elementLocatorName):
    try:
        valueFromElement=getValue(elementLocatorName,LocateBy)
        global userVariables
        userVariables[userVariableName]=valueFromElement
    except:
        test_results.write("[ERROR] Could not extract the variable '"+userVariableName+"' from the web element with locator '"+elementLocatorName+"'\n")

def getUserVariable(userVariableName):
    try:
        global userVariables
        return userVariables[userVariableName]
    except:
        test_results.write("[ERROR] Could not return the variable '"+userVariableName+ "'\n")

def goToLink(link):
    try:
        driver.get(link)
    except:
        test_results.write("[ERROR] Could not access the URL '"+link+ "'\n")
        if "http" not in link:
            test_results.write("The Full URL should be provided (http://www.example.com).\n")

def runTests():
    currentCase='TMS SSO Login'
    currentStep='Set Prod  Environment'
    enterVariable('$prodEnv','https://sso.groovv.com')
    currentCase='TMS SSO Login'
    currentStep='Set QA Environment'
    enterVariable('$qaEnv','https://sso.groovv.tst')
    currentCase='TMS SSO Login'
    currentStep='Set Prod Environmet'
    enterVariable('$prodEnv','https://sso.groovv.com')
    currentCase='TMS SSO Login'
    currentStep='Set Dev Environment'
    enterVariable('$devEnv','https://sso.groovv.dev')
    currentCase='TMS SSO Login'
    currentStep='Set Prod User'
    enterVariable('$prodUserName','XXXprod_user')
    currentCase='TMS SSO Login'
    currentStep='Set QA User'
    enterVariable('$qaUserName','XXXqa_user')
    currentCase='TMS SSO Login'
    currentStep='Go to SSO site'
    goToLink(userVariables['$prodEnv'])
    currentCase='TMS SSO Login'
    currentStep='Enter username'
    writeIn('Login_username',userVariables['$prodUserName'],'id')
    currentCase='TMS SSO Login'
    currentStep='Enter password'
    writeIn('Login_password','secure_pwd','id')
    currentCase='TMS SSO Login'
    currentStep='Click Login'
    clickOn('btn-primary','class_name')
    currentCase='TMS SSO Login'
    currentStep='Take Account Access screenshot'
    takeScreenshot(currentCase)
    currentCase='TMS SSO Login'
    currentStep='Assert Successful Login'
    assertUrlContains('https://sso.groovv.com/Admin/Index',currentCase)
    currentCase='Access Manager Users'
    currentStep='go to Admin users'
    clickOn('Manager Users','partial_link')
    currentCase='Access Manager Users'
    currentStep='Account Settings page screenshot of'
    takeScreenshot(currentCase)
    currentCase='Access Manager Users'
    currentStep='Print Results'
    echo('PrintTitle','0')
    currentCase='Access Manager Users'
    currentStep='Assert Account Users page'
    assertUrlContains('https://sso.groovv.com/Admin/Users',currentCase)
    currentCase='Create Subuser'
    currentStep='Add Subuser button click'
    clickOn('btn-groovv','class_name')
    currentCase='Create Subuser'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Confirm page Add User'
    assertTitle('Add User',currentCase)
    currentCase='Create Subuser'
    currentStep='Click on First Name label'
    clickOn('First Name','tag_name')
    currentCase='Create Subuser'
    currentStep='Set First Name variable'
    setRandomStringVariable('$firstName',5)
    currentCase='Create Subuser'
    currentStep='Enter First Name for Subuser'
    writeIn('firstName',userVariables['$firstName'],'id')
    currentCase='Create Subuser'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Click on Last Name label'
    clickOn('Last Name','tag_name')
    currentCase='Create Subuser'
    currentStep='Set Last Name for subuser'
    setRandomStringVariable('$lastName',4)
    currentCase='Create Subuser'
    currentStep='Enter Last Name for Subuser'
    writeIn('lastName',userVariables['$lastName'],'id')
    currentCase='Create Subuser'
    currentStep='Set Subuser email random value'
    setRandomEmailVariable('$subEmail','mailinator.com')
    currentCase='Create Subuser'
    currentStep='Click on Email label'
    clickOn('Email Address','tag_name')
    currentCase='Create Subuser'
    currentStep='Enter Email for Subuser'
    writeIn('emailAddress',userVariables['$subEmail'],'id')
    currentCase='Create Subuser'
    currentStep='Select Groovv Transactions Access level'
    pickOptionFromSelect('GroovvTransactionsAccountType','id','Master-Merchant')
    currentCase='Create Subuser'
    currentStep='Select Groovv POS Portal Profile'
    pickOptionFromSelect('GroovvPosPortalAccountType','id','Manager')
    currentCase='Create Subuser'
    currentStep='Screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Select Groovv POS Mobile Application Profile'
    pickOptionFromSelect('GroovvPosAppAccountType','id','Cashier')
    currentCase='Create Subuser'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Save'
    clickOn('div.col-md-3:nth-child(2) > input:nth-child(1)','css_selector')
    currentCase='Create Subuser'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Go to Manage users page'
    goToLink('https://sso.groovv.com/Admin/Users')
    currentCase='Create Subuser'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Create Subuser'
    currentStep='Confirm a user was created'
    assertElementIsPresent('.table > tbody:nth-child(2)','css_selector',currentCase)
    currentCase='Retrieve created subuser parameters'
    currentStep='Go to Users URL'
    goToLink('https://sso.groovv.com/Admin/Users')
    currentCase='Retrieve created subuser parameters'
    currentStep='Take Screenshot'
    takeScreenshot(currentCase)
    currentCase='Retrieve created subuser parameters'
    currentStep='Get USERNAME'
    extractVariableFromElement('$usernameFirstRow','xpath','//*[@id="content"]/div/div/div[2]/div/table/tbody/tr[1]/td[1]')
    currentCase='Retrieve created subuser parameters'
    currentStep='Get Name'
    extractVariableFromElement('$nameFirstRow','css_selector','.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    currentCase='Retrieve created subuser parameters'
    currentStep='Take Screenshot'
    takeScreenshot(currentCase)
    currentCase='Delete User'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Delete User'
    currentStep='Click edit button'
    clickOn('.table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(5) > a:nth-child(1)','css_selector')
    currentCase='Delete User'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    currentCase='Delete User'
    currentStep='Click delete'
    clickOn('del-user','id')
    currentCase='Delete User'
    currentStep='Do delete user'
    clickOn('div.btn-area:nth-child(3) > div:nth-child(2) > input:nth-child(1)','css_selector')
    currentCase='Delete User'
    currentStep='Wait'
    pauseForDuration(5)
    currentCase='Delete User'
    currentStep='screenshot'
    takeScreenshot(currentCase)
    # currentCase='Delete User'
    # currentStep='Confirm USERNAME is deleted'
    # assertNotMatchesValue('//*[@id="content"]/div/div/div[2]/div/table/tbody/tr[1]/td[1]','xpath',userVariables['$usernameFirstRow'],currentCase)
    currentCase='Delete User'
    currentStep='Confirm Name is deleted'
    assertNotMatchesValue('.table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)','css_selector',userVariables['$nameFirstRow'],currentCase)
def main():
    if __name__ == "__main__":
        createFolder()
        createFileForTestResults()
        startDriver()
        runTests()
        closeAlert("in_case_it_gets_stuck")
        driver.close()
        driver.quit()
        closeFileForTestResults()

if __name__ == "__main__":
    main()
