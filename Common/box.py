# coding: utf-8
from Common.base import Logger, CsvHelper

import time
import contextlib
import unittest
import sys
from unittest import SkipTest
from unittest.suite import _DebugResult, _isnotsuite
from unittest.case import _ShouldStop
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import traceback


class BaseDriver(object):
    """
    基础driver类
    """
    _base_driver = None
    _by_char = None

    def __init__(self, browser_type='Chrome', by_char=","):
        self.logger = Logger()

        if browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif browser_type == 'IE':
            driver = webdriver.Ie
        else:
            driver = webdriver.PhantomJS

        try:
            self._base_driver = driver
            self._by_char = by_char
        except Exception:
            self.logger.error(NameError('Browser "%s" Not Found! ' % browser_type))

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    def click_by_text(self, selector, text):
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            elements = self._base_driver.find_elements(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")
        for e in elements:
            if e.text == text:
                e.click()
                break

    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        ActionChains(self._base_driver).double_click(el).perform()
        el.send_keys(text)

    def _locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            element = self._base_driver.find_element(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")
        return element

    def _convert_selector_to_locator(self, selector):
        """
        转换自定义的 selector 为 Selenium 支持的 locator
        :param selector: 定位字符，字符串类型，"i ,  xxx "   ,不能"i","xxx"
        "su"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char, 1)[0].strip()
        selector_value = selector.split(self._by_char, 1)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")

        return locator

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_element(selector)
        return el.get_attribute(attribute)

    def exist_ele(self, text):
        selector = 'x, //*[contains(text(), "%s")]' % text
        try:
            self._locate_element(selector)
            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def table_is_not_null(self):
        # css定位，找class包含card的div容器，然后找列表的body，判断它非空
        selector = 's, div[class*="card"] tbody'
        try:
            table = self._locate_element(selector).text
            if table:
                return True
            else:
                return False
        except Exception as e:
            self.logger.debug(e)
            return False

    def type_search_input(self, name, value):
        selector = 'x, //span[contains(text(), "%s")]/following-sibling::*' % name
        try:
            type = self._locate_element(selector).tag_name
            if type == 'input':
                self.type(selector, value)
            else:
                selector_li = 'x, //li[contains(text(), "%s")]' % value
                self.click(selector)
                self.forced_wait(0.5)
                self.click(selector_li)
        except Exception as e:
            self.logger.debug(e)
            return False

    def type_time(self, name, value):
        try:
            start_time = value.split('&')[0]
            end_time = value.split('&')[1]
            selector = 'x, //span[contains(text(), "%s")]/following-sibling::*' % name
            sel_start = 'x, //input[@placeholder="开始日期"]'
            sel_end = 'x, //input[@placeholder="结束日期"]'
            self.click(selector)
            self.forced_wait(0.5)
            self._locate_element(sel_start).__setattr__(value, start_time)
            self._locate_element(sel_end).__setattr__(value, end_time)
        except:
            self.logger.error()

    # 等待相关
    @staticmethod
    def forced_wait(seconds):
        """
        强制等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self._base_driver.implicitly_wait(seconds)

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self._convert_selector_to_locator(selector)

        WebDriverWait(self._base_driver, seconds).until(expected_conditions.presence_of_element_located(locator))

    # 浏览器相关
    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.maximize_window()

    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self._base_driver.get(url)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self._base_driver.quit()

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self._base_driver.current_url


class BasePage(object):
    """
    基础页面类
    """
    driver = None

    def __init__(self, driver: BaseDriver):
        self.logger = Logger()
        self.driver = driver

    def get_url(self):
        return self.driver.get_url()


class BaseCase(unittest.TestCase):
    images = None

    def __init__(self, method_name: str = ...):
        self.logger = Logger()
        super().__init__(method_name)

    def run(self, result=None):
        orig_result = result
        # 初始化result类，此类就是TestResult类或者其子类，用来记录用例的执行结果信息等
        if result is None:
            # 如果没有传入result对象自己实例化一个TestResult对象
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        self._resultForDoCleanups = result
        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        # 获取当前TestCase类里面实现的某一个具体的方法（以test开头的方法）
        # 判断TestCase类是否有被skip装饰，或类的testMethod方法有没有被skip装饰，如果有skip装饰，则直接跳过这个类或者这个方法不执行（包括后面tearDown也不会被执行）
        if (getattr(self.__class__, "__unittest_skip__", False) or
                getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, self, skip_why)  # 调用addSkip
            finally:
                result.stopTest(self)
            return

        expecting_failure_method = getattr(testMethod,
                                           "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self,
                                          "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method
        outcome = _Outcome(result)

        try:
            self._outcome = outcome

            with outcome.testPartExecutor(self):
                self.setUp()
            if outcome.success:
                outcome.expecting_failure = expecting_failure
                with outcome.testPartExecutor(self, isTest=True):
                    testMethod()
                outcome.expecting_failure = False
                # 尝试异常继续运行
                with outcome.testPartExecutor(self):
                    self.tearDown()

            for test, reason in outcome.skipped:
                self._addSkip(result, test, reason)
            self._feedErrorsToResult(result, outcome.errors)
            if outcome.success:
                if expecting_failure:
                    if outcome.expectedFailure:
                        self.snapshot()
                        self._addExpectedFailure(result, outcome.expectedFailure)
                    else:
                        self._addUnexpectedSuccess(result)
                else:
                    result.addSuccess(self)

            self.doCleanups()
            return result
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()

            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None

            # clear the outcome, no more needed
            self._outcome = None

    def snapshot(self):
        """
        截图
        :return:
        """
        self.images.append(self.base_driver.save_window_snapshot_by_io())

    def read_csv_as_dict(self, file_name):
        """
        读 CSV 作为 DICT 类型
        :type file_name: csv_case 文件路径 和名字
        :return:
        """
        return CsvHelper().read_data_as_dict(file_name)

    def shortDescription(self):
        """Returns a one-line description of the test, or None if no
        description has been provided.

        The default implementation of this method returns the first line of
        the specified test method's docstring.
        """
        doc = self._testMethodDoc
        return doc and doc.split("\n")[0].strip() or None
        # 用[1]报错，数组超出界限，报告是空的，改为[0]就可以了
        # return doc and doc.split("\n")[0].strip() or None

    def _addSkip(self, result, test_case, reason):
        addSkip = getattr(result, 'addSkip', None)
        if addSkip is not None:
            addSkip(test_case, reason)
        else:
            self.logger.warning("TestResult has no addSkip method, skips not reported")
            result.addSuccess(test_case)


class BaseSuite(unittest.TestSuite):
    """
    A test suite is a composite test consisting of a number of TestCases.
    For use, create an instance of TestSuite, then add test case instances.
    When all tests have been added, the suite can be passed to a test runner,
    such as TextTestRunner. It will run the individual test cases in the order in which they were added,
    aggregating the results. When subclassing, do not forget to call the base class constructor.
    """
    def run(self, result, debug=False):
        top_level = False
        # getattr()函数，返回result对象的_testRunEntered属性值，默认值是False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = top_level = True

        for index, test in enumerate(self):
            if result.shouldStop:
                break

            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if (getattr(test.__class__, '_classSetupFailed', False) or
                        getattr(result, '_moduleSetUpFailed', False)):
                    continue

            if not debug:
                test(result)
            else:
                test.debug()

            if self._cleanup:
                self._removeTestAtIndex(index)

        if top_level:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result

    def debug(self):
        """Run the tests without collecting errors in a TestResult"""
        debug = _DebugResult()
        self.run(debug, True)

    def add_test(self, test):
        """
        添加单个测试
        :param test: 测试用例的类实例化的对象
        :return:
        """
        self.addTest(test)

    def add_tests(self, tests):
        """
        添加多个测试
        :param tests:
        :return:
        """
        self.addTests(tests)


class _Outcome(object):
    def __init__(self, result=None):
        self.expecting_failure = False
        self.result = result
        self.result_supports_subtests = hasattr(result, "addSubTest")
        self.success = True
        self.skipped = []
        self.expectedFailure = None
        self.errors = []

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, isTest=False):
        old_success = self.success
        self.success = True
        try:
            yield
        except KeyboardInterrupt:
            raise
        except SkipTest as e:
            self.success = False
            self.skipped.append((test_case, str(e)))
        except _ShouldStop:
            pass
        except:
            exc_info = sys.exc_info()
            if self.expecting_failure:
                self.expectedFailure = exc_info
            else:
                self.success = False
                # test_case.images.append(test_case.base_driver.save_window_snapshot_by_io())

                self.errors.append((test_case, exc_info))
            # explicitly break a reference cycle:
            # exc_info -> frame -> exc_info
            exc_info = None
        else:
            if self.result_supports_subtests and self.success:
                self.errors.append((test_case, None))
        finally:
            self.success = self.success and old_success
