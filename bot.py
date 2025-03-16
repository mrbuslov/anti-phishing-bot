import asyncio
import os
import re

from aiogram import Bot, Dispatcher, Router
from consts.consts import LINK_PATTERN
from consts.spam_consts import REFERRAL_LINKS_WORDS_INSERTIONS, SPAM_WORDS_INSERTIONS

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
router = Router()
dp = Dispatcher()


@router.message(lambda msg: True)
async def phishing_filter(message):
    msg_text = message.text.lower()
    new_user = message.from_user
    user_name = (
        "@" + new_user.username
        if new_user.username else
        (new_user.first_name + ' ' + new_user.last_name).strip()
    )
    if any(
            spam_msg in msg_text
            for spam_msg in SPAM_WORDS_INSERTIONS
    ):
        await message.answer(
            f"{user_name}, your message was encountered as phishing message. It was deleted."
        )
        await message.delete()
        return

    links_matches = re.findall(LINK_PATTERN, msg_text)
    for link in links_matches:
        if any(
                referral_link_part in link
                for referral_link_part in REFERRAL_LINKS_WORDS_INSERTIONS
        ):
            await message.answer(
                f"{user_name}, your message contains phishing link. It was deleted."
            )
            await message.delete()
            return


dp.include_router(router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
