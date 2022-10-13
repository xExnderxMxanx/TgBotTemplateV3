from aiogram.fsm.state import State, StatesGroup

class WaitingAnswer(StatesGroup):
    stat = State()