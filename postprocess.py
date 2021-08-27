import sys
import pandas as pd
import json
import os

if __name__ == "__main__":
  
    with open('bitmex-leaderboard.json', 'r') as f:
        data = json.load(f)
    new_raw_df = pd.DataFrame(data['data'])
    new_raw_df['timestamp'] = pd.to_datetime(new_raw_df['timestamp'], unit='s')

    output_fname = "df_output.csv"
    if not os.path.exists(output_fname):
        new_raw_df.to_csv(output_fname)
    else:
        old_df = pd.read_csv(output_fname, index_col=0)
        new_df = pd.concat([old_df, new_raw_df])
        new_df.to_csv(output_fname)
