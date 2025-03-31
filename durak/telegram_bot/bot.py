from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher()

# Логика игры (можно вынести в отдельный модуль)
def deal_cards():
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck[:6], deck[6:12], deck[-1]  # player, bot, trump

@dp.message(Command("start"))
async def start_game(message: types.Message):
    player_hand, bot_hand, trump = deal_cards()
    await message.reply(
        f"Твои карты: {', '.join(player_hand)}\n"
        f"Козырь: {trump}\n\n"
        "Выбери карту для атаки!"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())