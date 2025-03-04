# Bike Configurator'S API

1. First, you need [Python](https://www.python.org/) and a running [PostgreSQL](https://www.postgresql.org/) database.
2. Create a virtual environment and install all necessary packages:
   - First alternative, create a virtual environment; for VS Code, create a [Python Environment](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment) and include or install afterwards all required Python packages over pip: ```pip install -r requirements.txt```.
   - Second alternative, install pipenv ```pip install pipenv``` and then install all necessary packages ```pipenv install```.
3. Create a **.env** file where you define the 'DATABASE_URL = 'postgresql://{user}:{password}@{host}:{port}/{database}''.
4. Run the 'create_user.py' file in order to create a user, just follow the instructions for setting user and password.
5. (Optional) Generate demo content; run the `create_content.py` file.
6. Run FastAPI: ```fastapi dev main.py```
7. Open the http://127.0.0.1:8000/docs URL to the openapi.json
