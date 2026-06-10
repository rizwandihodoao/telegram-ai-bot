from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from google import genai

BOT_TOKEN = "8545517929:AAHp3YB1An2fbzQxn8r-Tg1-PYszjQld0aI"
GEMINI_API_KEY = "AQ.Ab8RN6IfMusr2Wq3Zq5IxJMP2VIJZyKeMmDvaxEUBhsxENT7SA"

client = genai.Client(api_key=GEMINI_API_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_text
    )

    await update.message.reply_text(response.text)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot started...")

if __name__ == "__main__":
    app.run_polling()
