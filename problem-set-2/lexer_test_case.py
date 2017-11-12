import unittest
from subprocess import Popen, PIPE

import os


class LexerTestCase(unittest.TestCase):
    FILE_LOCATION = ''
    CWD = os.getcwd()[:-6]

    def runParser(self, parser_input):
        p = Popen(['{cwd}{file}'.format(cwd=self.CWD, file=self.FILE_LOCATION)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(bytes(parser_input, "utf-8"))
        return output
