from ..basic_game import BasicGame

class StalkerCSGame(BasicGame):
    Name = "[Steam/WW/RU] S.T.A.L.K.E.R.: Clear Sky Support Plugin"
    Author = "m619s"
    Version = "0.1"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Clear Sky."

    GameName = "S.T.A.L.K.E.R.: Clear Sky"
    GameShortName = "stalkerclearsky"
    GameNexusName = "stalkerclearsky"

    GameBinary = "bin/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/_appdata_"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    GameSteamId = 20510