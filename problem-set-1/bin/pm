#!/usr/bin/env python
import sys
from matcher import PatternMatcher


def main():
    if len(sys.argv) < 3:
        print('Not enough parameters')
        print('To run type: {} [alphabet] [pattern] [...text]'.format(sys.argv[0]))
        exit(1)
    _, alphabet, pattern, *strings = sys.argv

    if len(set(alphabet)) != len(list(alphabet)):
        print("Found duplicates in alphabet {}.\nRemoving duplicates.\n".format(alphabet))
        alphabet = "".join(set(alphabet))

    print("Alphabet:\t{}".format(alphabet))
    print("Pattern:\t{}".format(pattern))

    try:
        pm = PatternMatcher(
            alphabet=alphabet,
            pattern=pattern
        )
    except ValueError as e:
        print("\nError for pattern matcher construction! Aborting program")
        print("{}\n".format(e))
        exit(1)

    for text in strings:
        try:
            pm.matcher(input_text=text, show_result=True)
        except ValueError as e:
            print("\nError for input text {}".format(text))
            print("{}\n".format(e))
    exit(0)


if __name__ == '__main__':
    main()
