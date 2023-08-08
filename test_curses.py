import curses
import sys

def main(argv):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    # stdscr.keypad(True)

    try:
        stdscr.addstr(0, 0, "Hello, world!", curses.color_pair(1))
        screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
        startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
        stdscr.addstr(3, startingXPos, screenDetailText)
        stdscr.addstr(5, curses.COLS - len("press a key to quit."), "press a key to quit.")

        stdscr.refresh()
        stdscr.getch()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

    curses.nocbreak()
    curses.echo()
    curses.curs_set(True)
    # stdscr.keypad(False)
    curses.endwin()


if __name__ == "__main__":
    main(sys.argv[1:])
