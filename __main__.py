import logging
import os

import dotenv
from telegram import (ForceReply, InlineKeyboardButton, InlineKeyboardMarkup,
                      KeyboardButton, ReplyKeyboardMarkup, TelegramError,
                      Update)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, ConversationHandler, Handler,
                          MessageHandler, Updater)
from telegram.ext.filters import Filters

from member_bot.config import Config
from member_bot.handlers import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

wallets_data = {}
orders = {}

def main():
    dotenv.load_dotenv()
    TOKEN = os.environ["BOT_TOKEN"]
    updater = Updater(TOKEN)

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text(Config.TELEGRAM_PRODUCT_BUTTONS + Config.INSTAGRAM_PRODUCT_BUTTONS), product_choose_handler)],

        states={
            Steps.PRODUCT_COUNT_STEP: [MessageHandler(
                Filters.text,
                order_confirm_handler
            )],
            # Steps.ORDER_CONFIRM_STEP: [MessageHandler(
            #     Filters.text,
                
            # )]
        },

        fallbacks=[CommandHandler('start', start_handler)]
    )

    
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start_handler))
    updater.dispatcher.add_handler(CommandHandler('cancel', start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text(Config.MAIN_MENU_BUTTONS), button))
    
    updater.dispatcher.add_handler(MessageHandler(Filters.text(Config.PRODUCT_BUTTONS), product_button_handler))

    updater.dispatcher.add_handler(MessageHandler(Filters.text("بازگشت به منوی اصلی ◀️"), start_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, help_command))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
