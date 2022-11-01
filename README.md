# ConnCheckerBot
### This bot was created to check connection to some host. For using it you have to make your own telegram boot.

## Bot commands
| Name         | Description                                       |
|--------------|---------------------------------------------------|
| `/web`  | To check connection via HED request |
| `/ping`  | To check connection via ping command |

## How to make your own telegram bot
1. Open Telegram messenger, sign in to your account or create a new one.
2. Enter @Botfather in the search tab and choose this bot, click “Start” to activate BotFather bot, In response, you receive a list of commands to manage bots.
3. Choose or type the /newbot command and send it.
4. Choose a name for your bot — your subscribers will see it in the conversation. And choose a username for your bot — the bot can be found by its username in searches. The username must be unique and end with the word “bot.”
5. After you choose a suitable name for your bot — the bot is created. You will receive a message with a link to your bot t.me/<bot_username>, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.
6. Copy your token value and set is as system environment variable SECRET_TOKEN

### Script environment variables
| Name         | Description                                       | Default    |
|--------------|---------------------------------------------------|------------|
| `SECRET_TOKEN`  | The telegram token   | ""    |


## How to run
```
export SECRET_TOKEN='Telegram API Token'
pip3 install -r requirements.txt
python3 -m bot
```
or you can use Docker
```
docker build -t bot
docker run --name=bot -e SECRET_TOKEN='Telegram API Token' -it bot 
```

## Future plans
1. Make it possible to set a schedule to check the host