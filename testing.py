import unittest

class testing(unittest.TestCase):
  def test_playAgain(self):
    self.assertEqual("Y","Y")

  def test_playAgain2(self):
    self.assertEqual("N","N")

  def test_has_tie(self):
    self.assertEqual("R","R")
    self.assertEqual("S","S")
    self.assertEqual("P","P")


  def has_Winner(self):
    self.assetNotEqual("R","S")
    self.assertNotEqual("R","P")
    self.assertNotEqual("S","P")


  
  
  

if __name__ == '__main__':
  unittest.main()
