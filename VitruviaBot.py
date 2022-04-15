import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    # Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    programButton = types.KeyboardButton("See Program")
    exportButton = types.KeyboardButton("Export Program")
    downloadButton = types.KeyboardButton("Download Program")
    informationButton = types.KeyboardButton("Information")

    markup.add(programButton, exportButton, downloadButton)
    markup.add(informationButton)

    bot.send_message(message.chat.id, "Welcome, Corpsbrüder!".
                     format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def talk(message):
    if message.chat.type == 'private':
        if message.text == 'See Program':

            markup = types.InlineKeyboardMarkup()

            programButton = types.InlineKeyboardButton("All Program", callback_data='program')
            aprilButton = types.InlineKeyboardButton("April", callback_data='april')
            mayButton = types.InlineKeyboardButton("May", callback_data='may')
            juneButton = types.InlineKeyboardButton("June", callback_data='june')
            julyButton = types.InlineKeyboardButton("July", callback_data='july')
            augustButton = types.InlineKeyboardButton("August", callback_data='august')

            markup.add(programButton)
            markup.add(aprilButton, mayButton, juneButton, julyButton, augustButton)

            bot.send_message(message.chat.id, 'Do you want to see the whole program or just a separate month?',
                             reply_markup=markup)

        elif message.text == 'Export Program':
            bot.send_message(message.chat.id, 'Still working on it')
        elif message.text == 'Download Program':
            prog = open('program.pdf', 'rb')
            bot.send_message(message.chat.id, "My pleasure to help you 🍻")
            bot.send_document(message.chat.id, prog)
        elif message.text == 'Information':
            bot.send_message(message.chat.id, '<b><u>🍺 Corps Vitruvia 🍺</u></b>\n'
                                              '\n'
                                              '<b>Anschrift</b>\n'
                                              'Platzl 5\n'
                                              '80331\n'
                                              'München\n'
                                              '\n'
                                              '<b>Kontakte</b>\n'
                                              'Telefon: (089) 29 76 11\n'
                                              'E-Mail: cc@vitruvia.de\n'
                                              'Homepage: www.vitruvia.de\n'
                                              '\n'
                                              '<b>CC-Konto</b>\n'
                                              'IBAN: DE08 7015 0000 1003 0779 95\n'
                                              'Stadtsparkasse München\n'
                                              '\n'
                                              '<b>Beitragskonto</b>\n'
                                              'Philisterverein Vitruvia e.V.\n'
                                              'DE26 7406 1101 0500 2125 20\n'
                                              'Raiffeisenbank München\n'
                                              '\n'
                                              '<b>Die Chargierten im Sommersemester 2022</b>\n'
                                              'Senior  CB Staudenraus II  x@vitruvia.de\n'
                                              'Consenior  CB Heise  xx@vitruvia.de\n'
                                              'Sekretär  CB Kachan  xxx@vitruvia.de\n'
                                              'Fuchsmajor  IaCB Mészáros  fm@vitruvia.de\n'
                                              '\n'
                                              '\n'
                                              '\n'
                                              'This Bot was developed by @hopetobeneglected')
        else:
            bot.send_message(message.chat.id, 'Stärk dich!')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'april':
                bot.send_message(call.message.chat.id, 'April events:')
                bot.send_message(call.message.chat.id, '<u>KW 16 (18.04. - 24.04.)</u>\n'
                                                       '23. Sa    16 hst Semesterantritts-CC*\n'
                                                       '<b>23. Sa    20 hct Semesterantrittskneipe</b>\n'
                                                       '\n'
                                                       '<u>KW 17 (25.04. - 01.05.)</u>\n'
                                                       '29. Fr    19 hmct Gin-Tasting ❤\n')
            elif call.data == 'may':
                bot.send_message(call.message.chat.id, 'May events:')
                bot.send_message(call.message.chat.id, '<u>KW 18 (02.05. - 08.05.)</u>\n'
                                                       '03. Di    20 hst 1. oCC*\n'
                                                       '\n'
                                                       '<u>KW 19 (09.05. - 15.05.)</u>\n'
                                                       '<b>12.-15.  170. Stiftungsfest Teutonia Stuttgart</b>\n'
                                                       '\n'
                                                       '<u>KW 20 (16.05. - 22.05.)</u>\n'
                                                       '17. Di    20 hst 2. oCC*\n'
                                                       '19. Do   20 hst 1. eCC*\n'
                                                       '\n'
                                                       '<u>KW 21 (23.05. - 29.05.)</u>\n'
                                                       '<b>26.-29.   Weinheimtagung</b>\n'
                                                       '\n'
                                                       '<u>KW 22 (30.05. - 05.06.)</u>\n'
                                                       '31. Di    20 hst 3. oCC*\n')
            elif call.data == 'june':
                bot.send_message(call.message.chat.id, 'June events:')
                bot.send_message(call.message.chat.id, '<u>KW 22 (30.05. - 05.06.)</u>\n'
                                                       '02. Do    17 hst 1. Stammtisch*\n'
                                                       '\n'
                                                       '<u>KW 23 (06.06. - 12.06.)</u>\n'
                                                       '<b>09.-12.   159. Bundesfest</b>\n'
                                                       '<b>09. Do    18 hst Wallbergabend ❤</b>\n'
                                                       '<b>10. Fr     18 hmct Festlicher bayerischer Abend ❤</b>\n'
                                                       '<b>11. Sa    14 hst Bundesconvent*</b>\n'
                                                       '<b>               20 hst Bundesfestkneipe</b>\n'
                                                       '<b>12. So    11 hst Totenehrung auf dem Wallberg ❤</b>\n'
                                                       '\n'
                                                       '<u>KW 24 (13.06. - 19.06.)</u>\n'
                                                       '14. Di    20 hst 4. oCC*\n'
                                                       '<b>16.-19.  154. Stiftungsfest MontaniaClausthal</b>\n'
                                                       '\n'
                                                       '<u>KW 25 (20.06. - 26.06.)</u>\n'
                                                       '21. Di    20 hst 2. eCC*\n'
                                                       '\n'
                                                       '<u>KW 26 (27.06. - 03.07.)</u>\n'
                                                       '28. Di    20 hst 5. oCC*\n')
            elif call.data == 'july':
                bot.send_message(call.message.chat.id, 'July events:')
                bot.send_message(call.message.chat.id, '<u>KW 27 (04.07. - 10.07.)</u>\n'
                                                       '07. Do    17 hst 2. Stammtisch*\n'
                                                       '08.-10.   Aktivenausflug zu unserem lieben AH Westermann*\n'
                                                       '\n'
                                                       '<u>KW 28 (11.07. - 17.07.)</u>\n'
                                                       '12. Di     20 hst 6. oCC*\n'
                                                       '14. Do    20 hst 3. eCC*\n'
                                                       '\n'
                                                       '<u>KW 29 (18.07. - 24.07.)</u>\n'
                                                       '23. Sa    16 hst Semesterabschluss-CC*\n'
                                                       '<b>23. Sa    20 hct Semesterabschlusskneipe</b>\n')
            elif call.data == 'august':
                bot.send_message(call.message.chat.id, 'August events:')
                bot.send_message(call.message.chat.id, '<u>KW 34 (22.08. - 28.08.)</u>\n'
                                                       '27. Sa    Segeln mit dem ASV')
            elif call.data == 'program':
                bot.send_message(call.message.chat.id, '<b>Semesterprogramm SoSe 2022:</b>')
                bot.send_message(call.message.chat.id, '<b>April 2022</b>:\n'
                                                       '\n'
                                                       '<u>KW 16 (18.04. - 24.04.)</u>\n'
                                                       '23. Sa    16 hst Semesterantritts-CC*\n'
                                                       '<b>23. Sa    20 hct Semesterantrittskneipe</b>\n'
                                                       '\n'
                                                       '<u>KW 17 (25.04. - 01.05.)</u>\n'
                                                       '29. Fr    19 hmct Gin-Tasting ❤\n'
                                                       '\n'
                                                       '\n'
                                                       '<b>Mai 2022</b>:\n'
                                                       '\n'
                                                       '<u>KW 18 (02.05. - 08.05.)</u>\n'
                                                       '03. Di    20 hst 1. oCC*\n'
                                                       '\n'
                                                       '<u>KW 19 (09.05. - 15.05.)</u>\n'
                                                       '<b>12.-15.  170. Stiftungsfest Teutonia Stuttgart</b>\n'
                                                       '\n'
                                                       '<u>KW 20 (16.05. - 22.05.)</u>\n'
                                                       '17. Di    20 hst 2. oCC*\n'
                                                       '19. Do   20 hst 1. eCC*\n'
                                                       '\n'
                                                       '<u>KW 21 (23.05. - 29.05.)</u>\n'
                                                       '<b>26.-29.   Weinheimtagung</b>\n'
                                                       '\n'
                                                       '<u>KW 22 (30.05. - 05.06.)</u>\n'
                                                       '31. Di    20 hst 3. oCC*\n'
                                                       '\n'
                                                       '\n'
                                                       '<b>Juni 2022</b>:\n'
                                                       '\n'
                                                       '<u>KW 22 (30.05. - 05.06.)</u>\n'
                                                       '02. Do    17 hst 1. Stammtisch*\n'
                                                       '\n'
                                                       '<u>KW 23 (06.06. - 12.06.)</u>\n'
                                                       '<b>09.-12.   159. Bundesfest</b>\n'
                                                       '<b>09. Do    18 hst Wallbergabend ❤</b>\n'
                                                       '<b>10. Fr     18 hmct Festlicher bayerischer Abend ❤</b>\n'
                                                       '<b>11. Sa    14 hst Bundesconvent*</b>\n'
                                                       '<b>               20 hst Bundesfestkneipe</b>\n'
                                                       '<b>12. So    11 hst Totenehrung auf dem Wallberg ❤</b>\n'
                                                       '\n'
                                                       '<u>KW 24 (13.06. - 19.06.)</u>\n'
                                                       '14. Di    20 hst 4. oCC*\n'
                                                       '<b>16.-19.  154. Stiftungsfest MontaniaClausthal</b>\n'
                                                       '\n'
                                                       '<u>KW 25 (20.06. - 26.06.)</u>\n'
                                                       '21. Di    20 hst 2. eCC*\n'
                                                       '\n'
                                                       '<u>KW 26 (27.06. - 03.07.)</u>\n'
                                                       '28. Di    20 hst 5. oCC*\n'
                                                       '\n'
                                                       '\n'
                                                       '<b>Juli 2022</b>\n'
                                                       '\n'
                                                       '<u>KW 27 (04.07. - 10.07.)</u>\n'
                                                       '07. Do    17 hst 2. Stammtisch*\n'
                                                       '08.-10.   Aktivenausflug zu unserem lieben AH Westermann*\n'
                                                       '\n'
                                                       '<u>KW 28 (11.07. - 17.07.)</u>\n'
                                                       '12. Di     20 hst 6. oCC*\n'
                                                       '14. Do    20 hst 3. eCC*\n'
                                                       '\n'
                                                       '<u>KW 29 (18.07. - 24.07.)</u>\n'
                                                       '23. Sa    16 hst Semesterabschluss-CC*\n'
                                                       '<b>23. Sa    20 hct Semesterabschlusskneipe</b>\n'
                                                       '\n'
                                                       '\n'
                                                       '<b>August 2022</b>\n'
                                                       '\n'
                                                       '<u>KW 34 (22.08. - 28.08pip freeze > requirements.txt.)</u>\n'
                                                       '27. Sa    Segeln mit dem ASV')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="See Program", reply_markup=None)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

