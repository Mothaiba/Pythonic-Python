from unicodedata import normalize

s1 = "café"  # composed "e" with acute accent
s2 = "cafe\u0301"  # decomposed "e" and acute accent

print(s1, s2)  # output: café café
print(len(s1), len(s2))  # output: (4, 5)
print(s1 == s2)  # output: False
print(normalize("NFC", s1) == normalize("NFC", s2))  # output: True