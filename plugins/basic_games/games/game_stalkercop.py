from ..basic_game import BasicGame

class StalkerCoPGame(BasicGame):
    Name = "[WW/RU] S.T.A.L.K.E.R.: Call of Pripyat Support Plugin"
    Author = "m619s"
    Version = "0.3.6"
    Description = "Adds basic support for game S.T.A.L.K.E.R.: Call of Pripyat."

    GameName = "S.T.A.L.K.E.R.: Call of Pripyat"
    GameShortName = "stalkercallofpripyat"
    GameNexusName = "stalkercallofpripyat"

    GameBinary = "bin/xrEngine.exe"

    GameDataPath = ""
    GameDocumentsDirectory = "%GAME_PATH%/_appdata_"
    GameIniFiles= "%GAME_DOCUMENTS%/user.ltx"
    GameSaveExtension = "scop"
    GameSavesDirectory = "%GAME_DOCUMENTS%/savedgames"

    GameSteamId = 41700