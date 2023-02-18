# deklarasi library dengan menggunakan nama alias
import pandas as pd

nilai = [70, 80, 90, 100, 85]

# membuat variabel dataframe (df) dengan isi list nilai dan nama kolom "nilai"
df = pd.DataFrame(nilai, columns=["nilai"])
df #dataframe
