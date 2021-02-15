class Config:
    MAIN_MENU_BUTTONS = ["لیست محصولات 📦",
                        "کیف پول 💰",
                        "پیگیری سفارش 🔍",
                        "انتقال 📲",
                        "اطلاعات کاربری 👤",
                        "تماس با ما 📞"]
    PRODUCT_BUTTONS = ["تلگرام", "اینستاگرام"]
    TELEGRAM_PRODUCT_BUTTONS = ["telegram product 1",
                        "telegram product 2",
                        "telegram product 3",
                        "telegram product 4",
                        "telegram product 5",]
    INSTAGRAM_PRODUCT_BUTTONS = ["instagram product 1",
                        "instagram product 2",
                        "instagram product 3",]
    
    PRODUCT_COUNT="""
    نام محصول :
    {}
    قیمت هر واحد :
    💵 {} تومان
    حداقل میزان سفارش :
    ⬇️ {} عدد
    حداکثر میزان سفارش :
    ⬆️ {} عدد

    در صورت تایید تعداد مورد نظر خود را وارد کنید :
    —————————
    برای لغو درخواست دستور زیر را وارد کنید
    /cancel
    """

    ORDER_CONFIRM="""
    سفارش شما :
    {}
    تعداد :
    📥  {} عدد
    هزینه :
    💳  {} تومان

    برای ثبت نهایی سفارش و کسر از کیف پول لطفا لینک صفحه مورد نظر خود را وارد کنید :
    —————————
    برای لغو درخواست دستور زیر را وارد کنید
    /cancel
    """

    CONTACT_MESSAGE = """
        در این بخش می توانید تیکت خود را از طریق ربات برای پشتیبانی ارسال کنید .
        لطفا تیکت خود را در یک پیام ارسال بفرمایید.
        پیام ارسالی شما میتواند پیام متنی و یا یک پیام تصویری همراه با کپشن باشد.
        ارتباط با پشتیبانی :
        @some_Channel"""

    CHANNEL_ID = -1001456142759
    admin_ids = [178648151]

    PRODUCTS = {"telegram product 1":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "telegram product 2":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "telegram product 3":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "telegram product 4":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "telegram product 5":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "instagram product 1":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "instagram product 2":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },
                    "instagram product 3":{"product_description":"",
                                        "product_price":10,
                                        "product_min":1,
                                        "product_max":100
                                        },                                    
                    }
