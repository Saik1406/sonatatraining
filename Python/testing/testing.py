import unittest
from Day_2.rock_paper_scissor1 import rock_paper_scissor
class AddTest(unittest.TestCase):
    def testAdd1(self):
        self.assertEqual('paper',rock_paper_scissor('rock','paper'))
    def testAdd2(self):
        self.assertEqual('scissor',rock_paper_scissor('paper','scissor'))
    def testAdd3(self):
        self.assertEqual('scissor',rock_paper_scissor('rock','scissor'))