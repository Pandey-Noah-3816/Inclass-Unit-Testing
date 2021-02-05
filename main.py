from calc import*
import unittest

class TestCase(unittest.TestCase):
  def test_case_1(self):
    self.assertEqual (calculator_app(2,2), [4,0,4,1.0])
  def test_case_2(self):
    self.assertEqual (calculator_app(2,0), [2,2,0,"zero div error"])
  def test_case_3(self):
    self.assertEqual (calculator_app("y",2), ["either a or b is not a num"])



if __name__ == '__main__':unittest.main()




