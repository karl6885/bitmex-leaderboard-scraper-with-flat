import sys
import pandas as pd
import json

if __name__ == "__main__":
  
    with open('bitmex-leaderboard.json', 'r') as f:
        data = json.load(f)
    new_raw_df = pd.DataFrame(data['data'])

    old_df = pd.read_csv("df_output.csv")
    new_df = pd.concat([old_df, new_raw_df])
    new_df.to_csv("df_output.csv")
