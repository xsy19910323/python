import unittest

from homework_0714.xsy_homework0714 import UntitledCase

suite = unittest.TestSuite()
tests = [UntitledCase('test_1_login'),UntitledCase('test_2_create_port'),UntitledCase('test_3_logout')]
suite.addTests(tests)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
