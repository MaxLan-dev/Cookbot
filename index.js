const TelegramBot = require('node-telegram-bot-api');
const token = '6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4'; // Replace with your own bot token
const bot = new TelegramBot(token, { polling: true });
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    const messageText = msg.text;
    console.log("i hjav");
    // Process the incoming message here
  
  });
  bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    const messageText = msg.text;
  
    if (messageText === '/start') {
      bot.sendMessage(chatId, 'Welcome to the bot!');
    }
  });