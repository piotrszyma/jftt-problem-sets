from lexer_test_case import LexerTestCase


class TestSecondSolution(LexerTestCase):
    FILE_LOCATION = '/task-2/lexer.o'
    maxDiff = None

    def test_should_remove_one_line_comment(self):
        text = """#include <stdio.h>
// this is a comment
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""
        response = self.runParser(text)
        self.assertEqual(response, expected_result)

    def test_should_remove_escaped_two_lines_comment(self):
        text = """#include <stdio.h>
// this is a comment \
lorem ipsum
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""
        response = self.runParser(text)
        self.assertEqual(response, expected_result)

        #

    def test_should_remove_multiline_comment(self):
        text = """#include <stdio.h>
/* this is a multiline comment
 * lorem ipsum dolor es
 */
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""

        response = self.runParser(text)
        self.assertEqual(response, expected_result)

    def test_should_remove_comment(self):
        text = """#include <stdio.h> //this is a comment \
this is another line \
and another
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""

        response = self.runParser(text)
        self.assertEqual(response, expected_result)

    def test_should_remove_comment_at_end(self):
        text = """#include <stdio.h> //this is a comment
/* this is another line */
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""

        response = self.runParser(text)
        self.assertEqual(response, expected_result)

        text = """#include <stdio.h> //this is a comment
  /// Komentarz dokumentacyjny \
  ciag dalszy jednolinijkowego komentarza
int main(void) {
    return 0;
}
// Komentarz jednolinijkowy\
  i jego ciÄg dalszy\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  i dalszy */
"""


        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""

        response = self.runParser(text)
        self.assertEqual(response, expected_result)


    def test_should_print_string(self):
        text = """
cout << "Lorem ipsum //" << endl;
"""
        expected_result = b"""
cout << "Lorem ipsum //" << endl;
"""
        response = self.runParser(text)
        self.assertEqual(response, expected_result)
    def test_should_not_remove(self):
        text = """int main() {
    cout << "Pulapka \" \
           // ma \
           /* ma */ \
           " << endl;
}"""
        expected_result = b"""int main() {
    cout << "Pulapka \" \
           // ma \
           /* ma */ \
           " << endl;
}"""
        response = self.runParser(text)
        self.assertEqual(response, expected_result)

        text = """cout << /*Proba*/"Zabawa \" // ala i kot " << endl;
"""

    def test_should_remove_comment_from_inside_func(self):
        text = """#include<iostream>

/** Maly przyklad programu
 *
 *  autor Maciej Gebala
 */

// /*
using namespace std;
// */

int main()
{
  /// Komentarz dokumentacyjny \
  ciag dalszy jednolinijkowego komentarza
  int i = 5;
  // Komentarz jednolinijkowy\
  i jego ciÄg dalszy\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  i dalszy */
  cout << "Jakis program" << endl; // ;
  // A tutaj taki komentarz \
  cout << "Poczatek komentarza /*" << endl; // ala
  cout << "Koniec komentarza */ "<< endl; // kot
  cout << "Komentarz /* ala */" << endl;
  cout << "Komentarz // kot " << endl;
  cout << "Zabawa \" // ala i kot " << endl;
  cout << "Pulapka \" \
           // ma \
           /* ma */ \
           " << endl;
 cout << /*Proba*/"Zabawa \" // ala i kot " << endl;
 printf("Zabawa \" // ala i kot ");
}

"""

        expected_result = b"""#include<iostream>


using namespace std;

int main()
{
  int i = 5;
  cout << "Jakis program" << endl; // ;
  cout << "Koniec komentarza */ "<< endl; // kot
  cout << "Komentarz /* ala */" << endl;
  cout << "Komentarz // kot " << endl;
  cout << "Zabawa \" // ala i kot " << endl;
  cout << "Pulapka \" \
           // ma \
           /* ma */ \
           " << endl;
 cout << "Zabawa \" // ala i kot " << endl;
 printf("Zabawa \" // ala i kot ");
}"""

        response = self.runParser(text)
        self.assertEqual(response, expected_result)
