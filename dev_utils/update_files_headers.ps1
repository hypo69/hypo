param (
    [string]$Path = ".",         # Путь к корневой папке проекта
    [switch]$ForceUpdate,        # Флаг для принудительного обновления
    [switch]$Clean,              # Флаг для очистки заголовков
    [switch]$Help                # Флаг для вывода справки
)


$helpText = @"
Скрипт для обработки Python файлов в проекте.

Использование:
    -p <Path>           : Указывает путь к корневой директории проекта. По умолчанию текущая директория.
    --force-update      : Принудительно обновляет заголовки и интерпретатор в файлах.
    --clean             : Выполняет очистку перед обновлением.
    -h, --help, ?       : Показывает справку о возможных параметрах и использовании скрипта.

Пример:
    .\update_files_headers.ps1 -p "src" --force-update --clean
"@


# Вывод справки, если требуется
if ($Help) {
    Write-Host $helpText
    return
}

# Формируем аргументы для Python-скрипта
$Args = @()

# Добавляем аргументы
if ($Path -ne ".") {
    $Args += "-p", $Path
}
if ($ForceUpdate) {
    $Args += "--force-update"
}
if ($Clean) {
    $Args += "--clean"
}

# Получаем путь к Python и запускаем скрипт
$RootPath = Resolve-Path -Path (Join-Path -Path $Path -ChildPath "..")
$PythonScriptPath = Join-Path -Path $Path -ChildPath "update_files_headers.py"
$PythonExe = Join-Path -Path $RootPath -ChildPath "venv\Scripts\python.exe"

if (-not (Test-Path $PythonExe)) {
    Write-Host "Ошибка: Python интерпретатор не найден по пути: $PythonExe"
    return
}

Write-Host "Запуск Python-скрипта: $PythonExe $PythonScriptPath $Args"
& "$env:VIRTUAL_ENV\Scripts\python.exe" $PythonScriptPath @Args
