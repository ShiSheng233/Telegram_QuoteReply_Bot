# Telegram QuoteReply Bot

[![Docker Image CI](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml/badge.svg?branch=master)](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml)

A simple bot powered by [Telegram API](https://core.telegram.org/bots/api)
and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

## Deploy

### Docker

```shell
docker run -d shisheng/telegram_quotereply_bot:ci_latest -e BOT_TOKEN= **Your Bot Token**
```

### Vercel

> By XiaoMengXinX
