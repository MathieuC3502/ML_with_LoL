@echo off
setlocal

REM Chemin vers le dossier de l'environnement virtuel
set VENV_DIR=ml_with_lol_env

REM Verifie si l'option -u est presente
set UPDATE_FLAG=false
if "%1"=="-u" (
    set UPDATE_FLAG=true
)

REM Verifie si l'environnement virtuel existe
if exist "%VENV_DIR%" (
    echo Activation de l'environnement virtuel existant...
    call "%VENV_DIR%\Scripts\activate.bat"
    echo Mise a jour de pip...
    python -m pip install --upgrade pip
    if %UPDATE_FLAG%==true (
        echo Mise a jour des dependances a partir de requirements.txt...
        pip install --upgrade -r requirements.txt -v
        if %errorlevel% neq 0 (
            echo Erreur lors de la mise a jour des dependances.
            exit /b %errorlevel%
        )
    )
) else (
    echo Creation d'un nouvel environnement virtuel...
    python -m venv "%VENV_DIR%"
    if %errorlevel% neq 0 (
        echo Erreur lors de la creation de l'environnement virtuel.
        exit /b %errorlevel%
    )
    call "%VENV_DIR%\Scripts\activate.bat"
    echo Mise a jour de pip...
    python -m pip install --upgrade pip
    echo Installation des dependances a partir de requirements.txt...
    pip install -r requirements.txt -v
    if %errorlevel% neq 0 (
        echo Erreur lors de l'installation des dependances.
        exit /b %errorlevel%
    )
)

REM Votre code ici, apres l'activation de l'environnement virtuel

endlocal