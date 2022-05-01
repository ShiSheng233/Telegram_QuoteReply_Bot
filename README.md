# Telegram QuoteReply Bot

[![Docker Image CI](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml/badge.svg?branch=master)](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml)

A simple bot powered by [Telegram API](https://core.telegram.org/bots/api)
and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

We provide a sample bot at [@quote_reply_bot](https://t.me/quote_reply_bot).

## Deploy

### Python

```
git clone https://github.com/ShiSheng233/Telegram_QuoteReply_Bot.git && cd Telegram_QuoteReply_Bot

python3 main.py
```

### Docker

```shell
docker run -d --env BOT_TOKEN="YOUR TOKEN HERE" shisheng/telegram_quotereply_bot:ci_latest
```

### Vercel

> By XiaoMengXinX
