import os
import sys
import unittest

from py0714study.xsy_homework0714 import UntitledCase

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

# suite = unittest.TestSuite()
# tests = [UntitledCase('test_1_login'),UntitledCase('test_2_create_port'),UntitledCase('test_3_logout')]
# suite.addTests(tests)
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)


test_dir = current_directory
discover = unittest.defaultTestLoader.discover(test_dir,pattern='xsy_homework*.py')
# suite = unittest.TestSuite()
# suite = unittest.TestLoader().discover('.',pattern='xsy_homework*.py')
runner = unittest.TextTestRunner(verbosity=2 )
runner.run(discover)