import os
import sys

from pyrogram import Client
from pyrogram.enums import ChatType
from dotenv import load_dotenv

from utils import create_html

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

app = Client("my_account", api_id=api_id, api_hash=api_hash)


async def search_message_in_chats(target_user):
    result = []
    async with app:
        async for dialog in app.get_dialogs():
            if dialog.chat.type == ChatType.SUPERGROUP:
                chat_title, chat_id, chat_username = dialog.chat.first_name or dialog.chat.title, dialog.chat.id, dialog.chat.username
                # print(chat_title, chat_username)
                data = {'id': chat_id,
                        'title': chat_title,
                        'username': chat_username,
                        'messages': []}
                async for message in app.search_messages(chat_id=chat_id, from_user=target_user):
                    # print(message.date, message.chat.title, message.text.replace('\n', ' ') if message.text is not None else None)
                    data['messages'].append(message)
                if data['messages']:
                    result.append(data)
    create_html(target_user=target_user, chats=result)


if __name__ == '__main__':
    target_user = ''

    app.run(search_message_in_chats(target_user=target_user))
