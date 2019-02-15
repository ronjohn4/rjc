from app import app


if __name__ == "__main__":
    print('app.run()')
    # app.run(port=5001, debug=True)
    app.run(port=8000, debug=False)
