import asyncio
from typing import Union
import string
import random
from pyrogram import types, Client
from sharkub.settings.prefix import my_prefix as prefix


def get_args(message: types.Message) -> Union[list, None]:
    """
    Returns a list of arguments, or None if there are no arguments.
    """

    text = message.text or message.caption
    if len(text.split(" ")) == 1: # if no arguments
        return None
    
    return text.split(" ")[1:]


def get_args_raw(message: types.Message) -> Union[str, None]:
    """
    Returns a string with arguments, or None if there are no arguments.
    """

    text = message.text or message.caption
    if len(text.split(" ")) == 1: # if no arguments
        return None
    
    return " ".join(text.split(" ")[1:])


def rand(_len: int) -> str:
    return "".join([random.choice(string.ascii_lowercase + string.digits) for _ in range(_len)])


async def asset_chat(client: Client, title: str, desc: str = None) -> types.Chat:
    return (await client.create_supergroup(title, desc))


class Conversation:

    def __init__(self, client: Client, chat_id: int | str, purge: int = True) -> None:
        self.client = client
        self.chat_id = chat_id
        self.purge = purge
        self.msgs = []
    
    async def __aenter__(self): # async with ...
        return self
    
    async def __aexit__(self):
        if self.purge:
            if len(self.msgs) > 0:
                for message in self.msgs:
                    await message.delete()    

    async def send_message(self, text: str, *args, **kwargs) -> types.Message:
        message = await self.client.send_message(
            self.chat_id,
            text,
            args,
            kwargs
        )
        self.msgs.append(message)
        return message
    
    async def send_photo(self, photo: str, *args, **kwargs) -> types.Message:
        photo = await self.client.send_photo(
            self.chat_id,
            photo,
            args,
            kwargs
        )
        self.msgs.append(photo)
        return photo
    
    async def get_response(self, timeout: int = 1) -> types.Message | None:
        responses = await self.client.get_chat_history(self.chat_id, 1)
        async for message in responses:
            while message.from_user.is_self:
                timeout -= 1
                if not timeout:
                    return None
                
                asyncio.sleep(1)
                responses = await self.client.get_chat_history(self.chat_id, 1)
            
            self.msgs.append(message)
            return message
        
        