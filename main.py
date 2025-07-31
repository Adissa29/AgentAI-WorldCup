from fastapi import FastAPI
from gui.interface import app as interface_app

app = interface_app

if __name__ == "__main__":
    import uvicorn
    import webbrowser
    import threading

    def open_browser():
        webbrowser.open_new_tab("http://127.0.0.1:8000/docs")

    threading.Timer(1.5, open_browser).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
