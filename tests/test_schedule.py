import pytest
from django.utils import timezone
from schedules.models import Schedule


def test_schedule_defaults():
    """Should have expected default values."""
    schedule = Schedule()
    assert schedule.start == pytest.approx(timezone.now())
