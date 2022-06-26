import pandas as pd
from tool.pd_tool import PandasTool

data ={
    "flower":["スズラン", "リンゴ", "キリ"],
    "prefectures":["北海道", "青森県", "岩手県"],
    "family":["ユリ科", "バラ科", "ゴマノハグサ科"],
    "hanakotoba":["繊細・幸福はふたたび", "誘惑", "-"]
}
df = pd.DataFrame(data)
columns_list = ["hanakotoba", "flower"]
condition = "flower == 'スズラン'"
mod_df = PandasTool().return_df_specified_columns(df, columns_list, condition)
print(mod_df)