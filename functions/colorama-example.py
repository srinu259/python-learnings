import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def format_text(color: str, effect: str) -> None:
    print("{}{}{}".format(color, effect, RESET))


colorama.init()
format_text(BLACK, "What color is this?")
format_text(RED, "What color is this?")
format_text(GREEN, "What color is this?")
format_text(YELLOW, "What color is this?")
format_text(BLUE, "What color is this?")
format_text(MAGENTA, "What color is this?")
format_text(CYAN, "What color is this?")
format_text(WHITE, "What color is this?")
format_text(BOLD, "What color is this?")
format_text(UNDERLINE, "What color is this?")
format_text(REVERSE, "What color is this?")
colorama.deinit()
print("*"*80)


# use * to pack multiple arguments
def multi_format_text(color: str, *effects: str) -> None:
    effects_required = "".join(effects)
    print("{}{}{}".format(color, effects_required, RESET))


colorama.init()
multi_format_text(BLACK, BOLD, UNDERLINE, "What color is this?")
multi_format_text(RED, "What color is this?")
multi_format_text(GREEN, "What color is this?")
multi_format_text(YELLOW, "What color is this?")
multi_format_text(BLUE, "What color is this?")
multi_format_text(MAGENTA, "What color is this?")
multi_format_text(CYAN, "What color is this?")
multi_format_text(WHITE, "What color is this?")
multi_format_text(BOLD, "What color is this?")
multi_format_text(UNDERLINE, "What color is this?")
multi_format_text(REVERSE, "What color is this?")
colorama.deinit()
