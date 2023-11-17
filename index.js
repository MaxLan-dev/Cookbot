
const TelegramBot = require('node-telegram-bot-api');

const token = '6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4'; // Replace with your own bot token
const bot = new TelegramBot(token, { polling: true });

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const messageText = msg.text;

  if (messageText === '/start') {
    bot.sendMessage(chatId, 'Welcome to the bot!');
  }
});
// const express = require('express');
// const fetch = require('node-fetch');
// const bodyParser = require('body-parser');

// const app = express();
// const port = 3000; // You can change this port if needed

// app.use(bodyParser.json());

// // Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
// const botToken = '6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4';

// app.post(`/webhook/${botToken}`, async (req, res) => {
//   const { message } = req.body;

//   if (message && message.text === '/start') {
//     const chatId = message.chat.id;
//     const responseText = 'Hello! Welcome to your Telegram bot.';

//     await sendMessage(chatId, responseText);
//   }

//   res.sendStatus(200);
// });

// async function sendMessage(chatId, text) {
//   const apiUrl = `https://api.telegram.org/bot${botToken}/sendMessage`;
//   const params = {
//     chat_id: chatId,
//     text,
//   };

//   try {
//     const response = await fetch(apiUrl, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(params),
//     });

//     const responseData = await response.json();
//     console.log(responseData);
//   } catch (error) {
//     console.error('Error sending message:', error.message);
//   }
// }

// app.listen(port, () => {
//   console.log(`Telegram bot listening at http://localhost:${port}`);
// });
