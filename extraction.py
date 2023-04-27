from bs4 import BeautifulSoup
import requests
import asyncio
from playwright.async_api import async_playwright

def bs():
    # Make a GET request to the webpage you want to extract text from
    response = requests.get("https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings")

    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all the text on the page
    text = soup.get_text()

    # Print the text
    print(text)

def pw():
    async def extract_text():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            # await page.goto('https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings')
            await page.goto('https://csrankings.org/')
            # Wait for the page to finish loading
            await page.wait_for_selector('body')
            # Extract the visible text on the page
            text = await page.evaluate("() => document.querySelector('body').innerText")
            print(text)
            await browser.close()

    asyncio.run(extract_text())


if __name__ == "__main__":
    # bs()
    pw()