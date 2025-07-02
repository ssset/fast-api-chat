from fastapi import FastAPI

def create_app():
    return FastAPI(
        title='simple kafka chat',
        docs_url='/api/docs',
        description='simple kafka + ddd example',
        debug=True
    )