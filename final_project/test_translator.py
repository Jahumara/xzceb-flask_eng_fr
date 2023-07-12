import unittest
from translator.py import translate_english_to_french, translate_french_to_english

class TranslationTests(unittest.TestCase):
  # This test asserts that the translation from English to French is equal to the expected translation.
    def test_translate_english_to_french_equal(self):
        result = translate_english_to_french("Hello")
        expected = "Bonjour"
        self.assertEqual(result, expected)
      
  #This test asserts that the translation from English to French is not equal to a different translation.
    def test_translate_english_to_french_not_equal(self):
        result = translate_english_to_french("Hello")
        expected = "Salut"
        self.assertNotEqual(result, expected)

  #This test asserts that the translation from French to English is equal to the expected translation.
    def test_translate_french_to_english_equal(self):
        result = translate_french_to_english("Bonjour")
        expected = "Hello"
        self.assertEqual(result, expected)
      
  #This test asserts that the translation from French to English is not equal to a different translation.
    def test_translate_french_to_english_not_equal(self):
        result = translate_french_to_english("Bonjour")
        expected = "Salut"
        self.assertNotEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

#Run coding standards check against the functions above.
pip install pylint
pylint test_translator.py

