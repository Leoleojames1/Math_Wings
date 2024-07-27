
class colors:
    def __init__(self):
        self.name = "read_write_class"

    def get_colors(self):
        """ a method for getting the color dictionary for command line print
            args: none
            returns: self.colors
        """
        self.colors = {
            "YELLOW": '\033[93m',
            "GREEN": '\033[92m',
            "RED": '\033[91m',
            "END": '\033[0m',
            "HEADER": '\033[95m',
            "OKBLUE": '\033[94m',
            "OKCYAN": '\033[96m',
            "OKGREEN": '\033[92m',
            "DARK_GREY": '\033[90m',
            "WARNING": '\033[93m',
            "FAIL": '\033[91m',
            "ENDC": '\033[0m',
            "BOLD": '\033[1m',
            "UNDERLINE": '\033[4m',
            "WHITE": '\x1B[37m',
            "LIGHT_GREY": '\033[37m',
            "LIGHT_RED": '\033[91m',
            "LIGHT_GREEN": '\033[92m',
            "LIGHT_YELLOW": '\033[93m',
            "LIGHT_BLUE": '\033[94m',
            "LIGHT_MAGENTA": '\033[95m',
            "LIGHT_CYAN": '\033[96m',
            "LIGHT_WHITE": '\033[97m',
            "DARK_BLACK": '\033[30m',
            "DARK_RED": '\033[31m',
            "DARK_GREEN": '\033[32m',
            "DARK_YELLOW": '\033[33m',
            "DARK_BLUE": '\033[34m',
            "DARK_MAGENTA": '\033[35m',
            "DARK_CYAN": '\033[36m',
            "DARK_WHITE": '\033[37m',
            "BRIGHT_BLACK": '\033[90m',
            "BRIGHT_RED": '\033[91m',
            "BRIGHT_GREEN": '\033[92m',
            "BRIGHT_YELLOW": '\033[93m',
            "BRIGHT_BLUE": '\033[94m',
            "BRIGHT_MAGENTA": '\033[95m',
            "BRIGHT_CYAN": '\033[96m',
            "BRIGHT_WHITE": '\033[97m',
        }
        return self.colors