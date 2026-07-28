def format_weather(data: dict) -> str:
    return (
        f" <b>{data['city']}, {data['country']}</b>\n\n"
        f" Температура: <b>{data['temp']}°C</b>\n"
        f" Ощущается: <b>{data['feels_like']}°C</b>\n"
        f" Влажность: <b>{data['humidity']}%</b>\n"
        f" Ветер: <b>{data['wind_speed']} м/с</b>\n"
        f" Давление: <b>{data['pressure']} мм рт.ст.</b>\n"
        f" {data['description'].capitalize()}\n\n"
        f" Обновлено: {data['updated_at']}"
    )

def format_rates(rates: dict) -> str:
    return (
        " <b>Курсы валют ЦБ РФ</b>\n\n"
        f"🇺🇸 USD: <b>{rates['USD']:.2f} ₽</b>\n"
        f"🇪🇺 EUR: <b>{rates['EUR']:.2f} ₽</b>\n"
        f"🇬🇧 GBP: <b>{rates['GBP']:.2f} ₽</b>\n"
        f"🇨🇳 CNY: <b>{rates['CNY']:.2f} ₽</b>\n"
        f"🇯🇵 JPY: <b>{rates['JPY']:.2f} ₽</b>\n"
        f" BTC: <b>{rates['BTC']:,.0f} ₽</b>\n\n"
        f" Обновлено: {rates['updated_at']}"
    )

def format_conversion(amount: float, from_curr: str, to_curr: str, result: float) -> str:
    return (
        f" <b>Конвертация валют</b>\n\n"
        f"{amount:.2f} {from_curr} = <b>{result:.2f} {to_curr}</b>"
    )
