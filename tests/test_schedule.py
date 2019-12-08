from datetime import timedelta

import pytest
from django.utils import timezone

from schedules.models import Schedule


@pytest.mark.parametrize(
    ("field_name", "expected"),
    [("name", ""), ("start", timezone.now), ("finish", None), ("every", timedelta(hours=1)),],
)
def test_schedule_default_values(field_name, expected):
    """Should have expected default value."""
    schedule_field = Schedule._meta.get_field(field_name)
    assert schedule_field.default == expected
