from lexer_test_case import LexerTestCase


class TestFourthSolution(LexerTestCase):
    FILE_LOCATION = '/task-4/lexer.o'

    def test_should_pass_examples(self):
        response = self.runParser("4 3 /\n")
        self.assertEqual(response, b'= 1\n')

        response = self.runParser("3 4 /\n")
        self.assertEqual(response, b'= 0\n')

        response = self.runParser("4 3 %\n")
        self.assertEqual(response, b'= 1\n')

        response = self.runParser("2 3 +\n")
        self.assertEqual(response, b'= 5\n')

        response = self.runParser("2 3 -\n")
        self.assertEqual(response, b'= -1\n')

        response = self.runParser("2 3+-4*\n")
        self.assertEqual(response, b'= -20\n')

        response = self.runParser("1 2 3 4 + * -\n")
        self.assertEqual(response, b'= -13\n')

        response = self.runParser("-1 2 -3 4 + * -\n")
        self.assertEqual(response, b'= -3\n')

        response = self.runParser("8 -7 6 -5 4 * -3 % / - +\n")
        self.assertEqual(response, b'= 4\n')

        response = self.runParser("2 3 2 ^ ^\n")
        self.assertEqual(response, b'= 512\n')

        response = self.runParser("2 3+*\n")
        self.assertEqual(response, b'Error: not enough arguments\n')

        response = self.runParser("2 3 4 +\n")
        self.assertEqual(response, b'Error: not enough operators\n')

        response = self.runParser("2.4 3+\n")
        self.assertEqual(response, b'Error: unknown symbol "."\n')

        #
