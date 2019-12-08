from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    """Recurring schedule."""

    name = models.CharField(default="", max_length=128)
    start = models.DateTimeField(default=timezone.now)
    finish = models.DateTimeField(default=None, null=True)
    every = models.DurationField(default=timedelta(hours=1))

    def next_occurrence(self) -> datetime:
        """Date and time for the next occurrence."""
        occurrences = ScheduleIterator(self)
        now = timezone.now()
        while next_occurrence := next(occurrences):
            if next_occurrence > now:
                return next_occurrence

    def __iter__(self):
        return ScheduleIterator(self)


class ScheduleIterator:
    """Produce Schedule occurrences."""

    def __init__(self, schedule: Schedule):
        self._schedule = schedule
        self._next_occurrence = schedule.start

    def has_occurrences(self) -> bool:
        """Any occurrences remaining before the finish, or ."""
        if self._schedule.finish:
            return self._next_occurrence < self._schedule.finish
        return True

    def __next__(self) -> datetime:
        self._next_occurrence += self._schedule.every
        if self.has_occurrences():
            return self._next_occurrence
