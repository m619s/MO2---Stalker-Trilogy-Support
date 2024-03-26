from ..basic_game import BasicGame

class StalkerSoCGame(BasicGame):
    Name = "[Steam/WW/RU] S.T.A.L.K.E.R. Support Plugin"
    Author = "m619s"
    Version = "0.3.1"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Shadow of Chernobyl."

    GameName = "S.T.A.L.K.E.R.: Shadow of Chernobyl"
    GameShortName = "stalkershadowofchernobyl"
    GameNexusName = "stalkershadowofchernobyl"

    GameBinary = "bin/XR_3DA.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/_appdata_"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    GameSteamId = 4500