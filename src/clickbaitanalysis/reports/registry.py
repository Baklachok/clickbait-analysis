from typing import cast

from .base import Report
from .clickbait import REPORT as CLICKBAIT_REPORT

_REPORTS: dict[str, Report] = {
    CLICKBAIT_REPORT.name: cast(Report, CLICKBAIT_REPORT),
}


def get_report(name: str) -> Report | None:
    return _REPORTS.get(name)


def available_reports() -> tuple[str, ...]:
    return tuple(_REPORTS)
