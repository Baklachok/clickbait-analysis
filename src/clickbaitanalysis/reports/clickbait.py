from collections.abc import Sequence
from dataclasses import dataclass

from ..models import VideoMetric


@dataclass(frozen=True, slots=True)
class ClickbaitReport:
    name: str = "clickbait"
    headers: tuple[str, str, str] = ("title", "ctr", "retention_rate")

    def build_rows(self, records: Sequence[VideoMetric]) -> list[tuple[str, str, str]]:
        filtered_records = sorted(
            (
                record
                for record in records
                if record.ctr > 15 and record.retention_rate < 40
            ),
            key=lambda record: record.ctr,
            reverse=True,
        )
        return [
            (record.title, f"{record.ctr:.1f}", f"{record.retention_rate:g}")
            for record in filtered_records
        ]


REPORT = ClickbaitReport()
