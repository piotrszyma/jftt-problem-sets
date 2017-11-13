from lexer_test_case import LexerTestCase


class TestFirstSolution(LexerTestCase):
    FILE_LOCATION = '/task-1/lexer.o'

    def test_start_with_tab_or_space(self):
        response = self.runParser("     aaaa bbb\n")
        self.assertEqual(response, b'aaaa bbb\n1 2')

        response = self.runParser("     aaaa \t\t \t\tbbb\n")
        self.assertEqual(response, b'aaaa bbb\n1 2')

    def test_end_with_tab_or_space(self):
        response = self.runParser("     aaaa bbb       \t\t\n")
        self.assertEqual(response, b'aaaa bbb\n1 2')

        response = self.runParser("     aaaa \t\t \t\tbbb\t\t\t   \t\n")
        self.assertEqual(response, b'aaaa bbb\n1 2')

    def test_start_and_end(self):
        response = self.runParser("   aaaa     \n")
        self.assertEqual(response, b'aaaa\n1 1')

        response = self.runParser("   aaaa     \n   aaa aaaa   \n")
        self.assertEqual(response, b'aaaaaaa aaaa\n2 3')

    def test_white_spaces(self):
        response = self.runParser("\f\f\f\r\r\ta\t\t\t\f\n")
        self.assertEqual(response, b'a\n1 1')

    def test_number_of_words_and_lines(self):
        response = self.runParser("aaa\nbbb\n")
        self.assertEqual(response, b'aaabbb\n2 2')

        response = self.runParser("aaa\n")
        self.assertEqual(response, b'aaa\n1 1')

        response = self.runParser("aaaa\n\n\nbbb\n")
        self.assertEqual(response, b'aaaabbb\n4 2')

    def test_blank_symbols(self):
        response = self.runParser("aaaa  \n\n\nbbb\n")
        self.assertEqual(response, b'aaaabbb\n4 2')

        response = self.runParser("aaaa \t\t \n\n\nbbb\n")
        self.assertEqual(response, b'aaaabbb\n4 2')

    def test_important_cases(self):
        response = self.runParser("")
        self.assertEqual(response, b'\n0 0')

        response = self.runParser("\n")
        self.assertEqual(response, b'\n1 0')

        response = self.runParser("  \t\n")
        self.assertEqual(response, b'\n1 0')

        response = self.runParser("  \n")
        self.assertEqual(response, b'\n1 0')

    def test_mixes(self):
        response = self.runParser("    aaa \t  x  \n   bbb \t\t   \naaaa \n")
        self.assertEqual(response, b'aaa xbbbaaaa\n3 4')

    def test_empty(self):
        response = self.runParser("")
        self.assertEqual(response, b'\n0 0')

    def test_not_empty(self):
        response = self.runParser(" ")
        self.assertEqual(response, b'\n1 0')
