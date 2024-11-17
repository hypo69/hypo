
# Получаем текущую директорию, где запускается скрипт
$currentDirectory = Get-Location

# Рекурсивная функция для установки прав
function Set-RecursivePermissions ($directory) {
    Get-ChildItem $directory -Recurse | ForEach-Object {
        # Присвоение максимальных прав для всех пользователей
        $_.Attributes = 'Directory'
        $_.Attributes = 'Normal'
    }
}

# Применяем рекурсивную функцию для текущей директории
Set-RecursivePermissions $currentDirectory

Write-Host "Права доступа успешно установлены для всех файлов и директорий."
