from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Ambil token dari environment variable (Railway akan mengatur ini)
TOKEN = os.getenv("7624457765:AAGWVct5zgwUDYg1JUzx8R8tzH2B3ETB3u0")

def start(update: Update, context: CallbackContext) -> None:
    # Ganti dengan URL website Anda
    website_url = "https://rebrand.ly/bbtop"
    
    # Buat tombol inline
    keyboard = [
        [InlineKeyboardButton("🌐 Kunjungi Website", url=website_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Kirim pesan + tombol
    update.message.reply_text(
        "Halo! Klik tombol di bawah untuk membuka website kami:",
        reply_markup=reply_markup
    )

def main() -> None:
    # Gunakan `Updater` dengan webhook jika di-deploy
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # Tambahkan handler untuk command /start
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Jika di-deploy di Railway (gunakan webhook)
    if "RAILWAY_ENVIRONMENT" in os.environ:
        PORT = int(os.getenv("PORT", 8443))
        APP_NAME = os.getenv("RAILWAY_PROJECT_NAME")
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"https://{APP_NAME}.railway.app/{TOKEN}"
        )
    else:
        # Mode polling (untuk development lokal)
        updater.start_polling()
    
    updater.idle()

if __name__ == "__main__":
    main()
