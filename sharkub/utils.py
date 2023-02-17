#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import asyncio
from typing import Union
import string
import random
from pyrogram import types, Client
from sharkub.settings.prefix import my_prefix as prefix
from typing import Union
from pyrogram.types import Message, User, Chat

def get_display_name(entity: Union[User, Chat]) -> str:
    """Получить отображаемое имя
    Параметры:
        entity (``pyrogram.types.User`` | ``pyrogram.types.Chat``):
            Сущность, для которой нужно получить отображаемое имя
    """
    return getattr(entity, "title", None) or (
        entity.first_name or "" + (
            " " + entity.last_name
            if entity.last_name else ""
        )
    )


def random_id(size: int = 10) -> str:
    """Возвращает рандомный идентификатор заданной длины
    Параметры:
        size (``int``, optional):
            Длина идентификатора
    """
    return "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(size)
    )

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
        
        