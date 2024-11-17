
# Запрашиваем у пользователя ввод пути к корневой директории
$rootPath = Read-Host "Введите путь к корневой директории"

# Проверяем, существует ли указанная директория
if (-not (Test-Path $rootPath -PathType Container)) {
    Write-Host "Указанная директория не существует. Завершение скрипта."
    exit
}

# Запрашиваем у пользователя ввод новой ширины или устанавливаем значение по умолчанию
$newWidth = Read-Host "Введите новую ширину (по умолчанию 1200)"
if (-not $newWidth) {
    $newWidth = 1200
}

# Функция для изменения размера изображения с сохранением пропорций
function Resize-Image {
    param (
        [string]$imagePath,
        [int]$newWidth
    )

    # Получаем имя файла без расширения
    $baseFileName = [System.IO.Path]::GetFileNameWithoutExtension($imagePath)

    # Проверяем, содержит ли имя файла индикатор разрешения
    if ($baseFileName -match "^${newWidth}_") {
        Write-Host "Индикатор разрешения уже присутствует в имени файла. Пропуск: $imagePath"
        return $imagePath
    }

    # Создаем объект для работы с изображением
    $image = [System.Drawing.Image]::FromFile($imagePath)

    # Рассчитываем новые размеры с сохранением пропорций
    $newHeight = [math]::Round(($newWidth / $image.Width) * $image.Height)

    # Создаем новый объект изображения с новыми размерами
    $newImage = New-Object System.Drawing.Bitmap -ArgumentList ($image, $newWidth, $newHeight)

    # Составляем полное имя нового изображения
    $newImageName = "${newWidth}_${baseFileName}" + [System.IO.Path]::GetExtension($imagePath)

    # Составляем полный путь для сохранения нового изображения
    $newImagePath = [System.IO.Path]::Combine([System.IO.Path]::GetDirectoryName($imagePath), $newImageName)

    # Проверяем, существует ли файл с таким именем
    $counter = 1
    while (Test-Path $newImagePath) {
        # Если файл существует, пробуем следующий номер
        $counter++
        $newImageName = "${newWidth}_${baseFileName}_$counter" + [System.IO.Path]::GetExtension($imagePath)
        $newImagePath = [System.IO.Path]::Combine([System.IO.Path]::GetDirectoryName($imagePath), $newImageName)
    }

    # Сохраняем новое изображение, только если файл с таким именем не существует
    if (-not (Test-Path $newImagePath)) {
        $newImage.Save($newImagePath)
    }

    # Закрываем исходное изображение
    $image.Dispose()
    $newImage.Dispose()

    # Возвращаем путь к новому изображению
    return $newImagePath
}

# Рекурсивно проходим по всем файлам в директории и её поддиректориях
Get-ChildItem -Path $rootPath -Recurse -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|gif)$' } | ForEach-Object {
    # Получаем путь к текущему изображению
    $currentImagePath = $_.FullName

    # Изменяем размер изображения
    $resizedImagePath = Resize-Image -imagePath $currentImagePath -newWidth $newWidth

    # Выводим информацию о каждом измененном изображении
    Write-Host "Изображение изменено: $resizedImagePath"
}
