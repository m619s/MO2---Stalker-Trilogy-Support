from enum import IntEnum
from pathlib import Path

import mobase
from PyQt6.QtCore import QDir, QFileInfo, Qt
from ..basic_game import BasicGame

class StalkerSoC_GogGame(BasicGame):
    Name = "[GOG] S.T.A.L.K.E.R. Support Plugin"
    Author = "m619s"
    Version = "0.4.1"
    Description = "Adds basic support for GOG version of game S.T.A.L.K.E.R.: Shadow of Chernobyl."

    GameName = "S.T.A.L.K.E.R.: Shadow of Chernobyl"
    GameShortName = "stalkershadowofchernobyl"
    GameNexusName = "stalkershadowofchernobyl"

    GameBinary = "bin/XR_3DA.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/_appdata_gog_"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    GameGogId = 1207660573

    def executables(self) -> list[mobase.ExecutableInfo]:
        info = [
            ["S.T.A.L.K.E.R.", "bin/XR_3DA.exe"],
            ["Settings", "Settings.exe"],
        ]
        gamedir = self.gameDirectory()
        return [
            mobase.ExecutableInfo(inf[0], QFileInfo(gamedir, inf[1])) for inf in info
        ]

    def mappings(self) -> list[mobase.Mapping]:
        appdata = self.gameDirectory().filePath("_appdata_gog_")
        m = mobase.Mapping()
        m.createTarget = True
        m.isDirectory = True
        m.source = appdata
        m.destination = appdata
        return [m]