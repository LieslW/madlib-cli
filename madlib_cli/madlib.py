welcome_message = """
******************************
**  ***** WELCOME *****     **
** Thank you for partaking  **
** in my first MadLib game. **
**  Madlib is a fun phrasal **
** template word game that  **
** prompts the player for a **
**  list of words to sub in **
**  for blanks in a story.  **
** The stories usually come **
**  out quite comedic when  **
**  the reader reads them   **
**  out for the first time. **
**   Try it out below and   **
**    follow the prompts!   **
**         HAVE FUN!        **
******************************
"""

print(welcome_message)


def read_template(track):
    try:
        with open(track, 'r') as file:
            contents = file.read().strip()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(string):
    pass


def merge(string, user_input):
    pass
