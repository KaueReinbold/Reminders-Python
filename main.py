from website import create_app
from src.data import setup_data
from pathlib import Path

app = create_app()

setup_data(app, f'{Path(__file__).parent}/database.db')

if __name__ == '__main__':
    # HACK: Get environment from the .env file
    app.run(debug=True, port=8000)
