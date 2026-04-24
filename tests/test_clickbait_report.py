from clickbaitanalysis.models import VideoMetric
from clickbaitanalysis.reports.clickbait import REPORT


def make_record(
    title: str,
    ctr: float,
    retention_rate: float,
) -> VideoMetric:
    return VideoMetric(
        title=title,
        ctr=ctr,
        retention_rate=retention_rate,
    )


def test_clickbait_report_filters_and_sorts_records() -> None:
    records = [
        make_record("not enough ctr", 15.0, 30.0),
        make_record("retention too high", 20.0, 40.0),
        make_record("middle", 21.5, 35.0),
        make_record("highest", 25.0, 22.0),
        make_record("lowest", 16.1, 39.0),
    ]

    rows = REPORT.build_rows(records)

    assert rows == [
        ("highest", "25.0", "22"),
        ("middle", "21.5", "35"),
        ("lowest", "16.1", "39"),
    ]


def test_clickbait_report_keeps_original_order_for_equal_ctr_values() -> None:
    records = [
        make_record("first", 20.0, 30.0),
        make_record("second", 20.0, 35.0),
    ]

    rows = REPORT.build_rows(records)

    assert rows == [
        ("first", "20.0", "30"),
        ("second", "20.0", "35"),
    ]
