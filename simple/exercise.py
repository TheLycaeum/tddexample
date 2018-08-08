def panagram(s):
    a = set(s.replace(" ", ""))
    return len(a) == 26

