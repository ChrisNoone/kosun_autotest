# coding: utf-8

from Common.box import *
from TestCase import *
from Common import HTMLTestHelper


class Runner(object):
    @staticmethod
    def run_test():
        suite = BaseSuite()
        tests = [test_login.LoginTest("test_login"), test_home.HomeTest("test_system_a"), test_home.HomeTest("test_user_a")]
        suite.add_tests(tests)
        report_time = time.strftime("%Y%m%d%H", time.localtime())
        report_file = "./TestReport/fusion_automate_report_%s.html" % report_time
        runner = HTMLTestHelper.HTMLTestRunner(file_name=report_file, verbosity=2)
        runner.run(suite)


if __name__ == "__main__":
    Runner().run_test()
