from telegram import __version__ as TG_VER

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

class TelegramChatBot:
    def __init__(self, token, chat_gpt_api_key_registrar):
        self.token = token
        self.application = None
        self.callback = None
        self.chat_gpt_api_key_registrar = chat_gpt_api_key_registrar

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Help!")

    async def register_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        tokens = update.message.text.split(' ')
        if(len(tokens)>1):
            self.chat_gpt_api_key_registrar(user['id'], user['username'], tokens[1])
            await update.message.reply_text(user['username'] + " is registered now!")    
        else:
            await update.message.reply_text("Could not register your api_key!!!")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
        if self.callback:
            await update.message.reply_text(self.callback(user['id'], update.message.text))
        else:
            await update.message.reply_text(update.message.text)

    def set_message_handler(self, message_handler):
        self.callback = message_handler
    
    def remove_message_handler(self):
        self.callback = None

    def run(self) -> None:
        """Start the bot."""
        self.application = Application.builder().token(self.token).build()

        # on different commands - answer in Telegram
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("register", self.register_command))

        # on non command i.e message - echo the message on Telegram
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        # Run the bot until the user presses Ctrl-C
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
