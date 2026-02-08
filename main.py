import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    ChatJoinRequestHandler,
)

# ================= HARD CODED TOKEN =================
BOT_TOKEN = "8594131409:AAEOcu4p9jtVComE8peujlsh9kZJW08MtvE"
# ====================================================

APK_PATH = "𝐓𝐊_𝐂𝐋𝐔𝐁_𝐏𝐀𝐍𝐍𝐄𝐋_𝐇𝐀𝐂𝐊.apk"
IMAGE_PATH = "HACK_PROOF.jpeg"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def approve_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request
    if not request:
        return

    user = request.from_user
    chat_id = request.chat.id

    # ❌ AUTO APPROVE DISABLED
    # await context.bot.approve_chat_join_request(
    #     chat_id=chat_id,
    #     user_id=user.id
    # )

    # ---------- GREETING DM ----------
    welcome_message = f"""
👋🏻 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 {user.mention_html()} হ্যালো 🤗 TK ক্লাব হ্যাক সার্ভিসে আপনাকে স্বাগতম | 🤑💵
"""

    await context.bot.send_message(
        chat_id=user.id,
        text=welcome_message,
        parse_mode="HTML",
    )

    # ---------- SEND APK ----------
    if os.path.exists(APK_PATH):
        with open(APK_PATH, "rb") as apk:
            await context.bot.send_document(
                chat_id=user.id,
                document=apk,
                caption="""
📂 ☆𝟏𝟎𝟎% 𝐍𝐔𝐌𝐁𝐄𝐑 𝐇𝐀𝐂𝐊💸

(১০০% নম্বর হ্যাক সকল ব্যবহারকারীর জন্য )💎
(১০০% ক্ষতিপূরণ নিশ্চিত)🧬

♻সাহায্যের জন্য - @TKCLUB_JAMES_ASSISTANT

🔴হ্যাকটি কীভাবে ব্যবহার করবেন
https://t.me/rajaindiaprediction/65
"""
            )

    # ---------- SEND VOICE ----------
        # ---------- SEND IMAGE ----------
    if os.path.exists(IMAGE_PATH):
        with open(IMAGE_PATH, "rb") as img:
            await context.bot.send_photo(
                chat_id=user.id,
                photo=img,
                caption="""
🎙 ৯ গুণ লাভের সদস্য প্রমাণপত্র 👇🏻
https://t.me/tkclub_numbershot/6?single

♻সাহায্যের জন্য- @TKCLUB_JAMES_ASSISTANT
ধারাবাহিক বিজয়ী সংখ্যা 🤑♻👑
"""
            )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_and_send))

    # ✅ JOIN REQUEST UPDATES ONLY
    app.run_polling(allowed_updates=["chat_join_request"])

if __name__ == "__main__":
    main()






