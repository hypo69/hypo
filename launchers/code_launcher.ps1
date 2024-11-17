
# Получаем все аргументы командной строки
$arguments = $args

# Проверка, был ли передан путь к Python скрипту
if ($arguments.Count -lt 1) {
    Write-Host "Ошибка: Путь к Python скрипту не был указан."
    exit 1
}

# Путь к Python скрипту (первый аргумент)
$scriptPath = $arguments[0]

# Укажите путь к директории для виртуальной среды
$venvPath = "venv"

# Проверка, существует ли директория venv, если нет, создаем виртуальное окружение
if (-not (Test-Path $venvPath)) {
    Write-Host "Создание виртуальной среды..."
    python -m venv $venvPath
}

# Активируем виртуальное окружение
& "$venvPath\Scripts\Activate"

# Устанавливаем зависимости, если необходимо
# Например, из requirements.txt
# pip install -r requirements.txt

# Запускаем Python скрипт
python $scriptPath

# Деактивируем виртуальное окружение после выполнения скрипта
deactivate
