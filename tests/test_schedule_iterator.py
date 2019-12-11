from datetime import datetime, timedelta
from unittest import mock

import pytest

from schedules.models import ScheduleIterator


@pytest.fixture(name="mock_schedule")
def create_mock_schedule():
    """Create a mock schedule with a start date and interval configured."""
    return mock.Mock(name="Schedule", start=datetime(2000, 1, 2, 3, 4, 5, 6), every=timedelta(hours=1))


def test_initialize(mock_schedule):
    """Should require a schedule."""
    ScheduleIterator(mock_schedule)
