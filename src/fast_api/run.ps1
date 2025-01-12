# Путь к файлу Python скрипта
$pythonScriptPath = ".\src\fast_api\main.py" # <--- Обновлен путь

# Уникальное имя мьютекса (используйте что-то специфичное для вашего приложения)
$mutexName = "Global\FastAPIServerManagerMutex"

# Создаем мьютекс
$mutex = New-Object System.Threading.Mutex($False, $mutexName)

# Пытаемся получить мьютекс
$acquiredMutex = $mutex.WaitOne(0, $False)

if (!$acquiredMutex) {
    Write-Error "Another instance of this script is already running."
    $mutex.Close()
    exit
}

# Функция для запуска сервера
function Start-FastAPIServer {
    param (
        [int]$Port = 8000,
        [string]$Host = "0.0.0.0"
    )

    Write-Host "Starting FastAPI server on port $Port and host $Host..."
    try {
        python $pythonScriptPath --command start --port $Port --host $Host # <--- Изменен вызов
        Write-Host "Server started successfully."
    } catch {
        Write-Error "Failed to start server: $($_.Exception.Message)"
    }
}

# Функция для остановки сервера
function Stop-FastAPIServer {
    param (
        [int]$Port = 8000
    )

    Write-Host "Stopping FastAPI server on port $Port..."
    try {
        python $pythonScriptPath --command stop --port $Port # <--- Изменен вызов
        Write-Host "Server stopped successfully."
    } catch {
        Write-Error "Failed to stop server: $($_.Exception.Message)"
    }
}

# Функция для остановки всех серверов
function Stop-AllFastAPIServers {
    Write-Host "Stopping all FastAPI servers..."
    try {
       python $pythonScriptPath --command stop_all # <--- Изменен вызов
        Write-Host "All servers stopped successfully."
    } catch {
        Write-Error "Failed to stop all servers: $($_.Exception.Message)"
    }
}
# Функция для получения статуса сервера
function Get-FastAPIServerStatus {
    Write-Host "Getting FastAPI server status..."
    try {
       python $pythonScriptPath --command status # <--- Изменен вызов
    } catch {
        Write-Error "Failed to get server status: $($_.Exception.Message)"
    }
}

# Функция для проверки, запущен ли сервер на указанном порту
function Test-PortIsListening {
    param (
        [int]$Port
    )

    try {
        Test-NetConnection -ComputerName localhost -Port $Port -ErrorAction Stop | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Меню для выбора действий
function Show-Menu {
    Write-Host "FastAPI Server Manager"
    Write-Host "----------------------"
    Write-Host "1. Start Server"
    Write-Host "2. Stop Server"
    Write-Host "3. Stop All Servers"
    Write-Host "4. Get Server Status"
    Write-Host "5. Exit"
}

# Главный цикл скрипта
while ($true) {
    Show-Menu

    $choice = Read-Host "Enter your choice (1-5)"

    switch ($choice) {
        "1" {
            $port = Read-Host "Enter port number (default 8000)"
            if (-not $port) {
                $port = 8000
            }
            $host = Read-Host "Enter host address (default 0.0.0.0)"
            if (-not $host) {
                $host = "0.0.0.0"
            }
             if (Test-PortIsListening -Port $port) {
                Write-Host "Server already running on port $port."
            } else {
                Start-FastAPIServer -Port $port -Host $host
            }
        }
        "2" {
            $port = Read-Host "Enter port number to stop"
            if (-not $port) {
                Write-Host "Port number is required"
             } else {
                Stop-FastAPIServer -Port $port
            }
        }
        "3" {
            Stop-AllFastAPIServers
        }
        "4" {
           Get-FastAPIServerStatus
        }
        "5" {
            Write-Host "Exiting..."
            break
        }
        default {
            Write-Host "Invalid choice. Please try again."
        }
    }

    Write-Host ""
}
# Закрываем мьютекс, когда скрипт завершается
$mutex.ReleaseMutex()
$mutex.Close()