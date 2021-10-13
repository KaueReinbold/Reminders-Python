from website import create_app

app = create_app()

if __name__ == '__main__':
    # HACK: Get environment from the .env file
    app.run(debug=True)
