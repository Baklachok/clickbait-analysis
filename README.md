# ClickbaitAnalysis

CLI-приложение читает один или несколько CSV-файлов с метриками YouTube и строит отчёт `clickbait`. В отчёт попадают только видео с `ctr > 15` и `retention_rate < 40`, отсортированные по убыванию `ctr`.

Пример запуска:

```bash
poetry run clickbaitanalysis --files stats1.csv stats2.csv --report clickbait
```
