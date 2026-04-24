from collections.abc import Sequence
from typing import Protocol, cast

from .models import VideoMetric
from .reports.clickbait import REPORT as CLICKBAIT_REPORT


class Report(Protocol):
    name: str
    headers: Sequence[str]

    def build_rows(self, records: Sequence[VideoMetric]) -> list[tuple[str, ...]]:
        """Build display rows for a report."""


_REPORTS: dict[str, Report] = {
    CLICKBAIT_REPORT.name: cast(Report, CLICKBAIT_REPORT),
}


def get_report(name: str) -> Report | None:
    return _REPORTS.get(name)


def available_reports() -> tuple[str, ...]:
    return tuple(_REPORTS)
