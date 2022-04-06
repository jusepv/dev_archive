import numpy as np
import pandas as pd


"""
long : long form으로 되어 있는 데이터이며, 바꾸려는 데이터를 해당 변수로 로드하면 됩니다.
wide : wide form으로 되어 있는 데이터이며, merge하려는 데이터를 해당 변수로 로드하면 됩니다.

"""
long = pd.read_csv('Control Q2.csv')
long.rename(columns = {"Study.No": "Study No"}, inplace = True)

wide = pd.read_csv('BelloCool Control.csv', encoding='cp949')

# EPIC part
EPIC = long[['Study No','EPIC_t', 'EPIC_Q1', 'EPIC_SS1', 'EPIC_SS2', 'EPIC_SS3', 'EPIC_SS4', 'EPIC_SS5', 'EPIC_TS']]
EPIC = EPIC.dropna(axis=0)

EPIC_pivot = EPIC.pivot_table(index='Study No', columns='EPIC_t')
EPIC_pivot.columns = EPIC_pivot.columns.get_level_values(1)+ '_' +  EPIC_pivot.columns.get_level_values(0)
EPIC_pivot = EPIC_pivot.reset_index()
epic_on = EPIC_pivot.columns.tolist()

# IIEF part
IIEF = long[['Study No', 'IIEF_t', 'IIEF_1', 'IIEF_2','IIEF_3', 'IIEF_4',	'IIEF_5', 'IIEF_S']]
IIEF = IIEF.dropna(axis=0)

IIEF_pivot = IIEF.pivot_table(index='Study No', columns='IIEF_t')
IIEF_pivot.columns = IIEF_pivot.columns.get_level_values(1)+ '_' +  IIEF_pivot.columns.get_level_values(0)
IIEF_pivot = IIEF_pivot.reset_index()
iief_on = IIEF_pivot.columns.tolist()

# EQ5D part
EQ5D = long[['Study No', 'EQ5D_t', 'EQ5D_1', 'EQ5D_2', 'EQ5D_3', 'EQ5D_4', 'EQ5D_5', 'EQ5D_U', 'EQ5D_VAS']]

EQ5D_pivot = EQ5D.pivot_table(index='Study No', columns='EQ5D_t',aggfunc='sum')
EQ5D_pivot.columns = EQ5D_pivot.columns.get_level_values(1)+ '_' +  EQ5D_pivot.columns.get_level_values(0)
EQ5D_pivot = EQ5D_pivot.reset_index()
eq5d_on = EQ5D_pivot.columns.tolist()


#merge part
wide_ls = wide.columns.tolist()
wide_ls =wide_ls[0:52]

wide_table = wide[wide_ls]
wide_epic = wide[epic_on]
wide_iief = wide[iief_on]
wide_eq5d = wide[eq5d_on]


df1 = pd.concat([wide_epic, EPIC_pivot]).groupby(['Study No'], dropna=False).sum(min_count=1).reset_index()
df2 = pd.concat([wide_iief, IIEF_pivot]).groupby(['Study No'], dropna=False).sum(min_count=1).reset_index()
df3 = pd.concat([wide_eq5d, EQ5D_pivot]).groupby(['Study No'], dropna=False).sum(min_count=1).replace(0,np.NaN).reset_index()

merge1 = pd.merge(df1,df2, on='Study No', how='outer')
merge2 = pd.merge(merge1, df3, on='Study No', how='outer')
merge3 = pd.merge(wide_table, merge2, on='Study No', how='outer')


merge3.to_csv('result.csv')