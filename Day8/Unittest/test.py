import unittest
import change_text

class TestChangeText(unittest.TestCase):

    def test_uppercase(self):
        word = input("Please enter your name in capital letters: ")
        result = change_text.all_capitals(word)
        self.assertEqual(result, word.upper())

        #word = "Study"
        #result = change_text.all_capitals(word)
        #self.assertEqual(result, "STUDY")

if __name__ == '__main__':
    unittest.main()