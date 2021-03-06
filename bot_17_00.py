#-------laska2
#!/usr/bin/env python
#____laska
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    kb = [[InlineKeyboardButton("Кафедра КМАД", callback_data = "kafedra")],
          [InlineKeyboardButton("Можливості для студентів", callback_data = "mozhluv")],
          [InlineKeyboardButton("Умови вступу", callback_data = "umovy")]]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text('Hi!', reply_markup = reply)
    


def help(update, context):
    update.message.reply_text('Help!')

def kafedra(update, context):
    
    kb = [[InlineKeyboardButton("Викладачі",callback_data = "vikladachu")],
           [InlineKeyboardButton("Принципи навчання на кафедрі",callback_data = "prictsipi")],
           [InlineKeyboardButton("Історія кафедри",callback_data = "istoria")],
           [InlineKeyboardButton("Аудиторії кафедрии",callback_data = "auditoria")],
           [InlineKeyboardButton("Наші випускники",callback_data = "vipuskniki")]]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text("З чого почнемо?",reply_markup = reply)

    
def umovy(update, context):
    update.callback_query.message.reply_text('Обери підпункт, який тобі цікавиий')
    kb =[[InlineKeyboardButton("Конкурсні предмети ЗНО", callback_data = "...")],
        [InlineKeyboardButton("Розрахунок конкурсного балу", callback_data = "...")],
        [InlineKeyboardButton("Етапи вступної кампанії", callback_data = "...")],
        [InlineKeyboardButton("Корисні посилання", callback_data = "...")],
        [InlineKeyboardButton("Кількість бюджетних та контрактних місць для вступників", callback_data = "...")],
        ]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text("Обери підпункт, який тобі цікавиий",reply_markup = reply)    

    
    
   
def mozhluv(update, context):

    kb1 = [[InlineKeyboardButton('Проєктне навчання',callback_data = ''))],
          [InlineKeyboardButton('Дуальна освіта', callback_data = '')],
          [InlineKeyboardButton('Працевлаштування',callback_data = '')],
          [InlineKeyboardButton('Практика',callback_data = '')]]
    reply = InlineKeyboardMarkup(kb1)
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?', reply_markup = reply)


def umovy(update, context):
    update.callback_query.message.reply_text("...")

def proect(update, context):
    update.callback_query.message.reply_text("...")

def osvita(update, context):
    update.callback_query.message.reply_text("...")

def prahe(update, context):
    update.callback_query.message.reply_text("...")

def practik(update, context):
    update.callback_query.message.reply_text("...")
    
def zno(update, context):
    update.callback_query.message.reply_text("..."))

def bali(update, context):
    update.callback_query.message.reply_text("...")

def vstup(update, context):
    update.callback_query.message.reply_text("...")
    
def posilannya(update, context):
    update.callback_query.message.reply_text("...")

def kontract(update, context):
    update.callback_query.message.reply_text("...")
    
    
def vikladachi(update, context):
    update.callback_query.message.reply_text('...')

def prinzipi(update, context):
    update.callback_query.message.reply_text('...')

def istoria(update, context):
    update.callback_query.message.reply_text('...')

def auditoriyi(update, context):
    update.callback_query.message.reply_text('...')

def vipuskniki(update, context):
    update.callback_query.message.reply_text('...')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("1622026876:AAGSPO1cWixVtEb0Zw8PKJxNa-KfQUh7818", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(mozhluv,pattern = "mozhluv"))
    dp.add_handler(CallbackQueryHandler(umovy,pattern = "umovy"))
    
    dp.add_handler(CallbackQueryHandler(vikladachi, pattern = 'vikladachi'))
    dp.add_handler(CallbackQueryHandler(prinzipi, pattern = 'prinzipi'))
    dp.add_handler(CallbackQueryHandler(istoria, pattern = 'istoria'))
    dp.add_handler(CallbackQueryHandler(auditoriyi, pattern = 'auditoriyi'))
    dp.add_handler(CallbackQueryHandler(vipuskniki, pattern = 'vipuskniki'))
    
    dp.add_handler(CallbackQueryHandler(proect,pattern = "proect"))
    dp.add_handler(CallbackQueryHandler(osvita,pattern = "osvita"))
    dp.add_handler(CallbackQueryHandler(prahe,pattern = "prahe"))
    dp.add_handler(CallbackQueryHandler(practik,pattern = "practik"))
    
    dp.add_handler(CallbackQueryHandler(zno, pattern = "zno"))
    dp.add_handler(CallbackQueryHandler(bali, pattern = "bali"))
    dp.add_handler(CallbackQueryHandler(vstup, pattern = "vstup"))
    dp.add_handler(CallbackQueryHandler(posilannya, pattern = "posilannya"))
    dp.add_handler(CallbackQueryHandler(kontract, pattern = "kontract"))




    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
