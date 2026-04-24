from dataclasses import dataclass
from typing import Sequence

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
                if record.ctr_value > 15 and record.retention_rate_value < 40
            ),
            key=lambda record: record.ctr_value,
            reverse=True,
        )
        return [
            (record.title, record.ctr_text, record.retention_rate_text)
            for record in filtered_records
        ]


REPORT = ClickbaitReport()
