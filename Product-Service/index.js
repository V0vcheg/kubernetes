const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

const logFilePath = '/var/log/user.log';

fs.open(logFilePath, 'a', (err, fd) => {
  if (err) throw err;
  fs.close(fd, (err) => {
    if (err) throw err;
  });
});

const logFile = fs.createWriteStream(logFilePath, { flags: 'a' });
const log = (message) => {
  logFile.write(`${new Date().toISOString()} - ${message}\n`);
};

app.get('/', (req, res) => {
  const apiKey = process.env.API_KEY;
  log(`Received request using API key: ${apiKey}`);
  res.send(`Hello from Product-Service using API key: ${apiKey}`);
});

app.listen(port, () => {
  log(`Product-Service listening at http://localhost:${port}`);
  console.log(`Product-Service listening at http://localhost:${port}`);
});
