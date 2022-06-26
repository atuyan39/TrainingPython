import pandas as pd

class PandasTool():
    def __init__(self):
        pass

    def return_df_specified_columns(self, target_df:pd.DataFrame, target_columns_list:list, condition:str=None):
        """ 条件に当てはまる指定したカラムのDFを返却する.

        Args:
            target_df (pd.DataFrame): _description_
            target_columns_list (list): _description_
            condition (str, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """ 
        df = target_df
        # 指定されたカラムが存在するか
        # target_columns_listの全ての要素が、target_df.columnsに含まれるか判定する
        if set(target_columns_list).issubset(df.columns):
            print("exists ")
        else:
            print("Not exists")
            return None
        
        # 指摘された条件式でqueryを実行
        if condition:
            df = df.query(condition)

        # カラムの順番にして返却する
        return df.reindex(columns=target_columns_list)

