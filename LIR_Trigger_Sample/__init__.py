import logging
from io import StringIO

import azure.functions as func
import pandas as pd


def main(myblob: func.InputStream):
    print("GOT DATA")
    input_data = StringIO(myblob.read().decode("utf-8"))
    df = pd.read_csv(input_data)
    logging.info(f"Number of rows: {len(df)}")
