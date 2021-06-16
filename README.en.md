# Dictionary of word stess in the Ukrainian language

[Ukrainian](./README.md)

This [dictionary](stress.txt) lists word stress for 2,770,680 of word forms
in the Ukrainian language.

We use 

We use the [`COMBINING ACUTE ACCENT`](https://unicode-table.com/en/0301/)
(`U+0301`) sign for denoting stress. This sign comes __after__ the stressed
vowel. For example, the following characters form the word `ма́ма`:

```python
>>> chars = ['м', 'а', '\u0301', 'м', 'а']
>>> print("".join(chars))
ма́ма
```

A word that have multiple valid options of stressed syllabuls, have multiple
accent signs in them (`по́ми́лка`).

This dictionary is based on ["Dictionaries of
Ukraine"](https://lcorp.ulif.org.ua/dictua/) by ULIF.
