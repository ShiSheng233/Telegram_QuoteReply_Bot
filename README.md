# Telegram QuoteReply Bot
[![Docker Image Release CI](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_latest_publish.yml/badge.svg)](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_latest_publish.yml) [![Docker Image Push CI](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml/badge.svg)](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_publish.yml) [![Docker Image Pull Request CI](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_pr_publish.yml/badge.svg)](https://github.com/ShiSheng233/Telegram_QuoteReply_Bot/actions/workflows/docker_image_pr_publish.yml)

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

<https://hub.docker.com/r/shisheng/telegram_quotereply_bot>

```shell
docker run -d --env BOT_TOKEN="YOUR TOKEN HERE" shisheng/telegram_quotereply_bot
```

Pull `shisheng/telegram_quotereply_bot:ci_pr_[pull_request.number]` for specific pull request's version

### Vercel

_Not very recommend_

> By XiaoMengXinX

1. Fork this repo and deploy to Vercel
2. Add a environment variable named `BOT_TOKEN`
3. Redeploy to make environment variables take effect
4. Set webhook method by accessing <https://api.telegram.org/bot[YOUR_TELEGRAM_BOT_TOKEN_HERE]/setWebhook?url=https://[YOUR_VERCEL_PROJ_NAME].vercel.app/api/bot>
