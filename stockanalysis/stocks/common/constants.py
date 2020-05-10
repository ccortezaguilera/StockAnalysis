from enum import Enum


class Conversions(Enum):
    WHAT_IF = "what_if"
    MAX_DAY_INCREASE = "max_day_increase"
    MAX_DAY_DECREASE = "max_day_decrease"
    MAX_DAY_PERCENT_INCREASE = "max_day_percent"
    MAX_DAY_PERCENT_DECREASE = "max_day_percent_decrease"
    MAX_MONTH_INCREASE = "max_month_increase"
    MAX_YEAR_INCREASE = "max_year_increase"
    TOP3 = "top3"
    DOWNLOAD = "download"
    REFRESH = "refresh"
