from clickbaitanalysis.models import VideoMetric
from clickbaitanalysis.reports.clickbait import REPORT


def make_record(
    title: str,
    ctr_text: str,
    retention_text: str,
) -> VideoMetric:
    return VideoMetric(
        title=title,
        ctr_text=ctr_text,
        retention_rate_text=retention_text,
        ctr_value=float(ctr_text),
        retention_rate_value=float(retention_text),
    )


def test_clickbait_report_filters_and_sorts_records() -> None:
    records = [
        make_record("not enough ctr", "15", "30"),
        make_record("retention too high", "20", "40"),
        make_record("middle", "21.5", "35"),
        make_record("highest", "25.0", "22"),
        make_record("lowest", "16.1", "39"),
    ]

    rows = REPORT.build_rows(records)

    assert rows == [
        ("highest", "25.0", "22"),
        ("middle", "21.5", "35"),
        ("lowest", "16.1", "39"),
    ]


def test_clickbait_report_keeps_original_order_for_equal_ctr_values() -> None:
    records = [
        make_record("first", "20.0", "30"),
        make_record("second", "20.0", "35"),
    ]

    rows = REPORT.build_rows(records)

    assert rows == [
        ("first", "20.0", "30"),
        ("second", "20.0", "35"),
    ]
