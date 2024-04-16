import logging
import re
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Definir patrones de expresiones regulares
patron_origen_destino_fecha = r"Volar de (\w+) a (\w+) el (\d{1,2} de \w+)"
patron_precio = r"Cuánto cuesta un vuelo de (\w+) a (\w+)"
patron_ida_vuelta = r"Un vuelo de ida y vuelta de (\w+) a (\w+)"
patron_otros = r"El cumpleaños de (\w+) es el (\d{1,2} de \w+)"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def process_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process user queries based on regular expressions."""
    message_text = update.message.text
    if re.search(patron_origen_destino_fecha, message_text):
        origen_destino_fecha = re.search(patron_origen_destino_fecha, message_text)
        origen = origen_destino_fecha.group(1)
        destino = origen_destino_fecha.group(2)
        fecha = origen_destino_fecha.group(3)
        await update.message.reply_text(f"Buscar vuelo de {origen} a {destino} para el {fecha}")
    elif re.search(patron_precio, message_text):
        precio = re.search(patron_precio, message_text)
        origen = precio.group(1)
        destino = precio.group(2)
        await update.message.reply_text(f"Consultar precio de vuelo de {origen} a {destino}")
    elif re.search(patron_ida_vuelta, message_text):
        ida_vuelta = re.search(patron_ida_vuelta, message_text)
        origen = ida_vuelta.group(1)
        destino = ida_vuelta.group(2)
        await update.message.reply_text(f"Buscar vuelo de ida y vuelta de {origen} a {destino}")
    elif re.search(patron_otros, message_text):
        festejo_pe = re.search(patron_otros, message_text)
        origen = festejo_pe.group(1)
        destino = festejo_pe.group(2)
        await update.message.reply_text(f"Su cumpleaños de tu amigo {origen} es el {destino}")
    else:
        await update.message.reply_text("Lo siento, no puedo entender tu consulta.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6582861074:AAGaW4uCCtUI6CUIp-J1YjEJ_MKlUykJa0Y").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_query))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
