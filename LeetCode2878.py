from ast import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
# Every DataFrame in pandas has a shape attribute. When you call it, it returns a tuple (number of rows, number of columns). In our case, for the given players DataFrame, the shape would be (10, 5) because there are 10 players and 5 attributes for each player.

def getDataframeSizeV2(players: pd.DataFrame) -> List[int]:
    return list(players.shape)