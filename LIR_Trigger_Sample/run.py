from typing import Dict

import pandas as pd

def run(data_frame: pd.DataFrame) -> Dict[str, int]:
    """
    Performs a mock "analysis" (just calculates the number of rows and columns)

    Returns:
        Dict[str, int]: Information about the shape of the DataFrame
    """
    return {
        "num_rows": len(data_frame),
        "num_cols": len(data_frame.columns)
    }