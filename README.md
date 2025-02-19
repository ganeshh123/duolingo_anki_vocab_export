# Duo Lingo Anki Vocab Export

Fork of https://github.com/enestvedto/Anki-Duolingo with fixes applied, specifically to overcome the wrong password issue.

## Setup

### Install Anki Connect

1.  Open the `Install Add-on` dialog by selecting `Tools` | `Add-ons` | `Get Add-ons...` in Anki.
2.  Input [2055492159](https://ankiweb.net/shared/info/2055492159) into the text box labeled `Code` and press the `OK` button to proceed.
3.  Restart Anki when prompted to do so in order to complete the installation of Anki-Connect.

Anki must be kept running in the background in order for other applications to be able to use Anki-Connect. You can verify that Anki-Connect is running at any time by accessing `localhost:8765` in your browser. If the server is running, you will see the message `Anki-Connect` displayed in your browser window.


### Export Duo Lingo Cookies

1. On any browser, go to [Duolingo](https://www.duolingo.com/) and log in with your credentials.
2. Open the developer tools by pressing `F12` or `Ctrl + Shift + I` on your keyboard.
3. Go to the "Console" tab and enter the following (you might need to allow pasting):

```js
copy(JSON.stringify(document.cookie.split('; ').map(c => {
    const [name, value] = c.split('=');
    return { name, value, domain: '.duolingo.com' };
})))
```
4. Paste the copied cookies into the [cookies.json](./cookies.json) file.


### Set up the python environment and install packages:

```bash
python3 -m venv myvenv
chmod +x ./myvenv/bin/activate
./myvenv/bin/activate
./myvenv/bin/pip3 install -r requirements.txt
```


## Running

To run the script, run the following command:

```bash
./myvenv/bin/python3 main.py
```

The script will automatically navigate to the Duolingo practice hub and extract all the words from the vocabulary list. It will then create a new deck with the name specified in the `deckname` field of the [config.ini](./config.ini) file and add the words to the deck. The script will then close the browser and exit.

## Configuration

You can change the name of the deck or the path to the Chrome executable by editing the [config.ini](./config.ini) file.