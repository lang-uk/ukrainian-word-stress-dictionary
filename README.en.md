# Dictionary of word stresses in the Ukrainian language

[Ukrainian](./README.md)

This [dictionary](stress.txt) lists word stresses for 2,931,496 word forms
and phrases in the Ukrainian language.

We use the [`COMBINING ACUTE ACCENT`](https://unicode-table.com/en/0301/)
(`U+0301`) sign to denote the stress. This sign comes __after__ the stressed
vowel. For example, the following characters form the word `ма́ма`:

```python
>>> chars = ['м', 'а', '\u0301', 'м', 'а']
>>> print("".join(chars))
ма́ма
```

Words that have multiple valid options of stressed syllables have multiple
accent signs in them (`по́ми́лка`).

This dictionary is based on ["Dictionaries of Ukraine"](https://lcorp.ulif.org.ua/dictua/) by ULIF.

