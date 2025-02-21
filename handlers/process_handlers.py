from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove

from aiogram import Router, F
from db.db_funcs import add_player, set_resul, get_stat
from lexicon.lexicon import Lexicon
from handlers.process_funcs import who_win
import keyboards


router = Router()
lexicon = Lexicon()


@router.message(CommandStart())
async def srart_process(message):
    await add_player(message)
    await message.answer(text=lexicon.start,
                         reply_markup=keyboards.start_keyboard)


@router.message(F.text.in_({lexicon.start_button_1, lexicon.more_game}))
async def game_process(message):
    await message.answer(text=lexicon.game_process,
                         reply_markup=keyboards.game_keyboard)


@router.message(F.text.in_({lexicon.start_button_2, lexicon.no_more_game}))
async def stat_process(message):
    stat = await get_stat(message.from_user.id)
    if stat.games == 0:
        await message.answer(text='у вас нет статистики',
                             reply_markup=keyboards.continue_keyboard)
    else:
        wins = round(stat.scores/stat.games*100, 2)
        await message.answer(text=f'games - {stat.games} \n'
                                  f'wins - {wins}% \n'
                                  '/start for refresh',
                             reply_markup=ReplyKeyboardRemove())


@router.message(F.text.in_({*lexicon.titles}))
async def winner_process(message):
    res = who_win(message.text)
    if res[0] is None:
        await message.answer(text=f'ничья \n'
                                  f'{message.from_user.username}-{message.text}\n'
                                  f'bot-{res[1]}',
                             reply_markup=keyboards.game_keyboard)
    elif res[0] == 'bot':
        await set_resul(message)
        await message.answer(text=f'победил бот \n'
                                  f'{message.from_user.username}-{message.text}\n'
                                  f'bot-{res[1]}',
                             reply_markup=keyboards.continue_keyboard)
    elif res[0] == 'user':
        await set_resul(message, score=1)
        await message.answer(text=f'победил кожаный \n'
                                  f'{message.from_user.username}-{message.text}\n'
                                  f'bot-{res[1]}',
                             reply_markup=keyboards.continue_keyboard)
