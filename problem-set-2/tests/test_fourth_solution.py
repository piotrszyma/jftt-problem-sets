from lexer_test_case import LexerTestCase


class TestFourthSolution(LexerTestCase):
    FILE_LOCATION = '/task-4/lexer.o'

    def test_should_pass_examples(self):
        response = self.runParser("4 3 /\n")
        self.assertEqual(response, b'\n= 1')

        # response = self.runParser("3 4 /\n")
        # self.assertEqual(response, b'\n= 0')
        #
        # response = self.runParser("4 3 %\n")
        # self.assertEqual(response, b'\n= 1')
        #
        # response = self.runParser("2 3 +\n")
        # self.assertEqual(response, b'\n= 5')
        #
        # response = self.runParser("2 3 -\n")
        # self.assertEqual(response, b'\n= -1')
        #
        # response = self.runParser("2 3+-4*\n")
        # self.assertEqual(response, b'\n= -20')
        #
        # response = self.runParser("1 2 3 4 + * -\n")
        # self.assertEqual(response, b'\n= -13')
        #
        # response = self.runParser("-1 2 -3 4 + * -\n")
        # self.assertEqual(response, b'\n= -3')
        #
        # response = self.runParser("8 -7 6 -5 4 * -3 % / - +\n")
        # self.assertEqual(response, b'= 4')

        # response = self.runParser("2 3 2 ^ ^\n")
        # self.assertEqual(response, b'= 512')
        #
        # response = self.runParser("2 3+*\n")
        # self.assertEqual(response, b'Error: not enough arguments')
        #
        # response = self.runParser("2 3 4 +\n")
        # self.assertEqual(response, b'Error: not enough operators')
        #
        # response = self.runParser("2.4 3+\n")
        # self.assertEqual(response, b'Error: unknown symbol "."')
        #
        #
