from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/image-sticking/upload')
async def upload_image(file: UploadFile):
    return {
        'filename': file.filename,
        'file_content_type': file.content_type,
    }