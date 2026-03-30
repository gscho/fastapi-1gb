import sklearn
import PIL
import pandas as pd
import spacy

from fastapi import FastAPI

app = FastAPI(title="1.5 GiB Single-Function App", version="1.0.0")


@app.get("/")
def app_info():
    return {
        "message": "This app now exposes a single function.",
        "size_strategy": "Dependency install footprint",
        "measured_dependency_bytes": 1629461844,
        "target_bytes": 1610612736,
        "imported_modules": {
            "sklearn": sklearn.__version__,
            "PIL": PIL.__version__,
            "pandas": pd.__version__,
            "spacy": spacy.__version__,
        },
    }
