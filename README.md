# Bike Configurator App

1. First, you need [Python](https://www.python.org/) and a running [PostgreSQL](https://www.postgresql.org/) database.
2. From the repository root, create and activate a virtual environment, then install the backend packages. Creating a virtual environment alone does not install packages:

   ```sh
   python -m venv .venv
   ```

   Activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\activate` in Windows Command Prompt, then run:

   ```sh
   python -m pip install --upgrade pip
   python -m pip install -r backend/requirements.txt
   ```

   In VS Code, select `.venv` as the Python interpreter. Keep the environment activated. The commands below are run from the repository root unless noted otherwise.
3. Create a **.env** file in `backend` and define `DATABASE_URL=postgresql://{user}:{password}@{host}:{port}/{database}`.
4. Run `python backend/demo/create_user.py` to create a user, then follow the prompts to set a username and password.
5. (Optional) Generate demo content with `cd backend && python -m src.content.create_content`, then return to the repository root.
6. Run FastAPI with `python -m uvicorn src.main:app --app-dir backend --reload --reload-dir backend`.
7. Open http://127.0.0.1:8000/docs to view the OpenAPI documentation.
