# discord-temp-bot

DiscordにSwitchBot 温湿度計の温度と湿度を送信するbot

## Usage

```
poetry install
poetry run python main.py
```

### Environment Variables

- DISCORD_TOKEN

  Discordのトークン

- SWITCHBOT_TOKEN

  SwitchBotのトークン
  SwitchBotアプリの `アプリバージョン` を10回連打すると出現する `開発者向けオプション` から発行可能

- SWITCHBOT_DEVICE_ID

  SwitchBot 温湿度計のデバイスID
  以下のコマンドで取得可能
  ```
  curl --request GET 'https://api.switch-bot.com/v1.0/devices' \                  
  --header 'Authorization: {SWITCHBOT_TOKEN}' \
  --header 'Content-Type: application/json; charset=utf8'
  ```
