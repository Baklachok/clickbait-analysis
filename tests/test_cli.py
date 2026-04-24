from pathlib import Path

import pytest

from clickbaitanalysis.cli import main


EXPECTED_TITLES = [
    "Секрет который скрывают тимлиды",
    "Почему продакшн упал в пятницу вечером",
    "Как я неделю не мыл кружку и выгорел",
    "Как я спал по 4 часа и ничего не понял",
    "Что будет если удалить папку lib",
    "Как я задолжал ревьюеру 1000 строк кода",
    "Я закоммитил пароль на гитхаб",
    "Как я фиксил баг три дня и нашёл лишнюю запятую",
    "Купил джуну макбук и он уволился",
    "Я бросил IT и стал фермером",
    "Проснулся в 5 утра и закрыл спринт",
]


def test_main_prints_clickbait_report_for_example_files(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--files", "stats1.csv", "stats2.csv", "--report", "clickbait"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.err == ""
    assert "title" in captured.out
    assert "ctr" in captured.out
    assert "retention_rate" in captured.out
    assert "25.0" in captured.out
    assert "17.0" in captured.out
    assert "Почему сеньоры не носят галстуки" not in captured.out

    positions = [captured.out.index(title) for title in EXPECTED_TITLES]
    assert positions == sorted(positions)


def test_main_returns_error_for_unknown_report(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--files", "stats1.csv", "--report", "unknown"])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "Unknown report 'unknown'. Available reports: clickbait\n"


def test_main_returns_error_for_missing_input_file(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--files", "missing.csv", "--report", "clickbait"])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "Input file not found: missing.csv\n"


@pytest.mark.parametrize(
    "argv",
    [
        [],
        ["--files", "stats1.csv"],
        ["--report", "clickbait"],
    ],
)
def test_main_uses_argparse_exit_code_for_invalid_arguments(argv: list[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main(argv)

    assert error.value.code == 2


def test_main_prints_empty_table_when_no_rows_match(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    csv_path = tmp_path / "no_clickbait.csv"
    csv_path.write_text(
        "\n".join(
            [
                "title,ctr,retention_rate,views,likes,avg_watch_time",
                "Нормальное видео,10,80,100,10,4.0",
            ]
        ),
        encoding="utf-8",
    )

    exit_code = main(["--files", str(csv_path), "--report", "clickbait"])

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert exit_code == 0
    assert captured.err == ""
    assert "Нормальное видео" not in captured.out
    assert output_lines[0].split() == ["title", "ctr", "retention_rate"]
