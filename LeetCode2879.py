import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

#  head serve para mostrar oq tem dentro do data frame(tipo um output), e quando colocamos um numero dentro dele limitamos a quantidade de dados q vai aparecer nesse caso das rows ou colunas