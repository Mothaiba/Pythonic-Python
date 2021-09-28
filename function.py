import unicodedata
import functools

nfc = functools.partial(unicodedata.normalize, "NFC")

s = "cafe\u0301"
print(nfc(s))  # output: café
print(nfc(s) == unicodedata.normalize("NFC", s))  # output: True
