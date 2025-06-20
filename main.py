from telegram.ext import Application, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

TOKEN = os.getenv("7624457765:AAGWVct5zgwUDYg1JUzx8R8tzH2B3ETB3u0")

async def start(update, context):
    # Kirim gambar (pastikan path benar)
    await update.message.reply_photo(
        photo=open("assets/hamster.jpg", "rb"),
        caption="🎮 Mainkan Sekarang Slot Paling Gacor Saat Ini!"
    )
    
    # Buat tombol
    keyboard = [[InlineKeyboardButton("▶️ PLAY NOW", url="https://rebrand.ly/bbtop")]]
    await update.message.reply_text(
        "Klik disini Untuk Lanjut Bermain!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    # Inisialisasi Application (ganti Updater)
    application = Application.builder().token(TOKEN).build()
    
    # Tambahkan handler
    application.add_handler(CommandHandler("start", start))
    
    # Untuk Railway (pakai webhook)
    if "RAILWAY_ENVIRONMENT" in os.environ:
        PORT = int(os.getenv("PORT", 8443))
        APP_NAME = os.getenv("RAILWAY_PROJECT_NAME")
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"https://{diligent-charisma}.railway.app/{webhook}"
        )
    else:
        # Mode polling (development)
        application.run_polling()

if __name__ == "__main__":
    main()
