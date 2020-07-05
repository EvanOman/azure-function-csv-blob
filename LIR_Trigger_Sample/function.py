import json
import logging
from io import StringIO

import azure.functions as func
import pandas as pd

from .run import run

def main(inputstream: func.InputStream, outputstream: func.Out[func.InputStream]) -> None:
    """
    Entrypoint for Azure Function

    Args:
        inputstream (func.InputStream): Input file stream (blob file)
        outputstream (func.Out[func.InputStream]): Output file stream (blob file)
    """
    logging.info("GOT DATA, file named %s", inputstream.name)

    # Read the input stream into a string
    input_data = StringIO(inputstream.read().decode("utf-8"))

    # Make a pandas DataFrame from the CSV string
    df = pd.read_csv(input_data)

    # Run "analysis" and write the output to the output stream as JSON
    results = run(df)
    outputstream.set(json.dumps(results))

    logging.info("DONE")
