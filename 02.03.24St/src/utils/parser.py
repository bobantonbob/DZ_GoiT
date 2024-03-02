import aiohttp
from bs4 import BeautifulSoup
NBU_URL = 'https://bank.gov.ua/ua/markets/exchangerates'


async def run_parser(currencies: list=None):
    print(f"Parser started")
    info = ''
    if currencies is None:
        currencies = ["EUR", "USD"]
    async with aiohttp.ClientSession() as session:
        async with session.get(url=NBU_URL) as response:
            print("Status:", response.status)
            html = await response.read()
    soup = BeautifulSoup(html, 'html.parser')
    main_block = soup.find("div", class_='col-md-8')
    table = main_block.find('table', id="exchangeRates")
    rows = table.find_all("tr")
    for row in rows:
        row_elements = row.find_all('td')
        for el in row_elements:
            joined_string = ':'.join([x.text.strip() for x in row_elements])
            match = False
            if el.text.strip() in currencies:
                match = True
            if match:
                rate = joined_string.split(':')[-1]
                info += f"{el.text.strip()} {rate}\n"
    return info




