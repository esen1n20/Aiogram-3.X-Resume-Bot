import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_commands, repost
from nastroyka import config


async def main():
    
    bot = Bot(config.bot_token.get_secret_value())
    
    dp = Dispatcher()

    
    dp.include_routers(
        user_commands.router,
        repost.router
    )
    
    
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)



if __name__ == "__main__":
    asyncio.run(main())