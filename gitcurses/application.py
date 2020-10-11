import curses
import os

import pygit2

from gitcurses.colors import Colors


class Application:

    def __init__(self):
        screen = curses.initscr()
        maxy, maxx = screen.getmaxyx()
        self.max_y = maxy
        self.max_x = maxx
        self.screen = screen

    def __enter__(self):
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.start_color()
        curses.curs_set(0)
        return self

    def __exit__(self, *args):
        curses.echo()
        curses.nocbreak()
        self.screen.keypad(False)

    def run(self):
        quit = False

        repo = pygit2.Repository(os.getcwd())
        branch_name = repo.head.shorthand
        remotes = repo.remotes
        self.screen.attron(Colors.get_pair(curses.COLOR_WHITE, curses.COLOR_MAGENTA))
        self.screen.hline(0, 0, ' ', self.max_x)
        self.screen.addstr(0, 1, "GitCurses v0.1")
        self.screen.addstr(2, 1, f"Head:     {branch_name}", Colors.get_pair(curses.COLOR_WHITE))
        if remotes:
            self.screen.addstr(3, 1, f"Upstream: {remotes}", Colors.get_pair(curses.COLOR_CYAN))

        while not quit:
            next_input = self.screen.getkey()
            self.screen.addstr(2, 1, next_input, Colors.get_pair(curses.COLOR_GREEN, curses.COLOR_BLUE))
            self.screen.addstr(3, 1, next_input, Colors.get_pair(curses.COLOR_CYAN))
            self.screen.attron(Colors.get_pair(curses.COLOR_BLUE))
            self.screen.hline(5, 0, '-', self.max_x)
            if 'q' in next_input:
                quit = True

