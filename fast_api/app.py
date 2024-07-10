from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'GET OLÁ MUNDO!'}

@app.post('/')
def read_root():
    return {'message': 'POST Olá Mundo!'}
