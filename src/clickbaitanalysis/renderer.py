from collections.abc import Sequence

from tabulate import tabulate


def render_report_table(
    headers: Sequence[str],
    rows: Sequence[Sequence[str]],
) -> str:
    return tabulate(
        rows,
        headers=headers,
        tablefmt="simple",
        disable_numparse=True,
    )
