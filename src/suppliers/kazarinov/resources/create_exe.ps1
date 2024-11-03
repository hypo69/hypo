#pyinstaller --onefile --name kazarinov_bot --add-data "../resources/*;." --add-data "icons/*;icons" --distpath ".." "..\bot.py"
pyinstaller --onefile --name kazarinov_bot --add-data "../resources/*;."  --distpath "..\..\..\exe\kazarinov" "..\bot.py"
