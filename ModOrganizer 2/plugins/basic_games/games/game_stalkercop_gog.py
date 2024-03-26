from enum import IntEnum
from pathlib import Path

import mobase
from PyQt6.QtCore import QDir, QFileInfo, Qt
from ..basic_game import BasicGame

class StalkerCoP_GogGame(BasicGame):
    Name = "[GOG] S.T.A.L.K.E.R.: Call of Pripyat Support Plugin"
    Author = "m619s"
    Version = "0.2.5"
    Description = "Adds basic support for GOG version of game S.T.A.L.K.E.R.: Call of Pripyat."

    GameName = "S.T.A.L.K.E.R.: Call of Pripyat (GOG)"
    GameShortName = "stalkercallofpripyat"
    GameNexusName = "stalkercallofpripyat"

    GameBinary = "bin/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/_appdata_"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "scop"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    GameGogId = 1207660583

    def executables(self) -> list[mobase.ExecutableInfo]:
        info = [
            ["S.T.A.L.K.E.R.: Call of Pripyat", "bin/xrEngine.exe"],
            ["Settings", "Settings.exe"],
        ]
        gamedir = self.gameDirectory()
        return [
            mobase.ExecutableInfo(inf[0], QFileInfo(gamedir, inf[1])) for inf in info
        ]

    def mappings(self) -> list[mobase.Mapping]:
        appdata = self.gameDirectory().filePath("_appdata_")
        m = mobase.Mapping()
        m.createTarget = True
        m.isDirectory = True
        m.source = appdata
        m.destination = appdata
        return [m]