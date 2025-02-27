from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# Bot Token (Replace with your bot token)
BOT_TOKEN =8002542797:AAGAREQHRnvQ7GREjkAIKUCQ-zETREvZKjQ

# Verification & Sponsored Links
VERIFICATION_LINKS = [
    ("📢 Join Channel", "https://t.me/Income_Genius_Community"),
    ("💬 Join Group", "https://t.me/Income_Genius_CommunityChat"),
    ("🤖 Start Reffer Me Bot", "https://t.me/Reffer_me_bot"),
    ("🎥 Subscribe YouTube", "https://www.youtube.com/@Mr.Income_genius"),
    ("🎞 Watch Sponsored Video", "https://youtube.com/shorts/zVkPozZ4Bw8?si=KiIvW1qRla6_F-9H"),
    ("🔥 Join Sponsored YT", "https://youtube.com/@phf-fun-and-comedy"),
    ("📞 WhatsApp Contact", "wa.me/8801719705085"),
]

# Auto-reply & auto-post settings
auto_reply_enabled = {}
auto_post_enabled = {}

# Verified Users
verified_users = set()

def start(update: Update, context: CallbackContext):
    """Send a welcome message with verification buttons."""
    keyboard = [[InlineKeyboardButton(text, url=link)] for text, link in VERIFICATION_LINKS]
    keyboard.append([InlineKeyboardButton("✅ Check🔁", callback_data="check_join")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "🚀 **Welcome to GeniusGPT 7.5!**\n\n"
        "🔹 To use this bot, complete the verification steps below:\n"
        "🔸 Join the Telegram **Channel & Group**\n"
        "🔸 Start the **Reffer Me Bot**\n"
        "🔸 Subscribe & Watch **YouTube Sponsored Content**\n"
        "🔸 Contact on **WhatsApp** if needed\n\n"
        "✅ **Click 'Check🔁' after completing these steps.**",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )

def check_join(update: Update, context: CallbackContext):
    """Check if the user is verified."""
    query = update.callback_query
    user_id = query.from_user.id

    # Simulated verification (Replace with actual API checks)
    verified_users.add(user_id)
    
    query.answer("✅ Verification successful! You can now use the bot.")
    query.edit_message_text("✅ You are verified! Use /start to begin.")

def start_reply(update: Update, context: CallbackContext):
    """Enable auto-reply in a group."""
    chat_id = update.message.chat_id
    auto_reply_enabled[chat_id] = True
    update.message.reply_text("✅ Auto-reply started in this group!")

def stop_reply(update: Update, context: CallbackContext):
    """Disable auto-reply in a group."""
    chat_id = update.message.chat_id
    auto_reply_enabled[chat_id] = False
    update.message.reply_text("❌ Auto-reply stopped in this group.")

def start_post(update: Update, context: CallbackContext):
    """Enable auto-posting in a channel."""
    chat_id = update.message.chat_id
    auto_post_enabled[chat_id] = True
    update.message.reply_text("✅ Auto-posting started in this channel!")

def stop_post(update: Update, context: CallbackContext):
    """Disable auto-posting in a channel."""
    chat_id = update.message.chat_id
    auto_post_enabled[chat_id] = False
    update.message.reply_text("❌ Auto-posting stopped in this channel.")

def auto_reply(update: Update, context: CallbackContext):
    """Handle auto-replies in enabled groups."""
    chat_id = update.message.chat_id
    if auto_reply_enabled.get(chat_id, False):
        update.message.reply_text("🤖 This is an automated reply!")

def copy_post(update: Update, context: CallbackContext):
    """Copy posts from selected sources and post in the channel."""
    chat_id = update.message.chat_id
    if auto_post_enabled.get(chat_id, False):
        context.bot.send_message(chat_id, f"📢 Forwarding message:\n{update.message.text}")

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("startreply", start_reply))
    dp.add_handler(CommandHandler("stopreply", stop_reply))
    dp.add_handler(CommandHandler("startpost", start_post))
    dp.add_handler(CommandHandler("stoppost", stop_post))

    # Handlers for auto-reply and copying posts
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, copy_post))

    # Callback for verification button
    dp.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()