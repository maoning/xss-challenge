const express = require('express');
const puppeteer = require('puppeteer');

const app = express();
const URL = require("url").URL;

const validUrl = (s) => {
  try {
    new URL(s);
    return true;
  } catch (err) {
    return false;
  }
};

app.get('/', async (req, res) => {
    const {message} = req.query;
    if (!message || message.length === 0) {
        return res.json({error: 'message query parameter is required'});
    }
    if (!validUrl(message)) {
      return res.json({error: 'message is not a valid url, read message'});
    }

    console.log("message is: " + message);
    const status = await visit(message);
    return status == 0 ?
      res.json({success: 'message is a valid url, visited url.'}) :
      res.json({failed: 'message is a valid url, visited url but encountered error.'});
});

app.listen(process.env.PORT || 5555);

async function visit(url) {
   const browser = await puppeteer.launch({
       headless: true,
       executablePath: '/usr/bin/chromium-browser',
       args: [
       "--no-sandbox",
       "--disable-gpu",
       ]
   });

    const page = await browser.newPage();
    await page.setCookie({
      'name': process.env.COOKIE_NAME || "secret-cookie",
      'value': process.env.COOKIE_VALUE || "cookie-value",
      'url': process.env.COOKIE_URL || "http://vulnapp"
    })
    const response = await page.goto(url, {
      timeout: 5000,
      waitUntil: 'networkidle0',
    });

    await page.close();
    await browser.close();

  if (response._status < 400) {
    return 0;
  }
  return 1;
}
