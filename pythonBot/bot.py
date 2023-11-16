import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext


# Set your OpenAI API key
openai.api_key = "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"
# Define the Telegram bot token
TELEGRAM_TOKEN = '6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4'

# Define the handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your ChatGPT-powered bot. Send me a message, and I will respond.')

# Define the handler for incoming messages
def handle_message(update: Update, context: CallbackContext) -> None:
    # Get the user's message
    user_message = update.message.text

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=user_message,
        temperature=0.7,  # Adjust the temperature for different levels of creativity
        max_tokens=150,  # Limit the length of the response
        n=1  # Generate a single response
    )

    # Extract the generated response from OpenAI and send it to the user
    bot_response = response['choices'][0]['text']
    update.message.reply_text(bot_response)

# Set up the Telegram bot
def main() -> None:
    updater = Updater(TELEGRAM_TOKEN, update_queue=None, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Add message handler
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
