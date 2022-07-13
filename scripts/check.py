#!/usr/bin/env python3
"""Print entries that have broken or absent accents.
"""
ACCENT = "\u0301"
VOWELS = "уеіїаояиюєУЕІАОЯИЮЄЇ"


def count_vowels(s):
    result = 0
    for x in VOWELS:
        result += s.count(x)
    return result


if __name__ == "__main__":
    for word in open("./stress.txt"):
        bad = False
        if count_vowels(word) < 2:
            continue

        pos = word.find(ACCENT)
        if pos <= 0:
            bad = True
        elif word[pos - 1] not in VOWELS:
            bad = True

        if bad:
            print(word.replace(ACCENT, "'"), end="")
