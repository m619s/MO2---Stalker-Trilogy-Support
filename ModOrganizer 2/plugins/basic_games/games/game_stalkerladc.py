from enum import IntEnum
from pathlib import Path

import mobase
from PyQt6.QtCore import QDir, QFileInfo, Qt
from ..basic_game import BasicGame

class StalkerLADCGame(BasicGame):
    Name = "S.T.A.L.K.E.R.: Lost Alpha DC Support Plugin"
    Author = "m619s"
    Version = "1.0"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Lost Alpha DC."

    GameName = "S.T.A.L.K.E.R.: Lost Alpha DC"
    GameShortName = "stalkerlostalphadc"

    GameBinary = "bins/XR_3DA.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/appdata"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    def executables(self) -> list[mobase.ExecutableInfo]:
        info = [
            ["S.T.A.L.K.E.R.: Lost Alpha DC", "bins/XR_3DA.exe"],
            ["Configurator", "Lost Alpha Configurator.exe"],
        ]
        gamedir = self.gameDirectory()
        return [
            mobase.ExecutableInfo(inf[0], QFileInfo(gamedir, inf[1])) for inf in info
        ]

    def mappings(self) -> list[mobase.Mapping]:
        appdata = self.gameDirectory().filePath("appdata")
        m = mobase.Mapping()
        m.createTarget = True
        m.isDirectory = True
        m.source = appdata
        m.destination = appdata
        return [m]