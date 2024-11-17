
#Установить политику выполнения для текущего пользователя, разрешив выполнение всех скриптов:
Set-ExecutionPolicy Unrestricted -Scope CurrentUser

# Получение пути к директории исполняюого файла
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Собираю пути
# $doxygenPath = Join-Path $scriptDirectory "\bin\doxygen\doxygen.exe"
# $enDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\en.doxy"
# $ruDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\ru.doxy"

$doxygenPath = Join-Path $scriptDirectory "\bin\doxygen\doxygen.exe"
$enDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\en.doxy"
$ruDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\ru.doxy"

# Переходим в рабочий каталог скрипта
Set-Location -Path $scriptDirectory

# Запускаю EN doxygen
Start-Process -FilePath $doxygenPath -ArgumentList $enDoxyfilePath -Wait

# Запускаю RU doxygen
Start-Process -FilePath $doxygenPath -ArgumentList $ruDoxyfilePath -Wait

Start-Process -FilePath bin/doxygen/doxygen.exe -ArgumentList docs/doxygen/ru.doxy -Wait
Start-Process -FilePath bin/doxygen/doxygen.exe -ArgumentList docs/doxygen/en.doxy -Wait


# Путь к HTML-документу
$htmlFilePath = "docs\doxygen\_build\ru\html\index.html"

# Проверка существования файла
if (Test-Path $htmlFilePath -PathType Leaf) {
    # Открываю HTML-документ в браузере по умолчанию
    Start-Process $htmlFilePath
} else {
    Write-Host "docs\\doxygen\\_build\\ru\\html\\index.html не найден"
}
