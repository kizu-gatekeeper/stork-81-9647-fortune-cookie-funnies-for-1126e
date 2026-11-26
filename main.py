"""Entry program for the make.fun "Fortune Cookie Funnies for Engineers" bounty.

It writes a single funny fortune cookie message for a software
engineer to entry.txt inside the output directory make.fun hands
it through MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = "Your code will compile on the first try today. (This cookie was written by someone who has never seen your code.)"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
