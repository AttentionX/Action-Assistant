import os
from dotenv import load_dotenv
from PIL import Image

from openai_api import state
from user_flow import essentials
from browsing import selenium_state
from util import util

# load_dotenv()

def init_assistants():
    model = 'gpt-3.5-turbo'
    system = 'You are a helpful assistant.'
    browsing_assistant = state.customChatGPT(model, system)
    driver = selenium_state.customDriver()
    return browsing_assistant, driver

def main():
    browsing_assistant, driver = init_assistants()
    initial_input = input('Hi how can I help you?\n')
    website_link = essentials.getWebsite(initial_input, browsing_assistant)
    driver.getLink(website_link)
    datetime_string = '_'.join(util.getDatetime(True))
    filename = driver.takeScreenshot(website_link.replace('https://', '').replace('.', '_').replace('/', '_'), datetime_string)
    print('Screenshot saved', filename)
    # screenshot = Image.open(filename)
    # screenshot.show()
    while True:
        user_input = input('')

if __name__ == "__main__":
    main()