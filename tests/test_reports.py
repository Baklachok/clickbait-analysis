from clickbaitanalysis.reports import available_reports, get_report


def test_get_report_returns_clickbait_report() -> None:
    report = get_report("clickbait")

    assert report is not None
    assert report.name == "clickbait"
    assert report.headers == ("title", "ctr", "retention_rate")


def test_available_reports_lists_registered_reports() -> None:
    assert available_reports() == ("clickbait",)


def test_get_report_returns_none_for_unknown_report() -> None:
    assert get_report("unknown") is None
