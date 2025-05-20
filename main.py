import asyncio
import sys

from app.currency_fetcher import CurrencyFetcher
from app.utils import validate_days, format_output


async def main():
    if len(sys.argv) != 2:
        print("Введи количество дней (от 1 до 10), например:")
        print("python main.py 3")
        return

    days = validate_days(sys.argv[1])
    if days is None:
        print("Неправильный ввод. Введи число от 1 до 10.")
        return

    fetcher = CurrencyFetcher()
    result = await fetcher.get_rates(days)
    print(format_output(result))


if __name__ == "__main__":
    asyncio.run(main())
