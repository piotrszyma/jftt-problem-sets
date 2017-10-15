import unittest
from matcher import PatternMatcher


class MatcherTest(unittest.TestCase):
    maxDiff = None

    def test_transition_func_generator_generates_proper_transitions(self):
        pm = PatternMatcher(
            pattern="ababaca",
            alphabet="abc"
        )

        states = pm._PatternMatcher__transition_func
        expected_states = [
            {'a': 1, 'b': 0, 'c': 0},  # 0
            {'a': 1, 'b': 2, 'c': 0},  # 1
            {'a': 3, 'b': 0, 'c': 0},  # 2
            {'a': 1, 'b': 4, 'c': 0},  # 3
            {'a': 5, 'b': 0, 'c': 0},  # 4
            {'a': 1, 'b': 4, 'c': 6},  # 5
            {'a': 7, 'b': 0, 'c': 0},  # 6
            {'a': 1, 'b': 2, 'c': 0}  # 7
        ]

        self.assertListEqual(states, expected_states)

    def test_should_find_matches_properly(self):
        pm = PatternMatcher(
            pattern="abc",
            alphabet="abcd"
        )

        self.assertEqual(pm.matcher("ac"), [])
        self.assertEqual(pm.matcher("abcdabcd"), [0, 4])
        self.assertEqual(pm.matcher("abcdabcddddddddabc"), [0, 4, 15])

        pm = PatternMatcher(
            pattern="a",
            alphabet="abcd"
        )

        self.assertEqual(pm.matcher("aaaa"), [0, 1, 2, 3])
        self.assertEqual(pm.matcher("bcdd"), [])

