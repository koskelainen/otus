import logging

logging.getLogger(__name__)


def get_int_counter(string):
    if isinstance(string, str):
        try:
            return int(string)
        except Exception as e:
            logging.warning(e)
            return string
    else:
        return 0


def get_float_counter(string):
    if isinstance(string, str):
        try:
            if string[:1].isdigit():
                return float(string.replace(",", "."))
            else:
                return float(string[1:].replace(",", ".")) * -1
        except Exception as e:
            logging.warning(e)
            return string
    else:
        return 0


def get_views_counter(string):
    if isinstance(string, str):
        try:
            return int((string.replace(",", "")).replace("k", "000"))
        except Exception as e:
            logging.warning(e)
            return string
    else:
        return 0