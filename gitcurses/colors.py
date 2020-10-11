import curses


class Colors:
    _last_pair = 0
    _colors = {}

    @classmethod
    def _next_number(cls):
        cls._last_pair += 1
        return cls._last_pair

    @classmethod
    def get_pair(cls, foreground, background = curses.COLOR_BLACK):
        t = (foreground, background)
        if t not in cls._colors:
            next_number = cls._next_number()
            curses.init_pair(next_number, foreground, background)
            cls._colors[t] = next_number
        return curses.color_pair(cls._colors[t])

