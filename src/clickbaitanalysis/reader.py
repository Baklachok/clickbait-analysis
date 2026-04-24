import csv
from collections.abc import Iterable
from pathlib import Path

from .models import VideoMetric


def read_video_metrics(path: Path) -> list[VideoMetric]:
    with path.open(encoding="utf-8", newline="") as csv_file:
        return [VideoMetric.from_csv_row(row) for row in csv.DictReader(csv_file)]


def read_video_metrics_from_files(paths: Iterable[Path]) -> list[VideoMetric]:
    records: list[VideoMetric] = []
    for path in paths:
        records.extend(read_video_metrics(path))
    return records
