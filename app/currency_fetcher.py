import aiohttp
from app.utils import get_last_dates


class CurrencyFetcher:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="

    async def fetch_day(self, session, date: str):
        try:
            async with session.get(self.BASE_URL + date) as response:
                if response.status != 200:
                    print(f"Ошибка при получении данных за {date}")
                    return None
                data = await response.json()
                rates = {
                    "EUR": {},
                    "USD": {}
                }
                for rate in data.get("exchangeRate", []):
                    if rate.get("currency") in rates:
                        rates[rate["currency"]] = {
                            "sale": rate.get("saleRate"),
                            "purchase": rate.get("purchaseRate")
                        }
                return {date: rates}
        except Exception as e:
            print(f"Ошибка сети за {date}: {e}")
            return None

    async def get_rates(self, days: int):
        results = []
        dates = get_last_dates(days)
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_day(session, date) for date in dates]
            responses = await asyncio.gather(*tasks)
            results = [res for res in responses if res]
        return results
