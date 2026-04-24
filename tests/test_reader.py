from pathlib import Path

from clickbaitanalysis.reader import read_video_metrics, read_video_metrics_from_files


def test_read_video_metrics_parses_text_and_numeric_fields() -> None:
    records = read_video_metrics(Path("stats1.csv"))

    first_record = records[0]

    assert first_record.title == "Я бросил IT и стал фермером"
    assert first_record.ctr_text == "18.2"
    assert first_record.retention_rate_text == "35"
    assert first_record.ctr_value == 18.2
    assert first_record.retention_rate_value == 35.0


def test_read_video_metrics_from_files_preserves_file_order() -> None:
    records = read_video_metrics_from_files([Path("stats1.csv"), Path("stats2.csv")])

    assert records[0].title == "Я бросил IT и стал фермером"
    assert records[10].title == "Проснулся в 5 утра и закрыл спринт"
