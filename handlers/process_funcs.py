from lexicon.lexicon import Lexicon
from random import randint


lexicon = Lexicon()


def who_win(user_choice):
    bot_answer = lexicon.titles[randint(0, 2)]
    if user_choice == bot_answer:
        return (None, bot_answer)
    elif user_choice+bot_answer in lexicon.win_combinstions:
        return ('user', bot_answer)
    else:
        return ('bot', bot_answer)
