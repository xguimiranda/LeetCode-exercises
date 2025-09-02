from ast import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
# 

def getDataframeSizeV2(players: pd.DataFrame) -> List[int]:
    return list(players.shape)