from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode

from filters.group_chat import IsGroup
from loader import bot  # Make sure the bot instance is imported correctly

# Define the FSM states
class SendPoster(StatesGroup):
    waiting_for_text = State()

# Initialize the router
group_router = Router()

# List of channel IDs where the text will be sent
CHANNEL_IDS = [-1002166239027, -1001747207701]

# Command handler for /send
@group_router.message(IsGroup(), Command("send"))
async def ask_for_text(message: Message, state: FSMContext):
    await message.answer("Please send me the text message, and I will send it to all channels.", parse_mode=ParseMode.HTML)
    await state.set_state(SendPoster.waiting_for_text)

# Message handler to receive the text and forward it to channels
@group_router.message(IsGroup(), F.content_type == ContentType.TEXT)
async def receive_text(message: Message, state: FSMContext):
    # Check if the state is waiting for text
    current_state = await state.get_state()
    if current_state == SendPoster.waiting_for_text:
        # Forward the text to all channels
        for channel_id in CHANNEL_IDS:
            await bot.send_message(chat_id=channel_id, text=message.text, parse_mode=ParseMode.HTML)


        await message.answer("The text message has been sent to all channels!", parse_mode=ParseMode.HTML)
        # Finish the state
        await state.clear()

# Handler for other messages if they are not text
@group_router.message(IsGroup(), ~F.content_type == ContentType.TEXT)
async def not_text_message(message: Message, state: FSMContext):
    # Check if the state is waiting for text
    current_state = await state.get_state()
    if current_state == SendPoster.waiting_for_text:
        await message.answer("Please send a valid text message.", parse_mode=ParseMode.HTML)
