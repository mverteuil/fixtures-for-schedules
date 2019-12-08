import pytest
from django.utils import timezone

from schedules.models import Schedule


@pytest.mark.parametrize(("field_name", "expected"), (("start", timezone.now),))
def test_default_start_date(field_name, expected):
    """Should be now if not otherwise specified."""
    schedule_field = Schedule._meta.get_field(field_name)
    assert schedule_field.default == expected
