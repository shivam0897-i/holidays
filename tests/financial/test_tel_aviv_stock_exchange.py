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

from unittest import TestCase

from holidays.financial.tel_aviv_stock_exchange import TelAvivStockExchange
from tests.common import CommonFinancialTests


class TestTelAvivStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TelAvivStockExchange)

    def test_purim(self):
        name = "פורים"
        self.assertHolidayName(
            name,
            "2022-03-17",
            "2023-03-07",
            "2024-03-24",
            "2025-03-14",
            "2026-03-03",
            "2027-03-23",
            "2028-03-12",
            "2029-03-01",
        )

    def test_shushan_purim(self):
        name = "שושן פורים"
        self.assertHolidayName(
            name,
            "2022-03-18",
            "2023-03-08",
            "2024-03-25",
            "2025-03-15",
            "2026-03-04",
            "2027-03-24",
            "2028-03-13",
            "2029-03-02",
        )

    def test_pesach_eve(self):
        name = "ערב פסח"
        self.assertHolidayName(
            name,
            "2022-04-15",
            "2023-04-05",
            "2024-04-22",
            "2025-04-12",
            "2026-04-01",
            "2027-04-21",
            "2028-04-10",
            "2029-03-30",
        )

    def test_pesach(self):
        name = "פסח"
        self.assertHolidayName(
            name,
            "2022-04-16",
            "2023-04-06",
            "2024-04-23",
            "2025-04-13",
            "2026-04-02",
            "2027-04-22",
            "2028-04-11",
            "2029-03-31",
        )

    def test_seventh_day_of_pesach_eve(self):
        name = "ערב שביעי של פסח"
        self.assertHolidayName(
            name,
            "2022-04-21",
            "2023-04-11",
            "2024-04-28",
            "2025-04-18",
            "2026-04-07",
            "2027-04-27",
            "2028-04-16",
            "2029-04-05",
        )

    def test_seventh_day_of_pesach(self):
        name = "שביעי של פסח"
        self.assertHolidayName(
            name,
            "2022-04-22",
            "2023-04-12",
            "2024-04-29",
            "2025-04-19",
            "2026-04-08",
            "2027-04-28",
            "2028-04-17",
            "2029-04-06",
        )

    def test_remembrance_day(self):
        name = "יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"
        self.assertHolidayName(
            name,
            "2023-04-25",
            "2026-04-21",
            "2027-05-11",
        )
        obs_dts = (
            "2022-05-04",
            "2024-05-13",
            "2025-04-30",
            "2028-05-01",
            "2029-04-18",
        )
        self.assertHolidayName(f"{name} (נצפה)", obs_dts)

    def test_independence_day(self):
        name = "יום העצמאות"
        self.assertHolidayName(
            name,
            "2023-04-26",
            "2026-04-22",
            "2027-05-12",
        )
        obs_dts = (
            "2022-05-05",
            "2024-05-14",
            "2025-05-01",
            "2028-05-02",
            "2029-04-19",
        )
        self.assertHolidayName(f"{name} (נצפה)", obs_dts)

    def test_shavuot_eve(self):
        name = "ערב שבועות"
        self.assertHolidayName(
            name,
            "2022-06-04",
            "2023-05-25",
            "2024-06-11",
            "2025-06-01",
            "2026-05-21",
            "2027-06-10",
            "2028-05-30",
            "2029-05-19",
        )

    def test_shavuot(self):
        name = "שבועות"
        self.assertHolidayName(
            name,
            "2022-06-05",
            "2023-05-26",
            "2024-06-12",
            "2025-06-02",
            "2026-05-22",
            "2027-06-11",
            "2028-05-31",
            "2029-05-20",
        )

    def test_tisha_bav(self):
        name = "תשעה באב"
        self.assertHolidayName(
            name,
            "2023-07-27",
            "2024-08-13",
            "2025-08-03",
            "2026-07-23",
            "2027-08-12",
            "2028-08-01",
        )
        obs_dts = (
            "2022-08-07",
            "2029-07-22",
        )
        self.assertHolidayName(f"{name} (נצפה)", obs_dts)

    def test_rosh_hashanah_eve(self):
        name = "ערב ראש השנה"
        self.assertHolidayName(
            name,
            "2022-09-25",
            "2023-09-15",
            "2024-10-02",
            "2025-09-22",
            "2026-09-11",
            "2027-10-01",
            "2028-09-20",
            "2029-09-09",
        )

    def test_rosh_hashanah(self):
        name = "ראש השנה"
        self.assertHolidayName(
            name,
            "2022-09-26",
            "2022-09-27",
            "2023-09-16",
            "2023-09-17",
            "2024-10-03",
            "2024-10-04",
            "2025-09-23",
            "2025-09-24",
            "2026-09-12",
            "2026-09-13",
            "2027-10-02",
            "2027-10-03",
            "2028-09-21",
            "2028-09-22",
            "2029-09-10",
            "2029-09-11",
        )

    def test_yom_kippur_eve(self):
        name = "ערב יום כיפור"
        self.assertHolidayName(
            name,
            "2022-10-04",
            "2023-09-24",
            "2024-10-11",
            "2025-10-01",
            "2026-09-20",
            "2027-10-10",
            "2028-09-29",
            "2029-09-18",
        )

    def test_yom_kippur(self):
        name = "יום כיפור"
        self.assertHolidayName(
            name,
            "2022-10-05",
            "2023-09-25",
            "2024-10-12",
            "2025-10-02",
            "2026-09-21",
            "2027-10-11",
            "2028-09-30",
            "2029-09-19",
        )

    def test_sukkot_eve(self):
        name = "ערב סוכות"
        self.assertHolidayName(
            name,
            "2022-10-09",
            "2023-09-29",
            "2024-10-16",
            "2025-10-06",
            "2026-09-25",
            "2027-10-15",
            "2028-10-04",
            "2029-09-23",
        )

    def test_sukkot(self):
        name = "סוכות"
        self.assertHolidayName(
            name,
            "2022-10-10",
            "2023-09-30",
            "2024-10-17",
            "2025-10-07",
            "2026-09-26",
            "2027-10-16",
            "2028-10-05",
            "2029-09-24",
        )

    def test_simchat_torah_eve(self):
        name = "ערב שמחת תורה"
        self.assertHolidayName(
            name,
            "2022-10-16",
            "2023-10-06",
            "2024-10-23",
            "2025-10-13",
            "2026-10-02",
            "2027-10-22",
            "2028-10-11",
            "2029-09-30",
        )

    def test_simchat_torah(self):
        name = "שמחת תורה/שמיני עצרת"
        self.assertHolidayName(
            name,
            "2022-10-17",
            "2023-10-07",
            "2024-10-24",
            "2025-10-14",
            "2026-10-03",
            "2027-10-23",
            "2028-10-12",
            "2029-10-01",
        )

    def test_weekend(self):
        # Trading week changed from Sunday-Thursday to Monday-Friday
        # on January 5, 2026.
        for dt in (
            "2025-12-26",  # FRI.
            "2025-12-27",  # SAT.
            "2026-01-02",  # FRI.
            "2026-01-03",  # SAT.
            "2026-01-10",  # SAT.
            "2026-01-11",  # SUN.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2025-12-28",  # SUN.
            "2026-01-04",  # SUN.
            "2026-01-05",  # MON.
            "2026-01-09",  # FRI.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-03-03", "פורים"),
            ("2026-03-04", "שושן פורים"),
            ("2026-04-01", "ערב פסח"),
            ("2026-04-02", "פסח"),
            ("2026-04-07", "ערב שביעי של פסח"),
            ("2026-04-08", "שביעי של פסח"),
            ("2026-04-21", "יום הזיכרון לחללי מערכות ישראל ונפגעי פעולות האיבה"),
            ("2026-04-22", "יום העצמאות"),
            ("2026-05-21", "ערב שבועות"),
            ("2026-05-22", "שבועות"),
            ("2026-07-23", "תשעה באב"),
            ("2026-09-11", "ערב ראש השנה"),
            ("2026-09-12", "ראש השנה"),
            ("2026-09-13", "ראש השנה"),
            ("2026-09-20", "ערב יום כיפור"),
            ("2026-09-21", "יום כיפור"),
            ("2026-09-25", "ערב סוכות"),
            ("2026-09-26", "סוכות"),
            ("2026-10-02", "ערב שמחת תורה"),
            ("2026-10-03", "שמחת תורה/שמיני עצרת"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-03-03", "Purim"),
            ("2026-03-04", "Shushan Purim"),
            ("2026-04-01", "Pesach Eve"),
            ("2026-04-02", "Pesach"),
            ("2026-04-07", "Seventh day of Pesach Eve"),
            ("2026-04-08", "Seventh day of Pesach"),
            ("2026-04-21", "Remembrance Day"),
            ("2026-04-22", "Independence Day"),
            ("2026-05-21", "Shavuot Eve"),
            ("2026-05-22", "Shavuot"),
            ("2026-07-23", "Tisha B'Av"),
            ("2026-09-11", "Rosh Hashanah Eve"),
            ("2026-09-12", "Rosh Hashanah"),
            ("2026-09-13", "Rosh Hashanah"),
            ("2026-09-20", "Yom Kippur Eve"),
            ("2026-09-21", "Yom Kippur"),
            ("2026-09-25", "Sukkot Eve"),
            ("2026-09-26", "Sukkot"),
            ("2026-10-02", "Simchat Torah Eve"),
            ("2026-10-03", "Simchat Torah / Shemini Atzeret"),
        )
