from lexer_test_case import LexerTestCase


class TestThirdSolution(LexerTestCase):
    FILE_LOCATION = '/task-3/lexer.o'

    def test_should_remove_one_line_comment(self):
        response = self.runParser("abcd\n% whatever\nabcd")
        self.assertEqual(response, b'abcd\nabcd')

        response = self.runParser("abcd\n% % \% %\%whatever\nabcd")
        self.assertEqual(response, b'abcd\nabcd')

    def test_should_remove_comment_at_end(self):
        response = self.runParser("abcd % whatever\nabcd")
        self.assertEqual(response, b'abcd \nabcd')

        response = self.runParser("abcd % \%\%%\% whatever\nabcd")
        self.assertEqual(response, b'abcd \nabcd')

    def test_should_return_all_if_no_comments(self):
        response = self.runParser("abcd  \n abcdef\n")
        self.assertEqual(response, b'abcd  \n abcdef\n')

    def test_should_not_interpreted_escaped_as_comment(self):
        response = self.runParser("\%  \n abcdef\n")
        self.assertEqual(response, b'\%  \n abcdef\n')

        response = self.runParser("\%%comment  \n abcdef\n")
        self.assertEqual(response, b'\%\n abcdef\n')

        response = self.runParser("\%%%%%%comment  \n abcdef\n")
        self.assertEqual(response, b'\%\n abcdef\n')

    def test_should_interpret_not_escaped(self):
        response = self.runParser("\\%  \n abcdef\n")
        self.assertEqual(response, b'\\%  \n abcdef\n')