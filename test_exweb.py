from unittest import TestCase
from nose.tools import ok_, eq_
from exweb import bmi

class TestCaseExweb(TestCase):
    def test_bmi(self):
        eq_(bmi(180.0,72.5), 22.4)
        eq_(bmi(162.5,62.5), 23.7)
