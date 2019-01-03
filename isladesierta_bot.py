# -*- coding: UTF-8 -*-

import telebot
import logging
import isladesierta
import unidecode

# CONSTANTS
TOKEN = ""

if __name__ == '__main__':
    logging.basicConfig(filename='isladesierta.log', filemode='a+', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',)
    logging.info("La Isla Desierta is starting...")

    isla = isladesierta.IslaDesierta()
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        logging.info(message)
        bot.send_message(message.chat.id, "Mañana te vas a una *isla desierta* ¿qué cosas puedes llevarte?\n" +
        "Usa el comando /mellevo para preguntar si puedes llevarte una cosa o no.\n" +
        "¡Consigue todo lo necesario para sobrevivir en la isla desierta!", parse_mode="Markdown")

    @bot.message_handler(commands=['mellevo'])
    def send_botes(message):
        logging.info(message)

        original_text = message.text.replace('/mellevo', '').strip()# ".join(message.text.split()[1:])
        if original_text == "":
            bot.reply_to(message, "Pregúntame por algo: /mellevo <cosa>")
            return
        text = original_text.lower()
        text = unidecode.unidecode(text)
        player = message.from_user

        ok = isla.ok(text, player.first_name)
        if ok:
            isla.add_word_player(text, player.id)
            bot.reply_to(message, player.first_name + " sí se puede llevar " + original_text + ".")
            if isla.player_win(player.id):
                isla.remove_player(player.id)
                bot.send_message(message.chat.id, "Enhorabuena " + player.first_name + "!! Podrás sobrevivir en la isla desierta con todo eso.\n"+
                "¿Te llevarías más cosas?", parse_mode="Markdown")
        else:
            isla.remove_player(player.id)
            bot.reply_to(message, player.first_name + " no se puede llevar " + original_text + ".")

    logging.info("La Isla Desierta is running...")
    bot.polling()
