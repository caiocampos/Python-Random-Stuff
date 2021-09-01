import re

TEL_REGEX = r"[+]?(\d)?\s*[(]?([2-9]\d{2})[).]?\s*([2-9]\d{2})[.-]?\s*(\d{4})\s*"


class Phone(object):
    def __init__(self, phone_number):
        m = re.search(TEL_REGEX, phone_number)
        if m is None:
            raise ValueError("Invalid Number format")
        (
            self.__country_code,
            self.__area_code,
            self.__exchange_code,
            self.__line_number
        ) = m.groups()
        if self.__area_code is None or self.__exchange_code is None or self.__line_number is None:
            raise ValueError("Invalid Number")
        if self.__country_code is not None and self.__country_code != "1":
            raise ValueError("Invalid Country code")
        if len(self.__area_code) < 3:
            raise ValueError("Invalid Area code")
        if len(self.__exchange_code) < 3:
            raise ValueError("Invalid Exchange code")
        if len(self.__line_number) < 4:
            raise ValueError("Invalid Line number")

    @property
    def country_code(self):
        return self.__country_code

    @property
    def area_code(self):
        return self.__area_code

    @property
    def exchange_code(self):
        return self.__exchange_code

    @property
    def line_number(self):
        return self.__line_number

    @property
    def number(self):
        return f"{self.__area_code}{self.__exchange_code}{self.__line_number}"

    def pretty(self):
        return f"({self.__area_code}) {self.__exchange_code}-{self.__line_number}"
