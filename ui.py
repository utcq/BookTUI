import curses
import textwrap
import os



home = os.path.expanduser('~')

def reader(chaptersx, title, file, page: int=0):
    screen = curses.initscr()
    screen.immedok(True)
    screen.keypad(True)
    curses.noecho()
    chapters = chaptersx
    pages = len(chapters)
    searchterm = ""
    pagsf = []
    pagc = 0
    listening = False
    if page != 0:
        page-=1
    screen.erase()
    screen.refresh()
    screen.idcok(False)
    screen.attron(curses.A_BOLD)
    screen.border(0)
    screen.attron(curses.A_NORMAL)

           
    while True:


        box1 = curses.newwin(39, 193,4, 14)
        box1.immedok(True)
        box1.box()
        box2 = curses.newwin(3, 13, 1, 2)
        box2.immedok(True)
        box2.box()
        box3 = curses.newwin(3, 60, 1, 50)
        box3.immedok(True)
        box3.box()
        box4 = curses.newwin(3, 30, 44, 2)
        box4.immedok(True)
        box4.box()




        
        box2.addstr(1, 2, textwrap.fill(f"{str(page + 1)}/{str(pages)}", 10))
        
        box3.addstr(1, 2, textwrap.fill(f"{title}"))

        box1.addstr(1, 3, textwrap.fill(chaptersx[page].replace(r"\n", "\n"), 180))
        
        box4.addstr(1, 1, textwrap.fill(searchterm), 12)


        #box1.addstr("Hello World of Curses!")


                    

        char = screen.getch()
        if listening:
            if char == 32:
                searchterm+=" "
            elif char == curses.KEY_BACKSPACE:
                pass
            else:
                try:
                    searchterm+=chr(char)
                except:
                    searchterm+=str(char)
        else:
            if char == 113: 
                if os.path.isdir(f"{home}/.config/booktui/"):
                    pass
                else:
                    os.mkdir(f"{home}/.config/booktui/")
                open(f"{home}/.config/booktui/{file.replace('.pdf', '.conf').replace('.epub','.conf')}", "w").write(str(page))
                break
        if char == curses.KEY_LEFT:
            page-=1
            try:
                x = chapters[page]
            except:
                page+=1
            if page <= -1:
                page+=1
        elif char == curses.KEY_RIGHT:
            page+=1
            try:
                x = chapters[page]
            except:
                page-=1
        elif char == 58:
            listening = True
            searchterm+=":"
        elif char == 10 and searchterm != "":
            pg = 0
            for chap in chaptersx:
                if searchterm.replace(':search ', '') in chap.lower():
                    pagsf.append(pg)
                    listening = False
                    chaptersx[pg] = chap.replace(searchterm.replace(":search ", ""), " --------> " + searchterm.replace(':search ', '') + " <-------- ")
                pg+=1
            try:
                if len(pagsf) > 0:
                    page = pagsf[0]
                    pagc = 0
            except Exception as e:
                pass

        elif char == 110 and searchterm != "" and pagsf != []:
            xc = len(pagsf) - 1
            if pagc != xc:
                pagc += 1
                page = pagsf[pagc]
            else:
                pagc = 0
                page = pagsf[0]
            
        elif char == 27 and searchterm != "":
            searchterm=""
            listening=False
            pagsf = []
            pagc = 0
            xi = 0
            for chap in chaptersx:
                chaptersx[xi] = chaptersx[xi].replace(" --------> ", "").replace(" <-------- ", "")
                xi += 1

    
    curses.endwin()

