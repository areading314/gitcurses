from gitcurses.application import Application


def main():
    with Application() as a:
        a.run()


if __name__ == '__main__':
    main()
