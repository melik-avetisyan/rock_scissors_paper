from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import Lexicon


lexicon = Lexicon()


start_button_1 = KeyboardButton(text=lexicon.start_button_1)
start_button_2 = KeyboardButton(text=lexicon.start_button_2)
start_keyboard = ReplyKeyboardMarkup(keyboard=[[start_button_1, start_button_2]],
                                     resize_keyboard=True)


game_buttons = [KeyboardButton(text=i) for i in lexicon.titles]
game_keyboard = ReplyKeyboardMarkup(keyboard=[game_buttons],
                                    resize_keyboard=True)

continue_button_1 = KeyboardButton(text=lexicon.more_game)
continue_button_2 = KeyboardButton(text=lexicon.no_more_game)
continue_keyboard = ReplyKeyboardMarkup(keyboard=[[continue_button_1, continue_button_2]],
                                        one_time_keyboard=True,
                                        resize_keyboard=True)