import decimal
import os
import configparser

_config = configparser.ConfigParser()
_config.read("config.ini", encoding="utf-8")


def _get_from_config_or_env(section: str, key: str) -> str:
    result = _config[section].get(key)
    if not result:
        result = os.environ[f"{section}:{key}"]
    return result


TELEGRAM_TOKEN = _get_from_config_or_env("bot", "telegram_token")
ADMIN_TELEGRAM_ID = int(_get_from_config_or_env("bot", "admin_telegram_id"))

MINIMUM_DEPOSIT_AMOUNT = decimal.Decimal(_get_from_config_or_env("app", "minimum_deposit_amount"))
MINIMUM_WITHDRAW_AMOUNT = decimal.Decimal(_get_from_config_or_env("app", "minimum_withdraw_amount"))
