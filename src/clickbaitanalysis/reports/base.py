from collections.abc import Sequence
from typing import Protocol

from ..models import VideoMetric


class Report(Protocol):
    name: str
    headers: Sequence[str]

    def build_rows(self, records: Sequence[VideoMetric]) -> list[tuple[str, ...]]:
        """Build display rows for a report."""
