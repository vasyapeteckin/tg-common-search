# Telegram common search

search for user messages in telegram common chats


# Installing

Clone this repository to your local machine with git, create virtual environment and install requirements.
```bash
git clone https://github.com/vasyapeteckin/tg-common-search.git
cd tg-common-search

```

# Basic usage

rename `example.env` to `.env`, configure `API_ID=` and `API_HASH=` get api keys [here](https://my.telegram.org/auth?to=apps)

```bash
python src/main.py
```

### CLI

Replace %target_username% for target id, username or @username

```bash
python src/main.py %target_username%
```

result saves to the `outputs/%target_username%.html`
