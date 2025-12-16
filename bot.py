from telegran import Update

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): context.user_data["number"] = random.randint(1, 5) context.user_data["score"] = 0 await update.message.reply_text( ) "Son topish o'yini!\n" "1 dan 5 son oyladin.\n" "Topish uchun: /top 5"

async def top(update: Update, context: ContextTypes. DEFAULT_TYPE): if "number" not in context.user_data: await update.message.reply_text("Avval/start bos.") return

try:

user_number = int(context.args[0]) secret context.user_data["number"]

if user_number secret: context.user_data["score"] += 1 score context.user_data["score"] await update.message.reply_text( ) f" To'g'ri!\n" f Ball: {score}\n" f"Yangi son o'yladin!" context.user_data["number"] random.randint(1, 10)

else:

await update.message.reply_text("X Noto'g'ri, yana urinib ko'r.")

except:

await update.message.reply_text("To'g'ri yoz: /top 5")

async def stat (update: Update, context: ContextTypes.DEFAULT_TYPE): score context.user_data.get("score", 0) await update.message.reply_text( f" Statistika:\n" f ) Jami ball: {score}"

app ApplicationBuilder().token("8010036299:AAH71B4QR9IrZh0gvd872ixJL7RMtEbrMhU").build()

app.add_handler (CommandHandler("start", start)) app.add_handler (CommandHandler("top", top)) app.add_handler(CommandHandler("sts", start))

Frint(" Bot ishga tushdi...") app.run_polling()
