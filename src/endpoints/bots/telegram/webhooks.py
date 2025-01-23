## \file /src/endpoints/bots/telegram/webhooks.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Телеграм бот через сервер FastAPI через RPC
====================================================

.. module:: src.endpoints.bots.telegram.webhooks
    :platform: Windows, Unix
    :synopsis: Функции вебхуков Телеграма

"""
import asyncio
from fastapi import Request, Response
from telegram import Update
from telegram.ext import Application
import json
from src.logger import logger


def telegram_webhook(request: Request, application: Application):
    """"""
    asyncio.run(telegram_webhook_async(request, application))

async def telegram_webhook_async(request: Request, application: Application):
    """Handle incoming webhook requests."""
    return request

    try:
        data = await request.json()
        async with application:
            update = Update.de_json(data, application.bot)
            await application.process_update(update)
        return Response(status_code=200)
    except json.JSONDecodeError as ex:
        logger.error(f'Error decoding JSON: ', ex)
        return Response(status_code=400, content=f'Invalid JSON: {ex}')
    except Exception as ex:
        logger.error(f'Error processing webhook: {type(ex)} - {ex}')
        return Response(status_code=500, content=f'Error processing webhook: {ex}')