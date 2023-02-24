# install library mlxtend
!pip install mlxtend

import pandas as pd
import numpy as np
# import apriori from library mixtend
from mlxtend.frequent_patterns import apriori, association_rules

# membuat data tabular yang terdiri dari data transaksi
df = pd.DataFrame(
    {
        "ID Transaksi": pd.Series([1, 2, 3, 4, 5]),
        "Item": pd.Series([["Susu", "Roti", "Biskuit", "Mentega"],\
                           ["Susu", "Biskuit", "Gula", "Kopi"], \
                           ["Gula", "Kopi", "Susu"], ["Kopi", "Biskuit", "Susu", "Gula"], \
                           ["Mentega", "Roti", "Kopi"]])
    }
)

df = df.explode('Item')
df

basket = (df.groupby(['ID Transaksi', 'Item'])['Item'].count()\
                                      .unstack().reset_index().fillna(0)\
                                      .set_index('ID Transaksi'))
basket.head()
