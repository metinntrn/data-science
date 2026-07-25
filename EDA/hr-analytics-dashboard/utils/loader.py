from pathlib import Path

import pandas as pd
import streamlit as st

from utils.paths import HR_DATA_FILE


@st.cache_data
def load_data(data_path: Path | str | None = None) -> pd.DataFrame:
    path = Path(data_path) if data_path else HR_DATA_FILE

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            f"Expected file at: {HR_DATA_FILE}"
        )

    return pd.read_csv(path)
