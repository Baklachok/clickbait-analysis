import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .reader import read_video_metrics_from_files
from .renderer import render_report_table
from .report_registry import available_reports, get_report


class CliError(Exception):
    """Raised for user-facing CLI validation errors."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate YouTube video reports from CSV files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to one or more CSV files with video metrics.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(list(argv) if argv is not None else None)
        report = get_report(args.report)
        if report is None:
            available = ", ".join(available_reports())
            raise CliError(f"Unknown report '{args.report}'. Available reports: {available}")

        file_paths = _validate_input_files(args.files)
        records = read_video_metrics_from_files(file_paths)
        rows = report.build_rows(records)
        print(render_report_table(report.headers, rows))
        return 0
    except CliError as error:
        print(error, file=sys.stderr)
        return 1


def _validate_input_files(file_names: Sequence[str]) -> list[Path]:
    validated_paths: list[Path] = []
    for file_name in file_names:
        path = Path(file_name)
        if not path.is_file():
            raise CliError(f"Input file not found: {file_name}")
        validated_paths.append(path)
    return validated_paths
