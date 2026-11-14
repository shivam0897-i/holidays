#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.calendars.gregorian import JAN, FEB, OCT, NOV, FRI, SAT, SUN, _timedelta
from holidays.groups import HebrewCalendarHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    FRI_TO_PREV_THU,
    FRI_TO_PREV_WED,
    MON_TO_NEXT_TUE,
    SAT_TO_NEXT_SUN,
    SAT_TO_PREV_THU,
    SAT_SUN_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    THU_TO_PREV_WED,
    ObservedHolidayBase,
)


class TelAvivStockExchange(ObservedHolidayBase, HebrewCalendarHolidays, StaticHolidays):
    """Tel Aviv Stock Exchange (TASE) holidays.

    References:
        * [TASE Trading and Vacation Schedules](https://web.archive.org/web/20261114073950/https://www.tase.co.il/en/content/knowledge_center/trading_vacation_schedule/)
        * [Vacation Schedule 2022](https://web.archive.org/web/20251117170332/https://content.tase.co.il/media/vyolzrvu/file_0010_vacation_schedule_2022_eng.pdf)
        * [Vacation Schedule 2023](https://web.archive.org/web/20261114073732/https://content.tase.co.il/media/iqcijli2/file_0010_vacation_schedule_2023_eng.pdf)
        * [Trading on Shushan Purim 2023](https://web.archive.org/web/20260118174913/https://www.tase.co.il/en/content/news-lobby/20230308_pr/)
        * [Vacation Schedule 2024](https://web.archive.org/web/20251117170328/https://content.tase.co.il/media/33xjyi00/file_0010_vacation_schedule_2024_eng.pdf)
    """

    market = "XTAE"
    default_language = "he"
    # %s (observed).
    observed_label = tr("%s (נצפה)")
    supported_languages = ("en_US", "he")
    start_year = 2022

    def __init__(self, *args, **kwargs):
        HebrewCalendarHolidays.__init__(self)
        StaticHolidays.__init__(self, TelAvivStockExchangeStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt, name, rule):
        is_observed, _ = super()._add_observed(dt, name, rule=rule)
        if not is_observed:
            self._add_holiday(name, dt)

    def _get_weekend(self, dt: date) -> set[int]:
        # January 4, 2026 was the first non-trading Sunday.
        return {SAT, SUN} if dt >= date(2026, JAN, 4) else {FRI, SAT}

    def _populate_common_holidays(self):
        super()._populate_common_holidays()
        # Fridays during Chol HaMoed remain shortened trading days.
        chol_hamoed = {
            _timedelta(dt, delta)  # type: ignore[arg-type]
            for dt, days in (
                (self._hebrew_calendar.passover_date(self._year), 5),
                (self._hebrew_calendar.sukkot_date(self._year), 6),
            )
            for delta in range(1, days + 1)
        }
        for dt in tuple(self):
            if dt.year != self._year:
                continue
            if (
                self._year >= 2026
                and self._is_sunday(dt)
                and (friday := self._get_observed_date(dt, SAT_SUN_TO_PREV_FRI)) not in self
                and friday not in chol_hamoed
            ):
                super()._add_observed(
                    dt,
                    # Market Holiday.
                    tr("יום חופשה בבורסה"),
                    rule=SAT_SUN_TO_PREV_FRI,
                    force_observed=True,
                    show_observed_label=False,
                )
            if self._is_weekend(dt):
                self.pop(dt)

    def _populate_public_holidays(self):
        # Purim.
        self._add_purim(tr("פורים"))

        # Pesach Eve.
        self._add_passover(tr("ערב פסח"), -1)
        # Pesach.
        self._add_passover(tr("פסח"))
        # Seventh day of Pesach Eve.
        self._add_passover(tr("ערב שביעי של פסח"), +5)
        # Seventh day of Pesach.
        self._add_passover(tr("שביעי של פסח"), +6)

        self._add_observed(
            _timedelta(self._hebrew_calendar.israel_independence_date(self._year), -1),
            # Remembrance Day.
            tr("יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            THU_TO_PREV_WED + FRI_TO_PREV_WED + SUN_TO_NEXT_MON,
        )

        self._add_observed(
            self._hebrew_calendar.israel_independence_date(self._year),
            # Independence Day.
            tr("יום העצמאות"),
            FRI_TO_PREV_THU + SAT_TO_PREV_THU + MON_TO_NEXT_TUE,
        )

        # Shavuot Eve.
        self._add_shavuot(tr("ערב שבועות"), -1)
        # Shavuot.
        self._add_shavuot(tr("שבועות"))

        self._add_observed(
            self._hebrew_calendar.tisha_bav_date(self._year),
            # Tisha B'Av.
            tr("תשעה באב"),
            SAT_TO_NEXT_SUN,
        )

        # Rosh Hashanah Eve.
        self._add_rosh_hashanah(tr("ערב ראש השנה"), -1)
        # Rosh Hashanah.
        self._add_rosh_hashanah(tr("ראש השנה"), range(2))

        # Yom Kippur Eve.
        self._add_yom_kippur(tr("ערב יום כיפור"), -1)
        # Yom Kippur.
        self._add_yom_kippur(tr("יום כיפור"))

        # Sukkot Eve.
        self._add_sukkot(tr("ערב סוכות"), -1)
        # Sukkot.
        self._add_sukkot(tr("סוכות"))
        # Simchat Torah Eve.
        self._add_sukkot(tr("ערב שמחת תורה"), +6)
        # Simchat Torah / Shemini Atzeret.
        self._add_sukkot(tr("שמחת תורה/שמיני עצרת"), +7)


class XTAE(TelAvivStockExchange):
    pass


class TelAvivStockExchangeStaticHolidays:
    """Tel Aviv Stock Exchange special holidays.

    References:
        * [Municipal elections 2024](https://web.archive.org/web/20250720201133/https://en.globes.co.il/en/article-Mon-TASE-edges-higher-despite-no-rate-cut-1001472244)
    """

    # Knesset Election Day.
    knesset_election_day = tr("יום הבחירות לכנסת")

    special_public_holidays = {
        2022: (NOV, 1, knesset_election_day),
        # Municipal Election Day.
        2024: (FEB, 27, tr("יום הבחירות לרשויות המקומיות")),
        2026: (OCT, 27, knesset_election_day),
    }
