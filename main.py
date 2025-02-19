from anki.anki import create_deck, create_note
from duolingo.duolingo import DuolingoBot
from selenium.webdriver.common.by import By
import configparser

def main():
    duolingo_bot = DuolingoBot()
    config = configparser.ConfigParser()
    config.read('config.cfg')
    deck_name = config['Anki']['deckname']
    
    try:
        duolingo_bot.navigate_to_words()
        duolingo_bot.load_full_vocab()

        # Extract words
        words = duolingo_bot.extract_words()
        words.reverse()
        
        create_deck(deck_name)

   
        for word in words:
            try:
                language_content = word.find_element(By.TAG_NAME, 'h3')
                english_translation = word.find_element(By.TAG_NAME, 'p')
                create_note(deck_name, english_translation.text, language_content.text)
            except Exception as e:
                print("Error accessing word content:", e)

    finally:
        duolingo_bot.close()

if __name__ == '__main__':
    main()
