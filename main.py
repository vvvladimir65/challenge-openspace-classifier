from utils.table import Table, Seat
from utils.openspace import Openspace
import pandas as pd
n_tables = 6
n_seats = 4

df = pd.read_excel('./utils/Example Excel Template.xlsx')

colleagues_list = df['Colleagues'].tolist()
print(colleagues_list)
a = Openspace(n_tables,n_seats)
print(a.organize(colleagues_list))
print(a.display())
print(a.store())



