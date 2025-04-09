@echo off
set COMPOSE_CMD=podman
set CROSSBAR_IMAGE=crossbario/crossbar

WHERE %COMPOSE_CMD% >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    set COMPOSE_CMD=docker
    )
echo Using %COMPOSE_CMD%
echo Stopping containers
%COMPOSE_CMD% compose down midware
echo Starting containers
%COMPOSE_CMD% compose up -d midware
echo Start finished