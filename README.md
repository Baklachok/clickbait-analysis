# ClickbaitAnalysis

CLI-приложение читает один или несколько CSV-файлов с метриками YouTube и строит отчёт `clickbait`. В отчёт попадают только видео с `ctr > 15` и `retention_rate < 40`, отсортированные по убыванию `ctr`.
Новые отчёты можно добавлять через пакет `clickbaitanalysis.reports` и реестр отчётов.

Пример запуска:

```bash
poetry run clickbaitanalysis --files stats1.csv stats2.csv --report clickbait
```

Скриншоты:
- успешный запуск: [docs/clickbait-cli-screenshot.png](docs/clickbait-cli-screenshot.png)
- обработка ошибки при несуществующем файле: [docs/clickbait-cli-error-screenshot.png](docs/clickbait-cli-error-screenshot.png)
