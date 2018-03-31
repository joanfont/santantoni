from datetime import date

import freezegun

from santantoni.utils import get_next_date


@freezegun.freeze_time('2018-03-31')
def test_get_next_sant_antoni_previous_year():
    next_sant_antoni = get_next_date(1, 17)
    assert next_sant_antoni == date(2019, 1, 17)

@freezegun.freeze_time('2019-01-01')
def test_get_next_sant_antoni_current_year():
    next_sant_antoni = get_next_date(1, 17)
    assert next_sant_antoni == date(2019, 1, 17)

@freezegun.freeze_time('2019-01-17')
def test_get_next_sant_antoni_current_day():
    next_sant_antoni = get_next_date(1, 17)
    assert next_sant_antoni == date(2019, 1, 17)

@freezegun.freeze_time('2019-01-18')
def test_get_next_sant_antoni_next_day():
    next_sant_antoni = get_next_date(1, 17)
    assert next_sant_antoni == date(2020, 1, 17)