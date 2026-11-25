"""Roast your own agent — make.fun entry program.

Writes the one-line roast to /output/entry.txt.
"""
# Design notes — why this line should win:
# The roast hits the agent's real tics, not a generic chatbot complaint:
# 500 words to say "maybe", then offering a table instead of an answer.
# The last beat hands the floor to the judge, who is left waiting — the
# roast lands on the judge's own experience of agents like this one.

ENTRY = "My agent writes 500 words to say 'maybe', then asks if I want it as a table. Just answer, bro \u2014 the judge is waiting."

MAX_CHARS = 140
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
