from django.utils import timezone

from schedules.models import Schedule


def test_default_start_date():
    """Should be now if not otherwise specified."""
    start_field = Schedule._meta.get_field("start")
    assert start_field.default is timezone.now
