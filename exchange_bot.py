#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
from telegram import __version__ as TG_VER
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


class ExchangeBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()

        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CallbackQueryHandler(self.button))
        self.application.add_handler(CommandHandler("help", self.help_command))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Sends a message with three inline buttons attached."""
        keyboard = [
            [
                InlineKeyboardButton("Buy", callback_data="1"),
                InlineKeyboardButton("Sell", callback_data="2"),
            ],
            [InlineKeyboardButton("My History", callback_data="3")],
            [InlineKeyboardButton("Help", callback_data="3")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("A Simple Bot to Buy/Sell Currencies with IRR(Toman):", reply_markup=reply_markup)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        await query.answer()

        await query.edit_message_text(text=f"Selected option: {query.data}")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Displays info on how to use the bot."""
        await update.message.reply_text("Use /start this bot to buy/sell other currencies via IRR (IRANIAN Currency = TOMAN).")

    def run(self) -> None:
        """Run the bot."""
        # Run the bot until the user presses Ctrl-C
        self.application.run_polling()
