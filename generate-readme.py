import glob
from collections import defaultdict


def header():
    return """# :bulb: TIL: Today I Learned

Inspired by https://github.com/jbranchaud/til.

---"""


def get_directories(md_files):
    directories = [f.split("/")[0] for f in md_files]
    return sorted(list(set(directories)))


def extract_title(file_name):
    with open(file_name, "r") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip()[2:]
    return None


if __name__ == "__main__":
    md_files = glob.glob("*/*.md")
    directories = get_directories(md_files)

    d = defaultdict(list)
    for file_name in md_files:
        directory = file_name.split("/")[0]
        title = extract_title(file_name)
        d[directory].append((title, file_name))

    print(header())
    for directory in directories:
        print(f"\n\n### {directory.title()}\n")
        for title, file_name in d[directory]:
            print(f"- [{title}]({file_name})")
