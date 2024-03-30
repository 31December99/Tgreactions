# -*- coding: utf-8 -*-

from telethon import TelegramClient, errors
from decouple import config
from telethon.errors import SessionPasswordNeededError


class MyTelegram:
    """Telegram login"""

    API_ID = config('YOUR_API_ID')
    API_HASH = config('YOUR_API_HASH')
    PHONE = config('YOUR_PHONE_NUMBER')
    SESSION = config('SESSION_NAME')
    INVITE_LINK = config('INVITE_LINK')

    def __init__(self):
        # Telegram Takeout instance
        self.__takeout = None
        # Channel entity
        self.__channel = None
        # Telgram client
        self.__client = None

    @property
    def takeout(self):
        return self.__takeout

    @property
    def channel(self):
        return self.__channel

    async def connect(self):
        """
        Connect to telegram

        retry_delay: wait for n seconds if connect fails then retry
        flood_sleep_threshold : telethon sleeps if flow_wait error < 240s occurs
        """
        self.__client = TelegramClient(session=self.SESSION,
                                       api_id=self.API_ID,
                                       api_hash=self.API_HASH,
                                       retry_delay=10,
                                       flood_sleep_threshold=240)
        await self.__client.connect()

    async def login(self):
        """
            Login to telegram after auth check
        """

        # Call connect method and config the client
        await self.connect()

        # Is this your first login ?
        if not await self.__client.is_user_authorized():
            print("Request auth...")
            await self.__client.send_code_request(self.PHONE)
            try:
                await self.__client.sign_in(phone=self.PHONE, code=int(input('Enter code: ')))
            except SessionPasswordNeededError:
                # if a password is set
                password = input("Enter your password: ")
                await self.__client.sign_in(password=password)

        # Get a takeout instance
        try:
            async with self.__client.takeout(finalize=False) as conn:
                self.__channel = await conn.get_input_entity(self.INVITE_LINK)
                self.__takeout = conn
                print(f"Connected...")
        except errors.TakeoutInitDelayError:
            print("Step 1 > Confirm authentication in the Telegram channel (+42777)")
            print("Step 2 > Restart the application")
        except errors.InviteHashExpiredError as err:
            print("Wrong or invalid link!", err)
