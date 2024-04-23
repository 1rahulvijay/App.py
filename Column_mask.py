import pandas as pd

# Assuming your DataFrame is named df
df = df.apply(lambda x: x.mask(x.astype(str).str.startswith('unnamed'), x.shift(-1)))
