sphinx-apidoc -o docs src --force --separate
# Переходим в директорию docs/sphinx
Set-Location -Path "docs"

# Перезаписываем index.rst, добавляя базовые директивы
@"
.. toctree::
   :maxdepth: 2
   :caption: Содержание:
"@ | Out-File -FilePath "index.rst" -Encoding UTF8

# Добавляем ссылки на каждый .rst файл, кроме index.rst
Get-ChildItem -Filter *.rst | Where-Object { $_.Name -ne "index.rst" } | ForEach-Object {
    "   $($_.BaseName)" | Out-File -FilePath "index.rst" -Encoding UTF8 -Append
}

