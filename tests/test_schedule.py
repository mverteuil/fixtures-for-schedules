from datetime import timedelta

import pytest
from django.utils import timezone

from schedules.models import Schedule, ScheduleIterator


@pytest.mark.parametrize(
    ("field_name", "expected"),
    [("name", ""), ("start", timezone.now), ("finish", None), ("every", timedelta(hours=1)),],
)
def test_schedule_default_values(field_name, expected):
    """Should have expected default value."""
    schedule_field = Schedule._meta.get_field(field_name)
    assert schedule_field.default == expected


def test_iterator():
    """Should use schedule iterator."""
    schedule = Schedule()
    assert isinstance(iter(schedule), ScheduleIterator)


def test_next_occurrence():
    """Should have accurately date and time for the next event in the schedule."""
    schedule_start = timezone.now()
    schedule_every = timedelta(hours=1)
    schedule = Schedule(start=schedule_start, every=schedule_every)
    expected = schedule_start + schedule_every
    assert schedule.next_occurrence() == expected
