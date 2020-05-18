import pandas as pd
import numpy as np
from oop_class import calculation
auto = pd.read_csv('autos.csv')
z = auto.head(5)
cc = calculation(auto)

sub_auto = ['price', 'hw_mpg']

cc.maxs(sub_auto)
cc.mins(sub_auto)
cc.summ(sub_auto)
cc.means(sub_auto)





