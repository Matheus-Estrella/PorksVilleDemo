set code=./code/main.py
set user=%USERNAME%
set python_path=python
set debugpy_path=C:/Users/%user%/.vscode/extensions/ms-python.debugpy-2024.10.0-win32-x64/bundled/libs/debugpy/launcher
set port=52801
set host=127.0.0.1

cmd /C "%python_path% -m debugpy --listen %host%:%port% --wait-for-client %code%"
