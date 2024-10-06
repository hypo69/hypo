
# Путь к HTML-документу
$htmlFilePath = "docs\doxygen\_build\ru\html\index.html"

# Проверка существования файла
if (Test-Path $htmlFilePath -PathType Leaf) {
    # Открываю HTML-документ в браузере по умолчанию
    Start-Process $htmlFilePath
} else {
    Write-Host "docs\\doxygen\\_build\\ru\\html\\index.html не найден"
}
