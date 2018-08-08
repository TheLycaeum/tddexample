def panagram(s):
    s = s.lower()
    for i in "!?.;: ,":
        s = s.replace(i,"")
    a = set(s)
    return len(a) == 26

