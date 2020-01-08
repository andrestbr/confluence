from dashboard.confluence.update_page import update_page
from dashboard.confluence.open_url_in_confluence import open_url_in_confluence

import pandas as pd
import numpy as np

from pandas import Series, DataFrame

donald_page_id = 130204303

df = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'))

print(df)

r = df.to_html()
print(r)

r = update_page(r, donald_page_id)
print(r)
open_url_in_confluence(donald_page_id)