from src.api import create_api
from src.data import setup_data
from pathlib import Path

api = create_api()

setup_data(api, f'{Path(__file__).parent}/database.db')

if __name__ == '__main__':
    # HACK: Get environment from the .env file
    api.run(debug=True, port=8001)
