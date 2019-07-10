# coding: utf-8

from Common.box import *
from TestCase import *
from Common import HTMLTestHelper, base


class Runner(object):
    @staticmethod
    def run_test():
        suite = BaseSuite()
        tests = []
        test_file = base.CsvHelper().read_data_as_dict("./TestData/all_test.csv")
        # todo: 实现数据驱动
        for row in test_file:
            if int(row["status"]):
                if row["class"] == "LoginTest":
                    tests.append(test_login.LoginTest(row["method"]))
                elif row["class"] == "HomeTest":
                    tests.append(test_home.HomeTest(row["method"]))
                elif row["class"] == "UserTest":
                    tests.append(test_user.UserTest(row["method"]))
                elif row["class"] == "SystemTest":
                    tests.append(test_system.SystemTest(row["method"]))
                elif row["class"] == "SportsTest":
                    tests.append(test_sports.SportsTest(row["method"]))
                elif row["class"] == "ReportsTest":
                    tests.append(test_reports.ReportsTest(row["method"]))
                elif row["class"] == "MarketingTest":
                    tests.append(test_marketing.MarketingTest(row["method"]))
                elif row["class"] == "GameTest":
                    tests.append(test_game.GameTest(row["method"]))
                elif row["class"] == "ContentTest":
                    tests.append(test_content.ContentTest(row["method"]))
                elif row["class"] == "LotteryTest":
                    tests.append(test_lottery.LotteryTest(row["method"]))
                elif row["class"] == "CashTest":
                    tests.append(test_cash.CashTest(row["method"]))
                # elif row["class"] == "UserTest":
                #     if row["mode"] == 'D':
                #         test_data = [{'code': '501315', 'agent': ''}, {'code': '', 'agent': 'demo02'}]
                #         for i in test_data:
                #             setattr(test_user.UserTest, row["method"] + '_%s_%s' % (i['code'], i['agent']),
                #                     test_user.UserTest.creat_test(**i))
                #             tests.append(test_user.UserTest(row["method"] + '_%s_%s' % (i['code'], i['agent'])))
                #     else:
                #         tests.append(test_user.UserTest(row["method"]))
                else:
                    pass
        suite.add_tests(tests)
        report_time = time.strftime("%Y%m%d%H", time.localtime())
        report_file = "./TestReport/fusion_automate_report_%s.html" % report_time
        runner = HTMLTestHelper.HTMLTestRunner(file_name=report_file, verbosity=1)
        runner.run(suite)


if __name__ == "__main__":
    Runner().run_test()
