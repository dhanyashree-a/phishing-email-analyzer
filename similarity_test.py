from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


tests = [
    ("paypal", "paypa1"),
    ("microsoft", "micros0ft"),
    ("google", "g00gle"),
    ("amazon", "arnazon"),
    ("paypal", "pay"),
]

for original, suspicious in tests:
    score = similarity(original, suspicious)
    print(original, "vs", suspicious, "=", score)