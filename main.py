from website import create_app
from src.data import setup_data

from src.service import setup_service

app = create_app()

setup_data(app)
setup_service()

if __name__ == '__main__':
    # HACK: Get environment from the .env file
    app.run(debug=True, port=8000)
