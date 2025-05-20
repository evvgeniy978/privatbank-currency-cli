from datetime import datetime, timedelta


def validate_days(value: str) -> int | None:
    try:
        days = int(value)
        if 1 <= days <= 10:
            return days
    except ValueError:
        pass
    return None


def get_last_dates(n: int) -> list[str]:
    today = datetime.now()
    return [
        (today - timedelta(days=i)).strftime("%d.%m.%Y")
        for i in range(n)
    ]


def format_output(data: list[dict]) -> str:
    import json
    return json.dumps(data, indent=2, ensure_ascii=False)
