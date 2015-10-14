from app import app
import os

if __name__ == "__main__":
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',8080))
    app.run(host,port)