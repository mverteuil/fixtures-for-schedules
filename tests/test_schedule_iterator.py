import pytest

from schedules.models import ScheduleIterator


def test_initialize():
    """Should require a schedule."""
    with pytest.raises(TypeError):
        ScheduleIterator()
