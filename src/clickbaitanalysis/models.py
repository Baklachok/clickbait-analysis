from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VideoMetric:
    title: str
    ctr_text: str
    retention_rate_text: str
    ctr_value: float
    retention_rate_value: float

    @classmethod
    def from_csv_row(cls, row: Mapping[str, str]) -> "VideoMetric":
        ctr_text = row["ctr"]
        retention_rate_text = row["retention_rate"]
        return cls(
            title=row["title"],
            ctr_text=ctr_text,
            retention_rate_text=retention_rate_text,
            ctr_value=float(ctr_text),
            retention_rate_value=float(retention_rate_text),
        )
