## Requirements
- Python 3.10+
- pip

## Setup and run

1. Create a virtual environment

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment
windows: 
    ```bash
    venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI server
    ```bash
    uvicorn main:app --reload
    ```