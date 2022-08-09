import curses
import textwrap

def reader(chaptersx, title, page: int=0):
    screen = curses.initscr()
    screen.immedok(True)
    screen.keypad(True)
    curses.noecho()
    chapters = chaptersx
    pages = len(chapters)
    while True:
        screen.attron(curses.A_BOLD)
        screen.border(0)
        screen.attron(curses.A_NORMAL)

        box1 = curses.newwin(43, 193,4, 14)
        box1.immedok(True)
        box1.box()
        box2 = curses.newwin(3, 13, 1, 2)
        box2.immedok(True)
        box2.box()
        box3 = curses.newwin(3, 60, 1, 50)
        box3.immedok(True)
        box3.box()



        
        box2.addstr(1, 2, textwrap.fill(f"{str(page + 1)}/{str(pages)}", 10))
        
        box3.addstr(1, 2, textwrap.fill(f"{title}"))

        box1.addstr(1, 3, textwrap.fill(chaptersx[page].replace(r"\n", "\n"), 180))


        #box1.addstr("Hello World of Curses!")

        char = screen.getch()
        if char == 113: break
        elif char == curses.KEY_LEFT:
            page-=1
            try:
                x = chapters[page]
            except:
                page+=1
            if page <= 0:
                page+=1
        elif char == curses.KEY_RIGHT:
            page+=1
            try:
                x = chapters[page]
            except:
                page-=1



    
    curses.endwin()

