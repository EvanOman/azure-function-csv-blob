import logging
from io import StringIO

import azure.functions as func
import pandas as pd

from .run import run


def main(myblob: func.InputStream):
    logging.info("GOT DATA")
    input_data = StringIO(myblob.read().decode("utf-8"))
    df = pd.read_csv(input_data)
    logging.info(run(df))
