from app import app

# Vercel requires this
application = app

if __name__ == "__main__":
    app.run(debug=False)