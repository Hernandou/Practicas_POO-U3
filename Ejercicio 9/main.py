from ClassPalindromo import Palindromo
import unittest


class TestPalindromos(unittest.TestCase):

    def setUp(self):
        self.__palindromo = Palindromo.Palindromo('')

    def Testvacio(self):
        self.__palindromo.setPalabra('')
        self.assertFalse(self.__palindromo.nuevoesPalindromo())

    def TestPalindromopar(self):
        self.__palindromo.setPalabra('papa')
        self.assertTrue(self.__palindromo.nuevoesPalindromo)

    def TestPalindromoimpar(self):
        self.__palindromo.setPalabra('kayak')
        self.assertTrue(self.__palindromo.nuevoesPalindromo)

    def TestNoPalindromopar(self):
        self.__palindromo.setPalabra('papa')
        self.assertFalse(self.__palindromo.nuevoesPalindromo())

    def TestNoPalindromoimpar(self):
        self.__palindromo.setPalabra('capaz')
        self.assertFalse(self.__palindromo.nuevoesPalindromo())


if __name__ == "__main__":
    unittest.main()
