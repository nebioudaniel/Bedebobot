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
    """The Big Vision Welcome Message."""
    keyboard = [
        [
            InlineKeyboardButton("✨ Share My Opinion", callback_data='opinion'),
            InlineKeyboardButton("💎 Pro Advice", callback_data='advice'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🌟 <b>Welcome to Bedebo (በደቦ) — The Future of Student Life.</b>\n\n"
        "We aren't just building an app; we are building an <b>Elite Student Economy</b>. "
        "Here is what's coming to your phone:\n\n"
        "💰 <b>REWARDS SYSTEM:</b> Get 'Bedebo Points' for helping others. Turn your knowledge into value.\n"
        "📈 <b>AI CAREER BOOST:</b> Instant AI coaching to help you pass exams and land top internships.\n"
        "⚡ <b>VIRAL FEED:</b> A TikTok-style campus feed that keeps you updated on everything trending.\n"
        "🏢 <b>EXCLUSIVE HUBS:</b> Private digital spaces for your University and Department.\n"
        "🛍️ <b>CAMPUS MARKET:</b> Buy, sell, and trade books or gear with students nearby.\n\n"
        "<b>The Bedebo Team</b> wants to know: Are you ready for this revolution?"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='HTML')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'opinion':
        text = "🚀 <b>The Vision:</b> What do you think about the <b>Rewards & Money</b> feature? Would that change your student life?"
    else:
        text = "💎 <b>The Strategy:</b> If you were running Bedebo, what is the first <b>BIG</b> feature you would launch to make it go viral?"

    context.user_data['mode'] = query.data
    await query.edit_message_text(text=text, parse_mode='HTML')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Forwards the gold mine of ideas to you."""
    mode = context.user_data.get('mode', 'General')
    user = update.message.from_user
    feedback = update.message.text

    # Forwarding to you
    report_to_admin = (
        f"👑 <b>NEW STRATEGIC FEEDBACK</b>\n\n"
        f"👤 <b>Visionary:</b> {user.first_name} (@{user.username})\n"
        f"📂 <b>Category:</b> {mode.capitalize()}\n"
        f"📝 <b>Idea:</b> {feedback}"
    )
    
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=report_to_admin, parse_mode='HTML')
    except Exception:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"New Strategy from {user.first_name}: {feedback}")

    # Response to user
    keyboard = [[InlineKeyboardButton("🔙 Back to Vision", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 <b>Amazing Idea!</b> Your thoughts have been sent straight to <b>The Bedebo Team</b>. We are building this for you.",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("✨ Share My Opinion", callback_data='opinion'), InlineKeyboardButton("💎 Pro Advice", callback_data='advice')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("<b>What else is on your mind?</b>", reply_markup=reply_markup, parse_mode='HTML')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern='^(opinion|advice)$'))
    application.add_handler(CallbackQueryHandler(back_to_start, pattern='^back$'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bedebo Vision Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()