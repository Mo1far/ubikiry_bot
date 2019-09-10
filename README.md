# Cloning this repo
```
git clone https://github.com/Mo1far/ubikiry_bot.git
```
# Install system requirements
```
python3.8-dev
python3.8-distutils
```

# Install requirements
```
pip3 install -r requirements.txt
```
# Running Redis
```
$ redis-server
```

# First Run
Uncomment the line in bot/db.py (remove '# ''), and 
```
# db.create_tables([Users])
```
and return back after first run
# Run
```
$ screen python3.8 main.py
```

# Edit TG TOKEN
insert your token in bot/config.py
```
BOT_TOKEN = 'Your Token'

```

# Edit rate limit
Edit RATE_LIMIT in bot/config.py

#### Example
```angular2html
if RATE_LIMIT=5 You can use command every 5 seconds
```

# Set target chat
1 - get the chat id by adding @chatid_echo_bot to the chat bot, you can remove the bot from the chat after receiving chat_id
2 - Set chat_id in bot/config.py 
```angular2html
TARGET_CHAT_ID = 'your chat_id'
```