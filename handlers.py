import re

from telegram import (ForceReply, InlineKeyboardButton, InlineKeyboardMarkup,
                      KeyboardButton, ReplyKeyboardMarkup, TelegramError,
                      Update, ParseMode)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, Handler, MessageHandler, Updater)

from member_bot.config import Config

class Steps:
    PRODUCT_COUNT_STEP, ORDER_CONFIRM_STEP, PAYMENT_VERIFY_STEP, SUCCESSFUL_PAYMENT_STEP = ["PRODUCT_ORDER_STEP_"+str(i) for i in range(4)]
    

def start_handler(update, context) -> None:
    main_menu_keyboard = [
        [KeyboardButton("لیست محصولات 📦")],
        [
            KeyboardButton("کیف پول 💰"),
            KeyboardButton("پیگیری سفارش 🔍"),
        ],
        [
            KeyboardButton("انتخاب 📲"),
            KeyboardButton("اطلاعات کاربری 👤"),
        ],
        [KeyboardButton("تماس با ما 📞")],
    ]
    
    reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard,
                                        resize_keyboard=True,
                                        one_time_keyboard=True)

    start_message = "یکی از گزینه های زیر را انتخاب کنید :"

    update.message.reply_text(text=start_message,
                                reply_markup=reply_kb_markup)

def help_command(update, context) -> None:
    update.message.reply_text("لطفا از /start ربات اجرای ربات استفاده کنید.")


def button(update, context) -> None:
    button_text = update._effective_message.text
    reply_message = ""

    keyboard = []
    
    user_id = update._effective_message.chat_id
    wallet_balance = 100000000 or Config.WALLETS_DATA.get(user_id, 0)
    user_orders = [151,1515,51,51,51,1,51] or Config.ORDERS.get(user_id, [])
    do_force_reply = False

    try:
        member = context.bot.get_chat_member(Config.CHANNEL_ID, user_id)
    except TelegramError:
        print("ERROR")
    
    # if member.status == "left":
    #     print("user is NOT joined")
    #     reply_message = "لطفا به کانال جوین شوید @some_chaneel"

    if button_text == "لیست محصولات 📦":
        for product in Config.PRODUCT_BUTTONS:
            keyboard.append([KeyboardButton(product)])
        reply_message = "لطفا نوع محصول مورد نظر خود را انتخاب کنید :"
    
    elif button_text == "کیف پول 💰":
        """ add charge wallet buttom """
        keyboard.append([KeyboardButton("شارژ حساب 🔋")])
        reply_message = f"""
        📥 برای استفاده از خدمات ربات می بایست ابتدا کیف پول خود را شارژ کرده و سپس نسبت به سفارش محصولات مورد نظر خود اقدام کنید.

        💰 موجودی کیف پول شما در حال حاضر :
        {wallet_balance} تومان
        """
    
    elif button_text == "پیگیری سفارش 🔍":
        reply_message = "لطفا کد پیگیری سفارش خود را ارسال کنید"
        do_force_reply = True
    
    elif button_text == "انتقال 📲":
        reply_message = f"""
        💳 مبلغ مورد نظر برای انتقال را وارد کنید:

        موجودی حساب شما {wallet_balance} تومان می باشد."""
        do_force_reply = True
    
    elif button_text == "اطلاعات کاربری 👤":
        
        reply_message = f"""
        👤 اطلاعات کاربری: 

        👤 شناسه کاربری: {user_id}
        💰 موجودی: {wallet_balance} تومان
        🛍 تعداد سفارشات: {len(user_orders)} عدد
        """
    
    elif button_text == "تماس با ما 📞":
        reply_message = Config.CONTACT_MESSAGE
    
    keyboard.append([KeyboardButton("بازگشت به منوی اصلی ◀️")])
    reply_keyboard_markup = ReplyKeyboardMarkup(keyboard,
                                        resize_keyboard=True,
                                        one_time_keyboard=True)
    
    update.message.reply_text(text=reply_message, reply_markup= ForceReply() if do_force_reply else reply_keyboard_markup)


def product_button_handler(update, context):
    button_text = update._effective_message.text
    reply_message = "لطفا محصول مورد نظر خود را انتخاب کنید :"

    keyboard = []
    
    if button_text == "تلگرام":
        products =  Config.TELEGRAM_PRODUCT_BUTTONS
    elif button_text == "اینستاگرام":
        products =  Config.INSTAGRAM_PRODUCT_BUTTONS
    
    for product in products:
            keyboard.append([KeyboardButton(product)])

    keyboard.append([KeyboardButton("بازگشت به منوی اصلی ◀️")])
    reply_keyboard_markup = ReplyKeyboardMarkup(keyboard,
                                        resize_keyboard=True,
                                        one_time_keyboard=True)
    
    update.message.reply_text(text=reply_message, reply_markup=reply_keyboard_markup)


def product_choose_handler(update, context):
    button_text = update._effective_message.text
    
    product = Config.PRODUCTS[button_text]

    reply_message = Config.PRODUCT_COUNT.format(button_text, product["product_description"],
                                                product["product_price"], product["product_min"],
                                                product["product_max"])

    keyboard = []

    keyboard.append([KeyboardButton("بازگشت به منوی اصلی ◀️")])
    
    update.message.reply_text(text=reply_message, parse_mode=ParseMode.HTML)
    return Steps.PRODUCT_COUNT_STEP


def order_confirm_handler(update, context):
    update_message = update.message
    reply_to_message = update.message.reply_to_message
    # reply_header = reply_to_message.text.split()[0]
    
    min_count = re.findall('⬇️ (\d+)', reply_to_message)[0]
    max_count = re.findall('⬆️ (\d+)', reply_to_message)[0]
    product_price = re.findall("💵 (\d+) تومان", reply_to_message)[0]

    try:
        product_count = int(update_message)
    except ValueError:
        # TODO: show error ask again
        return

    total_price = product_count * product_count
    if  min_count <= product_count <= max_count:
        respose = Config.ORDER_CONFIRM
        respose.format(product_count, product_count, total_price)
        update.message.reply_text(text='fads', reply_markup=ForceReply())
    
    return Steps.ORDER_CONFIRM_STEP

# TODO: make send_to_admins a decorator to send message to admind to
def send_to_admins_action(update, context):
    update_message = update.message
    reply_to_message = update.message.reply_to_message
    for admin_id in Config.ADMIN_IDS:
        reply_to_message.forward(chat_id=admin_id)
        update_message.forward(chat_id=admin_id)
    update.message.reply_text(text=f'Your message sent to admin.')


def get_group_link_action(update, context):
    pass
