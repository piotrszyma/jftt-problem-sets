class PatternMatcher:
    def __init__(self, pattern, alphabet):
        self.__validate_init(pattern, alphabet)
        self.__pattern = pattern
        self.__alphabet = set(alphabet)
        self.__transition_func = None
        self.__matches = []
        self.__compute_transition_func()

    def __compute_transition_func(self):
        m = len(self.__pattern)
        self.__transition_func = [{l: 0 for l in self.__alphabet} for _ in range(len(self.__pattern) + 1)]

        for q in range(0, m + 1):
            for a in self.__alphabet:
                k = min(m + 1, q + 2)
                while True:
                    k -= 1
                    if (self.__pattern[:q] + a).endswith((self.__pattern[:k])):
                        break
                self.__transition_func[q][a] = k

    def matcher(self, input_text, show_result=False):
        self.__validate_matcher(input_text)
        self.__matches = []
        n = len(input_text)
        m = len(self.__pattern)
        q = 0
        for i in range(0, n):
            q = self.__transition_func[q][input_text[i]]
            if q == m:
                self.__matches.append(i - m + 1)

        if show_result:
            output = ("\n'{}' found {} times".format(self.__pattern, len(self.__matches)))
            output += ("\n{}".format(input_text))
            for l in self.__matches:
                output += ("\n" + ("·" * l + input_text[l:l + m]).ljust(n, "·"))
            print(output, end="")
        return self.__matches

    def __validate_init(self, pattern, alphabet):
        if not set(pattern).issubset(set(alphabet)):
            raise ValueError("Pattern must be a subset of alphabet\nSigns in pattern not in alphabet: {}".format(
                set(pattern) - set(alphabet)))

    def __validate_matcher(self, input_text):
        if not set(input_text).issubset(self.__alphabet):
            raise ValueError("Input text must be a subset of alphabet\nSigns in input text not in alphabet: {}".format(
                set(input_text) - set(self.__alphabet)))
