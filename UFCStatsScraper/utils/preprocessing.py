"""Various utility functions for the spider"""


def set_logger(lv=None, path=None):
    import logging

    logger = logging.getLogger("ufcstatsscraper")
    logger.setLevel(logging.DEBUG)
    if lv is None:
        lv = logging.WARNING
    if path is None:
        path = "ufcstatsscraper/logging/gen.log"
    fh = logging.FileHandler(path, mode="w")
    fh.setLevel(lv)
    logger.addHandler(fh)
    return logger


def is_datetime(text):
    """Check if a string is a datetime object"""
    from datetime import datetime as dt

    return isinstance(text, dt)


def remove_whitespace(text):
    """Remove whitespace from a string"""
    import logging

    try:
        text = text.strip()
    except Exception as e:
        logging.debug(e)

    else:
        return text.strip()
    return [item.strip() for item in text]


def remove_non_numeric(text):
    """Remove non-numeric characters from a string"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return "".join([char for char in text if char.isnumeric()])
    return ["".join([char for char in item if char.isnumeric()]) for item in text]


def remove_non_alphanumeric(text):
    """Remove non-alphanumeric characters from a string"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return "".join([char for char in text if char.isalnum()])
    return ["".join([char for char in item if char.isalnum()]) for item in text]


def remove_newlines(text):
    """Remove newlines from a string"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return text.replace("\n", "")
    return [item.replace("\n", "") for item in text]


def format_date(text):
    """Format a date string"""
    from datetime import datetime as dt
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        if is_datetime(text):
            return text
        elif text == "---":
            return "---"
        else:
            try:
                return dt.strptime(text, "%b %d, %Y")
            except Exception as e:
                logging.debug(e)
    try:
        if is_datetime(text):
            return text
        elif text == "---":
            return ["---" for _ in text]
        else:
            return [dt.strptime(item, "%b %d, %Y") for item in text]
    except Exception as e:
        logging.debug(e)


def replace_empty_string(text):
    """Replace empty strings with ---"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return "---" if text == "" else text
    return ["---" if item == "" else item for item in text]


def convert_percentage(text):
    """Convert a percentage string to a float"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return str(float(text.strip("%")) / 100)
    return [str(float(item.strip("%"))) / 100 for item in text]


def convert_to_int(text):
    """Convert a string to an integer"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return 0 if text == "---" else int(text)
    return [0 if item == "---" else int(item) for item in text]


def convert_to_float(text):
    """Convert a string to a float"""
    import logging

    try:
        text.isalnum()
    except Exception as e:
        logging.debug(e)
    else:
        return 0 if text == "---" else float(text)
    return [0 if item == "---" else float(item) for item in text]


def extract_record(text):
    import re

    record = tuple([int(w) for w in re.findall(r"\d+", text)])
    return record


if __name__ == "__main__":
    stringg = ["6' 0\""]

    print(remove_non_numeric(stringg))

    record = extract_record("6-0-0")
    print(record)

    is_alphanumeric = ("---").isalnum()
