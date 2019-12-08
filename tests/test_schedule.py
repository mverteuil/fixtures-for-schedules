from unittest import mock

from schedules.models import Schedule


def test_default_start_date():
    """Should be now if not otherwise specified."""
    with mock.patch("schedules.models.timezone") as mock_timezone:
        schedule = Schedule()
        assert schedule.start == mock_timezone.now()
