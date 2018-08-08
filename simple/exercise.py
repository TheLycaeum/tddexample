def panagram(s):
    s = s.lower()
    a = set(s.replace(" ", ""))
    return len(a) == 26

