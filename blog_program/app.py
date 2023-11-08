from website import create_app #folder name

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# to close folder in vs code: CTRL+K -> F
# account name: paul@mail.com, password: 1234567
# account 2: paul2@mail.com, password: 1234567