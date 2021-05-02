# xss-challenge
An xss web challenge based on flask, nodejs, headless chrome &amp; puppeteer

## Local Setup
```
git clone https://github.com/maoning/xss-challenge.git
cd xss-challenge
docker-compose build
docker-compose up
```

Visit `http://localhost:5000` to access the vulnerable app.

## Design
### vulnapp
vulnapp container hosts a simple flask app that contains a reflected xss vulnerability. When a message is submitted via the app, it calls xssbot service to read the message.

### xssbot
xssbot is a nodejs server. Once it receives an api call from vulnapp to read a message, and if the message is a url, it will use headless chrome to visit that url with an admin cookie.

## Caveat
xssbot can reach vulnapp service via http://vulnapp:5000.
