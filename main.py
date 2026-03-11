from fastapi import FastAPI

app = FastAPI(title="1.5 GiB Single-Function App", version="1.0.0")


@app.get("/")
def app_info():
    return {
        "message": "This app now exposes a single function.",
        "size_strategy": "Dependency install footprint",
        "measured_dependency_bytes": 1629461844,
        "target_bytes": 1610612736,
    }
