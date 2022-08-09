#!/usr/bin/python3
import ui
import os, re, sys


def updater():
    print("Checking for updates...")
    ver = int(open(f"{home}/BookTUI/.version", "r").read())
    response= requests.get('https://raw.githubusercontent.com/UnityTheCoder/BookTUI/main/.version')
    crv = int(response.text)
    if ver != crv:
        os.system(f"rm -rf {home}/BookTUI; git clone https://github.com/UnityTheCoder/BookTUI.git {home}/BookTUI; chmod +x /usr/bin/booktui")
        print("Updated!")
        exit()
    print("Updates not found!")

def retrieveTitle(path):
    result = os.popen(f"pdfinfo {path}  2>/dev/null | grep Title: | sed 's/Title:[ ]*//'")
    return result.read().replace(r"\n", "\n")


def retrieveContent(path):
    result = os.popen(f"pdftotext {path} -")
    return result.read().replace(r"\n", "\n")


def splitIntoCharps(text):
    charps = []
    charpsz = []
    charpsz = text.split("\n\n")
    for ch in charpsz:
        if ch == '':
            pass
        elif ch == '•':
            pass
        elif "page" in ch.lower():
            pass
        elif ch in charps:
            pass
        elif len(ch) < 4:
            pass
        else:
            charps.append(ch)

        
    return charps


if __name__ == "__main__":
    updater()
    if len(sys.argv) == 1:
        print("Usage: booktui file.pdf [OPTIONAL: page_number]\nKEYS: \n    -> = Next page\n    <- = Previous page\n    Q = exit")
        sys.exit(1)
    else:
        file = sys.argv[1]
        page = 0
        if len(sys.argv) == 3:
            page = int(sys.argv[2])
        title = retrieveTitle(file)
        content = retrieveContent(file)
        book = splitIntoCharps(content)
        ui.reader(book, title, page)
