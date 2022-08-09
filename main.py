#!/usr/bin/python3
import ui
import os, re, sys, requests
home = os.path.expanduser('~')

def updater():
    print("Checking for updates...")
    ver = float(open(f"{home}/BookTUI/.version", "r").read().strip().replace("\n", ""))
    response= requests.get('https://raw.githubusercontent.com/UnityTheCoder/BookTUI/main/.version')
    crv = float(response.text.strip().replace("\n", "")) 
    if ver != crv:
        os.system(f"rm -rf {home}/BookTUI; git clone https://github.com/UnityTheCoder/BookTUI.git {home}/BookTUI; chmod +x /usr/bin/booktui")
        print("Updated!")
        exit()
    print("Updates not found!")

def retrieveTitle(path):
    result = os.popen(f"pdfinfo {path}  2>/dev/null | grep Title: | sed 's/Title:[ ]*//'")
    return result.read().replace(r"\n", "\n")


def retrieveETitle(path):
    result = os.popen(f"epub2txt --meta {path}  2>/dev/null | grep Title: | sed 's/Title:[ ]*//'")
    return result.read().replace(r"\n", "\n")

def retrieveEContent(path):
    result = os.popen(f"epub2txt {path}")
    return result.read().replace(r"\n", "\n")

def splitIntoCharpsE(textx):
    charps = []
    text = ""
    for line in textx.strip().split("\n"):
        text += line + r"\n"
        if r"[0m" in text:
            #[1mLadle Rat Rotten Hut [0m
            charps.append(text.replace("[1m", "").replace("[0m", "").replace("[3m", ""))
            text = ""
    return charps
    


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
    if len(sys.argv) == 1:
        print("Usage: booktui [OPTIONAL: update] file.pdf [OPTIONAL: page_number]\nKEYS: \n    -> = Next page\n    <- = Previous page\n    Q = exit\n    :search = Search a word in text\n    N = next found word")
        sys.exit(1)
    else:
        file = sys.argv[1]
        page = 0
        if len(sys.argv) == 3:
            page = int(sys.argv[2])
        if sys.argv[1] == "update":
            updater()
            exit()

        if file.endswith(".pdf"):
            title = retrieveTitle(file)
            content = retrieveContent(file)
            book = splitIntoCharps(content)
            ui.reader(book, title, page)
        elif file.endswith(".epub"):
            title = retrieveETitle(file)
            content = retrieveEContent(file)
            book = splitIntoCharpsE(content)
            ui.reader(book, title, page)
        
