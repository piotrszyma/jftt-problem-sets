from matcher import PatternMatcher

pm = PatternMatcher(
    pattern="ababaca",
    alphabet=set("abc"))

pm.matcher("abababacaba")
