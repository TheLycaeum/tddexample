def panagram(s):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True

