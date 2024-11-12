param (
    [string]$Path = ".",
    [switch]$ExcludeVenv = $true,
    [string]$Interpreter = "/venv/Scripts/python.exe",
    [switch]$ForceUpdate = $false,
    [switch]$Help = $false
)

# Информация о запуске скрипта
$helpText = @"
Скрипт для обработки Python файлов в проекте.

Использование:
    -p <Path>           : Указывает путь к корневой директории проекта. По умолчанию текущая директория.
    --exclude-venv      : Исключает директорию 'venv' из обработки.
    --interpreter <Path>: Указывает путь к интерпретатору Python. По умолчанию '/venv/Scripts/python.exe'.
    --force-update      : Принудительно обновляет заголовки и интерпретатор в файлах.
    -h, --help, ?       : Показывает справку о возможных параметрах и использовании скрипта.

Пример:
    .\update_files_headers.ps1 -p "C:\path\to\project" --exclude-venv --interpreter "/venv/Scripts/python.exe" --force-update
"@

# Если включена опция помощи, выводим информацию и завершаем выполнение
if ($Help) {
    Write-Host $helpText
    return
}

# Формируем аргументы для Python-скрипта
$Args = @()

# Добавляем аргумент для пути, если он не равен значению по умолчанию
if ($Path -ne ".") {
    $Args += "-p", $Path
}

# Добавляем флаг ExcludeVenv, если он включен
if ($ExcludeVenv) {
    $Args += "--exclude-venv"
}

# Добавляем флаг ForceUpdate, если он включен
if ($ForceUpdate) {
    $Args += "--force-update"
}

# Добавляем интерпретатор, если он отличается от значения по умолчанию
#if ($Interpreter -ne "/venv/Scripts/python.exe") {
#    $Args += "--interpreter", $Interpreter
#}

# Получаем абсолютный путь
$RootPath = Resolve-Path -Path $Path
Write-Host "Запуск скрипта обработки Python файлов в директории RootPath: $RootPath /n Path $Path "

# Проверяем, если путь к Python скрипту правильный
$PythonScriptPath = "./update_files_headers.py"
$PythonExe = "python"  # или полный путь к Python интерпретатору, если не установлен глобально

# Запуск Python-скрипта с передачей аргументов
Write-Host "Запуск Python-скрипта: $PythonExe $PythonScriptPath $Args"
& $PythonExe $PythonScriptPath @Args
