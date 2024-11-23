from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    txt = State()

class AdminReplyState(StatesGroup):
    waiting_for_reply = State()