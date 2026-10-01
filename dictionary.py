from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
TEXT_FILE = ROOT / "text.txt"
MASTER_FILE = ROOT / "master.txt"
NEW_WORDS_FILE = ROOT / "newwords.txt"


def words_from(text):
    return {
        word
        for word in re.sub(r"[^A-Za-z]", "\n", text).splitlines()
        if word
    }


def main():
    raw_words = words_from(TEXT_FILE.read_text(encoding="utf-8"))
    master_words = words_from(MASTER_FILE.read_text(encoding="utf-8"))
    new_words = sorted(raw_words - master_words)

    NEW_WORDS_FILE.write_text(
        "\n".join(new_words) + ("\n" if new_words else ""),
        encoding="utf-8",
    )

    if new_words:
        with MASTER_FILE.open("a", encoding="utf-8", newline="") as master_file:
            if MASTER_FILE.stat().st_size and not MASTER_FILE.read_bytes().endswith(b"\n"):
                master_file.write("\n")
            master_file.write("\n".join(new_words) + "\n")


if __name__ == "__main__":
    main()