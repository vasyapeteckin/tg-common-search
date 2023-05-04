import os
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
        try:
            chats = await app.get_common_chats(target_user)
            for chat in chats:
                if chat.type == ChatType.SUPERGROUP:
                    chat_title, chat_id, chat_username = chat.first_name or chat.title, chat.id, chat.username
                    data = {'id': str(chat_id)[4:],
                            'title': chat_title,
                            'username': chat_username,
                            'messages': []}

                    async for message in app.search_messages(chat_id=chat_id, from_user=target_user):
                        data['messages'].append(message)
                    if data['messages']:
                        result.append(data)
        except ValueError as e:
            print(e.args[0])
    create_html(target_user=target_user, chats=result)


if __name__ == '__main__':
    target_user = ''

    app.run(search_message_in_chats(target_user=target_user))
