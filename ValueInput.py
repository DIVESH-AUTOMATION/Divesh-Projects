import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService, Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    UnexpectedAlertPresentException, NoSuchWindowException
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import CommonFiles.Config as con


class Valueinput:

    """ Browser selection """
    driver = webdriver.Firefox()

    """ Set Data """

    def Set_Popup_Data(self, by, locator, fieldData):
        """
        :param by: ID, XPATH
        :param locator: locator Value
        :param fieldData: To enter data in field
        """
        by = by.lower()

        # if bys == "ID":
        element = self.driver.find_element(by, locator)
        element.clear()
        time.sleep(1)
        count = 1
        while True:
            element.send_keys(fieldData)
            time.sleep(3)
            element.send_keys(Keys.TAB)
            time.sleep(2)
            value1 = element.get_attribute("value")
            if count == 3 or value1 != "":
                break
            count += 1
        # if bys == "XPATH":
        #     element = self.driver.find_element("xpath", Locator)
        #     element.clear()
        #     time.sleep(1)
        #     count = 1
        #     while True:
        #         element.send_keys(fieldData)
        #         time.sleep(3)
        #         element.send_keys(Keys.TAB)
        #         time.sleep(2)
        #         value1 = element.get_attribute("value")
        #         if count == 3 or value1 != "":
        #             break
        #         count += 1

    def Set_DropDown_Data(self, by, setby, Locator, fieldData):
        """by : XPATH , ID ,CSS etx \n
            setby : VT(Visibletext) , Value(value) , Index(index) \n
            Locator : actual XPath \n
            field data : data which needs to enter"""
        by = by.lower()
        if setby == "VT":
            self.Explicitwait(by, "CLICKABLE", Locator)
            select = Select(self.driver.find_element(by, Locator))
            select.select_by_visible_text(fieldData)
            time.sleep(2)
        if setby == "Value":
            self.Explicitwait(by, "CLICKABLE", Locator)
            select = Select(self.driver.find_element(by, Locator))
            select.select_by_value(fieldData)
            time.sleep(2)
        if setby == "Index":
            self.Explicitwait(by, "CLICKABLE", Locator)
            select = Select(self.driver.find_element(by, Locator))
            select.select_by_index(fieldData)
            time.sleep(2)
    def Set_Text_Data(self, by, Locator, fieldData):
        by = by.lower()
        # if bys == "ID":
        #
        time.sleep(2)

        elements=self.driver.find_element(by, Locator)
        elements.clear()
        elements.send_keys(fieldData)


        # if bys == "XPATH":
        #     self.Explicitwait("XPATH", "CLICKABLE", Locator)
        #     self.driver.find_element("xpath", Locator).send_keys(fieldData)


    # def Set_DropDown_Data(self, by, setby, locator, fieldData):
    #     """
    #     :param by: XPATH , ID ,CSS etc
    #     :param setby: VT(VisibleText) , Value(value) , Index(index)
    #     :param locator: locator Data
    #     :param fieldData: To enter data in field
    #     :param retries : number of retries in case of exceptions
    #     """
    #     retries = 3
    #     attempt = 0
    #     self.Explicitwait(by, "CLICKABLE", locator)
    #     while attempt < retries:
    #         try:
    #             select = Select(self.findElement(by, locator))
    #             match setby:
    #                 case "VT": select.select_by_visible_text(fieldData)
    #                 case "Value": select.select_by_value(fieldData)
    #                 case "Index": select.select_by_index(fieldData)
    #                 case _: raise ValueError("Invalid setby value provided. It must be 'VT', 'Value', or 'Index'.")
    #             time.sleep(1.5)
    #             return  # Exit the function if successful
    #
    #         except UnexpectedAlertPresentException as e:
    #             print(f"UnexpectedAlertPresentException exception found in locator {locator}")
    #             alert = self.driver.switch_to.alert
    #             print(f"Alert text: {alert.text}")
    #             alert.accept()  # or alert.dismiss()
    #         except Exception as e:
    #             pass
    #
    #         retries -= 1
    #         time.sleep(0.5)  # Wait before retrying

    def Set_Text_Data(self, by, locator, fieldData):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        :param fieldData: To enter data in field
        """
        by = by.lower()
        self.Explicitwait(by, "CLICKABLE", locator)
        element = self.findElement(by, locator)
        retries = 3
        attempt = 0
        while attempt < retries:
            try:
                # element.send_keys(Keys.CONTROL, "a")
                element.send_keys(fieldData)
                time.sleep(1.5)
                return  # Exit the function if successful

            except UnexpectedAlertPresentException as e:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception as e:
                self.driver.execute_script(f"arguments[0].value='{fieldData}';", element)

            retries -= 1
            time.sleep(0.5)  # Wait before retrying

    def Set_TextAndTAB_Data(self, by, locator, fieldData):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        :param fieldData: To enter data in field
        :return:
        """
        by = by.lower()
        #self.Explicitwait(by, "CLICKABLE", locator)
        retries = 3
        attempt = 0
        while attempt < retries:
            try:
                element = self.findElement(by, locator)
                element.clear()
                element.send_keys(Keys.CONTROL, "a")
                time.sleep(2)
                element.send_keys(fieldData)
                element.send_keys(Keys.TAB)
                time.sleep(1.5)
                return  # Exit the function if successful

            except UnexpectedAlertPresentException as e:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception as e:
                print(f"Not able to set data for locator : {locator}")

            retries -= 1
            time.sleep(0.5)  # Wait before retrying

    """ Get Data """

    def Get_CheckBox_Data(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        """
        by = by.lower()
        return self.findElement(by, locator).is_selected()

    def getAlert_Text(self):
        alertText = ""
        try:
            alertText = Alert(self.driver).text
        except:
            pass
        time.sleep(1)

        return alertText

    def Get_DropDown_Data(self, by, condition, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param condition: ATT, TEXT
        :param locator: locator Data
        """
        by = by.lower()
        retries = 3
        attempt = 0
        while attempt < retries:
            try:
                select = Select(self.findElement(by, locator))
                match condition:
                    case "ATT":
                        val = select.first_selected_option.get_attribute("value")
                    case "TEXT":
                        val = select.first_selected_option.text
                    case _: raise ValueError("Invalid condition value provided. It must be 'ATT' or 'TEXT'.")
                time.sleep(1.5)
                return val  # Return the value if successful

            except UnexpectedAlertPresentException as e:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception as e:
                pass

            attempt += 1
            time.sleep(0.5)  # Wait before retrying

    def GetTextByValue(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        :return:
        """
        by = by.lower()
        retries = 3
        attempt = 0
        while attempt < retries:
            try:
                value = self.findElement(by, locator).get_attribute("value")
                time.sleep(1.5)
                return value  # Return the value if successful

            except UnexpectedAlertPresentException as e:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception as e:
                pass
            attempt += 1
            time.sleep(0.5)  # Wait before retrying

    def GetTextByTextElement(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        """
        by = by.lower()
        retries = 3
        attempt = 0
        while attempt < retries:
            try:
                value = self.findElement(by, locator).text
                time.sleep(1.5)
                return value  # Return the value if successful

            except UnexpectedAlertPresentException as e:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception:
                print(f"Not able to fetch data from locator : {locator}")
            attempt += 1
            time.sleep(0.5)  # Wait before retrying

    @property
    def has_value(string):
        """
        :param : Checks if a string has a value (is not empty).
        Args:
            string: The string to check.
        Returns:
            True if the string has a value, False otherwise.
        """

        return bool(string)

    def getValue_And_DivideBy2(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator:locator Data
        """
        self.findElement(by.ID, locator).clear()
        fieldData = self.findElement(by.ID, locator).get_attribute("value")
        time.sleep(1)
        fieldData1 = int(fieldData) // 2
        self.findElement(by.ID, locator).send_keys(fieldData)
        self.findElement(by.ID, locator).send_keys(Keys.TAB)
        time.sleep(0.5)

    """ Clear, Click, DoubleClick """

    def Clear_Text_Data(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator:locator Data
        """
        retries = 3
        by = by.lower()
        element = self.findElement(by, locator)
        self.Explicitwait(by, "CLICKABLE", locator)
        while retries > 0:
            try:
                element.click()
                element.clear()
                if self.GetTextByValue(by, locator) != "":
                    try:
                        self.Clear_Text_Data(by, locator)
                    except:
                        pass
                time.sleep(1.5)
                return  # Exit if clear is successful

            except UnexpectedAlertPresentException:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception:
                pass
            retries -= 1
            time.sleep(0.5)  # Wait and retry

    def ClickOnElement(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Path
        """
        retries = 3
        by = by.lower()
        #self.Explicitwait(by, "CLICKABLE", locator)
        while retries > 0:
            try:
                self.findElement(by, locator).click()
                time.sleep(1)
                return  # Exit if click is successful

            except UnexpectedAlertPresentException:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                self.AlertAccept()
            except Exception as e:
                print(e.__cause__)

            retries -= 1
            time.sleep(0.5)  # Wait and retry

    def DoubleClickOnElement(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Path
        """
        retries = 3
        by = by.lower()
        # self.Explicitwait(by, "CLICKABLE", locator)
        action = ActionChains(self.driver)
        while retries > 0:
            try:
                source = self.findElement(by, locator)
                action.double_click(source).perform()
                time.sleep(1.5)
                return  # Exit if click is successful

            except UnexpectedAlertPresentException:
                print(f"UnexpectedAlertPresentException exception found in locator {locator}")
                alert = self.driver.switch_to.alert
                print(f"Alert text: {alert.text}")
                alert.accept()  # or alert.dismiss()
            except Exception:
                raise Exception


            retries -= 1
            time.sleep(0.5)  # Wait and retry

    ''' find_Elements/find_Element '''

    def findElements(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        """
        return self.driver.find_elements(by, locator)  # Exit if click is successful

    def findElement(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Data
        """
        return self.driver.find_element(by, locator)  # Exit if click is successful

    ''' isDisplay/isEnable '''

    def isEnabled(self, by, locator):
        by = by.lower()
        return self.findElement(by, locator).is_enabled()

    def isDisplayed(self, by, locator):
        by = by.lower()
        return self.findElement(by, locator).is_displayed()

    ''' Explicit Wait '''

    def Explicitwait(self, by, Condition, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param Condition: PRESENCE, CLICKABLE, VISIBILITY
        :param locator: locator Path
        """
        by = by.lower()
        waitSeconds = 25
        try:
            match Condition:
                case "PRESENCE": WebDriverWait(self.driver, waitSeconds).until(
                    EC.presence_of_element_located((by, locator)))
                case "CLICKABLE": WebDriverWait(self.driver, waitSeconds).until(
                    EC.element_to_be_clickable((by, locator)))
                case "VISIBILITY": WebDriverWait(self.driver, waitSeconds).until(
                    EC.visibility_of_element_located((by, locator)))
                case _: raise ValueError("Invalid setby value provided. It must be 'PRESENCE', 'CLICKABLE', or 'VISIBILITY'.")
        except:
            print(f"Explicitwait for {Condition} condition failed, Locator is : {locator}")


    ''' Alert Handled'''

    def AlertAccept(self):
        try:
            Alert(self.driver).accept()
        except:
            pass
        time.sleep(1.5)

    """ Window Switch """

    def Login_window_switch(self):
        """Closes the login window and Keep only Home-window"""
        size = len(self.driver.window_handles)
        while size <= 1:
            time.sleep(3)
            size = len(self.driver.window_handles)
            if size > 1:
                break
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.close()
        self.driver.switch_to.window(handles[1])
        self.driver.maximize_window()
        time.sleep(6)

    def New_window_switch(self):
        size = len(self.driver.window_handles)
        while size <= 1:
            time.sleep(3)
            size = len(self.driver.window_handles)
            if size > 1:
                break
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(6)

    def Previous_window_Switch(self, windowName):
        self.driver.switch_to.window(windowName)

    def getcurrrentwindow(self):
        return self.driver.current_window_handle

    def WindowClose(self):
        self.driver.close()
        time.sleep(1.5)

    def AllWindowClose(self):
       # self.driver.delete_all_cookies()
        self.driver.quit()
        print("--- All windows are closed and cookies are also cleared ---")
        time.sleep(8)

    def maximize_window(self):
        self.driver.maximize_window()
        time.sleep(2)

    def checkTabSwitch(self, by, locator):
        for attempt in range(2):
            try:
                # Store all window handles
                all_window_handles = self.driver.window_handles
                # Iterate through handles, excluding the current one (tab1)
                for handle in all_window_handles:
                    if handle != self.driver.current_window_handle:
                        # self.driver.switch_to.window(handle)  # Switch to potential tab2
                        # Verify if this is actually tab2
                        # Replace with a suitable check for your application
                        if self.driver.title == "Expected title of tab2":
                            break  # Tab2 found, exit the loop
                else:  # Tab2 not found in any other handle
                    if attempt == 0:
                        # If first attempt failed, try switching with Ctrl+Tab
                        self.ClickOnElement(by,locator)
                    else:
                        # If second attempt also fails, raise an exception
                        raise NoSuchWindowException("Tab2 not found")
                break  # Exit outer loop if tab2 found

            except NoSuchWindowException:
                if attempt == 1:
                    raise  # If second attempt fails, propagate the exception
                else:
                    pass  # Silently retry for the first attempt

    """ Interact with frame """

    def FrameswitchByID(self, framename):
        """
        :param framename: Frame ID
        """
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.frame_to_be_available_and_switch_to_it(('id', framename)))

    def frameSwitch(self, by, locator):
        """
        :param by: XPATH , ID ,CSS etc
        :param locator: locator Path
        """
        by = by.lower()
        iframe = self.findElement(by, locator)
        self.driver.switch_to.frame(iframe)
        time.sleep(1.5)

    def switchToParentFrame(self):
        self.driver.switch_to.parent_frame()
        time.sleep(1.5)

    def defaultcontent(self):
        self.driver.switch_to.default_content()
        time.sleep(1.5)

    def Switchtodefaultcontent(self):
        """
        :param driver: Pass Driver
        """
        return self.driver.switch_to.default_content()

    """ Assertions """

    def asserts(self, Expected, Actual, Field):
        """
        :param Expected: Expected value
        :param Actual: Actual Value
        :param Field: Field Name
        """
        try:
            if Actual != "":
                assert Expected == Actual
                print(f'Data "{Actual}" is tested and it is as Expected.')
            elif Actual == "":
                print(f"----- Actual value is blank ----- => ", Field)
        except:
            print("Failed, Expected Value => " + str(Expected) + " || Actual Value => " + str(Actual) + " || Field Name : " + Field)

    def Numeric_asserts(self, Expected, Actual, Field):
        """
        :param Expected: Expected value
        :param Actual: Actual Value
        :param Field: Field Name
        """
        try:
            assert Expected == Actual
        except Exception as e:
            print("Failed , Value is Not matching => " + Expected + " : " + Actual + " : " + Field)

    def assertsNotBlank(self, Actual, Field):
        try:
            assert Actual != ""
        except Exception as e:
            print("Failed , Value is Blank :- " + str(Actual) + " : " + Field)

    def dictionary_Extract(self, dictionary):
        count = 0
        print(len(dictionary))
        for x in range(len(dictionary)):
            print(f"dictionary[{count}]", dictionary[count])
            count = count + 1

    def Get_Radio_button_data(self,by,locator):
        by= by.lower()
        radiobutton=self.findElement(by,locator)
        radiobutton.is_selected()
        return radiobutton

