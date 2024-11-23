from aiogram import Router, types, Bot, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.finitestate import AdminReplyState, Form
from nastroyka import config



import text

bot = Bot(config.bot_token.get_secret_value())
router = Router()

@router.message(F.text.lower() == "создать весточку")
async def process_message(message: Message, state: FSMContext):
    await state.set_state(Form.txt)
    await message.answer(text.kakashka)

def generate_reply_markup(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="НАПИСАТЬ ЛОПУХУ НЕВЕЖЕМУ ЛАПТЕЙ", callback_data=f"reply_{user_id}")]])




@router.message(Form.txt)
async def form_txt(message: Message, state: FSMContext):
    
    await state.update_data(txt=message.text)
    await bot.send_message(
        config.ADMIN_CHAT_ID,
        f"ВОПРОС ОТ ОБЫВАТЕЛЯ ОБЫЧНОЙ РУССКОЙ ОБЩИНЫ {message.from_user.first_name}: {message.text}",
        reply_markup=generate_reply_markup(message.from_user.id))
    await message.answer("ВАШ ЗАПРОС НА ПОДКРЕПЛЕНИЕ ОТ БОЙЦОВ ТУГАРСКИХ ВОЙН ОТПРАВЛЕН")
    await state.clear()



@router.callback_query(F.data.startswith("reply_"))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.data.split("_")[1]
    await state.set_state(AdminReplyState.waiting_for_reply)
    await state.update_data(reply_to_user_id=user_id)
    await bot.send_message(chat_id=config.ADMIN_CHAT_ID, text="ВВЕДИТЕ ОТВЕТ ГОНЦУ")



@router.message(AdminReplyState.waiting_for_reply)
async def send_reply_to_user(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data['reply_to_user_id']
    
    await bot.send_message(chat_id=user_id, text=f"ВЕСТОЧКА ОТ КНЯЗЯ РУСИ ВЕЛИКОЙ: {message.text}")
    await bot.send_message(chat_id=config.ADMIN_CHAT_ID, text="ВЕСТОЧКА ЗАСЛАНА")
    await state.clear()