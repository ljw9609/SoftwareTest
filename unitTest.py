import unittest
import os
from myCalendar import *


class UnitTest(unittest.TestCase):
    def setUp(self):
        print('\nCase before')
        pass

    # 语句覆盖100%，分支覆盖100%
    def test_leapyear(self):
        print('test leapyear start')

        # case1
        actual1 = leapyear(1997)
        expect1 = False
        self.assertEqual(expect1, actual1)

        # case2
        actual2 = leapyear(2008)
        expect2 = True
        self.assertEqual(expect2, actual2)

        # case3
        actual3 = leapyear(2100)
        expect3 = False
        self.assertEqual(expect3, actual3)

        # case4
        actual4 = leapyear(2000)
        expect4 = True
        self.assertEqual(expect4, actual4)

        print('test leapyear finish')

    # 语句覆盖100%
    def test_allLeapYears(self):
        print('test allLeapYears start')

        actual1 = allLeapyears(2008)
        expect1 = 486
        self.assertEqual(expect1, actual1)

        print('test allLeapYears finish')

    # 语句覆盖100%
    def test_firstDay(self):
        print('test firstDay start')

        actual1 = firstDay(2018)
        expect1 = 1
        self.assertEqual(expect1, actual1)

        print('test firstDay finish')

    # 语句覆盖100%，分支覆盖100%
    def test_datesOfMonth(self):
        print('test datesOfMonth start')

        # case1
        actual1 = datesOfMonth(2008, 1)
        expect1 = 31
        self.assertEqual(expect1, actual1)

        # case2
        actual2 = datesOfMonth(2008, 3)
        expect2 = 31
        self.assertEqual(expect2, actual2)

        # case3
        actual3 = datesOfMonth(2008, 4)
        expect3 = 30
        self.assertEqual(expect3, actual3)

        # case4
        actual4 = datesOfMonth(2008, 5)
        expect4 = 31
        self.assertEqual(expect4, actual4)

        # case5
        actual5 = datesOfMonth(2008, 6)
        expect5 = 30
        self.assertEqual(expect5, actual5)

        # case6
        actual6 = datesOfMonth(2008, 7)
        expect6 = 31
        self.assertEqual(expect6, actual6)

        # case7
        actual7 = datesOfMonth(2008, 8)
        expect7 = 31
        self.assertEqual(expect7, actual7)

        # case8
        actual8 = datesOfMonth(2008, 9)
        expect8 = 30
        self.assertEqual(expect8, actual8)

        # case9
        actual9 = datesOfMonth(2008, 10)
        expect9 = 31
        self.assertEqual(expect9, actual9)

        # case10
        actual10 = datesOfMonth(2008, 11)
        expect10 = 30
        self.assertEqual(expect10, actual10)

        # case11
        actual11 = datesOfMonth(2008, 12)
        expect11 = 31
        self.assertEqual(expect11, actual11)

        # case12
        actual12 = datesOfMonth(2008, 2)
        expect12 = 29
        self.assertEqual(expect12, actual12)

        # case13
        actual13 = datesOfMonth(2007, 2)
        expect13 = 28
        self.assertEqual(expect13, actual13)

        print('test datesOfMonth finish')

    # 语句覆盖97%，分支覆盖91.67%
    def test_firstDayOfMonth(self):
        print('test firstDayOfMonth start')

        # case1
        actual1 = firstDayOfMonth(2008, 1)
        expect1 = 2
        self.assertEqual(expect1, actual1)

        # case2
        actual2 = firstDayOfMonth(2008, 12)
        expect2 = 1
        self.assertEqual(expect2, actual2)

        # case3
        actual3 = firstDayOfMonth(2007, 12)
        expect3 = 6
        self.assertEqual(expect3, actual3)

        print('test firstDayOfMonth finish')

    # 语句覆盖100%，分支覆盖100%
    def test_layout(self):
        print('test layout start')

        # case1
        actual1 = layout(2008, 1)
        expect1 = eval("[['   ', '   ', '   ', 'Jan', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect1, actual1)

        # case2
        actual2 = layout(2008, 2)
        expect2 = eval("[['   ', '   ', '   ', 'Feb', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', '', '', 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect2, actual2)

        # case3
        actual3 = layout(2008, 3)
        expect3 = eval("[['   ', '   ', '   ', 'Mar', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', '', '', '', 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, '', '', '', '', '']]")
        self.assertEqual(expect3, actual3)

        # case4
        actual4 = layout(2008, 4)
        expect4 = eval("[['   ', '   ', '   ', 'Apr', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, '', '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect4, actual4)

        # case5
        actual5 = layout(2008, 5)
        expect5 = eval("[['   ', '   ', '   ', 'May', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', '', 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect5, actual5)

        # case6
        actual6 = layout(2008, 6)
        expect6 = eval("[['   ', '   ', '   ', 'Jun', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, '', '', '', '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect6, actual6)

        # case7
        actual7 = layout(2008, 7)
        expect7 = eval("[['   ', '   ', '   ', 'Jul', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect7, actual7)

        # case8
        actual8 = layout(2008, 8)
        expect8 = eval("[['   ', '   ', '   ', 'Aug', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', '', '', 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30], [31, '', '', '', '', '', '']]")
        self.assertEqual(expect8, actual8)

        # case9
        actual9 = layout(2008, 9)
        expect9 = eval("[['   ', '   ', '   ', 'Sep', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, '', '', '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect9, actual9)

        # case10
        actual10 = layout(2008, 10)
        expect10 = eval("[['   ', '   ', '   ', 'Oct', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect10, actual10)

        # case11
        actual11 = layout(2008, 11)
        expect11 = eval("[['   ', '   ', '   ', 'Nov', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', '', '', '', '', '', 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, '', '', '', '', '', '']]")
        self.assertEqual(expect11, actual11)

        # case12
        actual12 = layout(2008, 12)
        expect12 = eval("[['   ', '   ', '   ', 'Dec', '   ', '   ', '   '], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], ['', 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, '', '', ''], ['', '', '', '', '', '', '']]")
        self.assertEqual(expect12, actual12)
        print('test layout finish')

    def tearDown(self):
        print('Case after')
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UnitTest("test_leapyear"))
    suite.addTest(UnitTest('test_allLeapYears'))
    suite.addTest(UnitTest('test_firstDay'))
    suite.addTest(UnitTest('test_datesOfMonth'))
    suite.addTest(UnitTest('test_firstDayOfMonth'))
    suite.addTest(UnitTest('test_layout'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

