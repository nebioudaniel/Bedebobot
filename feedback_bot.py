import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# 1. Setup Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- CONFIGURATION ---
TOKEN = "8388535592:AAFFG0Ztl8waYYW4oQCOnISU-u6_8Rjx4Q0"
ADMIN_ID = "7173564024" 
# ---------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clean, Modern Welcome Message focused on Networking & AI."""
    keyboard = [
        [
            InlineKeyboardButton("⚠️ Study Struggles", callback_data='problem'),
            InlineKeyboardButton("💡 Dream Solution", callback_data='solution'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🚀 <b>Join the Future of Student Networking.</b>\n\n"
        "We are building a modern platform to help students <b>network, grow, and succeed</b> "
        "using the power of AI.\n\n"
        "If you're interested in being part of this, we want your raw thoughts. "
        "Help us build the tool <i>you</i> actually need."
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='HTML')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'problem':
        text = "<b>What is the biggest problem you face while studying?</b>\n(e.g., staying focused, finding resources, networking with the right people...)"
    else:
        text = "<b>If you could have any AI feature to help you grow, what would it be?</b>\n(Describe your 'dream solution' below!)"

    context.user_data['mode'] = query.data
    await query.edit_message_text(text=text, parse_mode='HTML')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Forwards feedback to the admin."""
    mode = context.user_data.get('mode', 'General')
    user = update.message.from_user
    feedback = update.message.text

    # Forwarding to Admin
    report_to_admin = (
        f"📩 <b>NEW FEEDBACK</b>\n\n"
        f"👤 <b>User:</b> {user.first_name} (@{user.username})\n"
        f"📂 <b>Category:</b> {mode.upper()}\n"
        f"📝 <b>Response:</b> {feedback}"
    )
    
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=report_to_admin, parse_mode='HTML')
    except Exception:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"Feedback from {user.first_name}: {feedback}")

    # Response to user
    keyboard = [[InlineKeyboardButton("🔙 Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✅ <b>Thank you!</b> Your feedback is incredibly valuable as we build this together.",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⚠️ Study Struggles", callback_data='problem'),
            InlineKeyboardButton("💡 Dream Solution", callback_data='solution'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("<b>What else would you like to share?</b>", reply_markup=reply_markup, parse_mode='HTML')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern='^(problem|solution)$'))
    application.add_handler(CallbackQueryHandler(back_to_start, pattern='^back$'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Networking & AI Feedback Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
