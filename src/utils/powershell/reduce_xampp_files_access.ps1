## \file hypotez/src/utils/powershell/reduce_xampp_files_access.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.utils.powershell """
MODE = 'debug'
# Укажите путь к директории XAMPP
$xamppPath = "C:\xampp"

# Рекурсивно присвоить полные права доступа всем файлам и папкам
Get-ChildItem -Path $xamppPath -Recurse | ForEach-Object {
    $acl = Get-Acl $_.FullName
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators", "FullControl", "Allow")
    $acl.SetAccessRule($rule)
    Set-Acl -Path $_.FullName -AclObject $acl
}

Write-Host "Полные права доступа были присвоены рекурсивно в директории XAMPP."
