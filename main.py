import os
import sys
import time
from subprocess import call

class CarteDuJour():
    def __init__(self, options):
        self.options        = options
        self.choosen_index  = 0
        self.choosen_option = options.keys()[self.choosen_index]

    def loop(self):
        self.run()
        user_input =  self.wait_key()

        if user_input == "\n":
            print "\nChoosen: " + self.options[self.choosen_option]
            return self.options[self.choosen_option]
        else:
            self.update_selector(user_input)
            self.loop()

    def run(self):
        call("clear")
        print "\n\n\033[35;1mMenu Options\033[0m\n\n"

        for option in options:
            print self.selector(option) + " " + option + " : " + options[option]

    def selector(self, option):
        if option == self.choosen_option:
            return "(\033[36m*\033[0m)"
        else:
            return "( )"

    def update_selector(self, user_input):
        self.choosen_index = self.find_next_index(user_input)
        self.choosen_option = self.options.keys()[self.choosen_index]

    def movement(self, user_input):
        if user_input == "j":
            return 1
        elif user_input == "k":
            return -1
        else:
            print "\n\033[31;1mInvalid selection\033[0m"
            time.sleep(1)
            self.loop()

    def find_next_index(self, user_input):
        direction = self.movement(user_input)

        if self.choosen_index == len(self.options.keys()) - direction:
            return 0
        elif self.choosen_index == 0 and direction == -1:
            return len(self.options.keys()) - 1
        else:
            return self.choosen_index + self.movement(user_input)

    def wait_key(self):
        ''' Wait for a key press on the console and return it. '''
        result = None
        if os.name == 'nt':
            import msvcrt
            result = msvcrt.getch()
        else:
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

        return result

options       = { "Option 1": "Point Break", "Option 2": "Monsters Inc", "Option 3": "Senna" }
carte_du_jour = CarteDuJour(options)
carte_du_jour.loop()
