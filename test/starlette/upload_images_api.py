from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import os

async def upload(request):
    form = await request.form()
    images = form.getlist('image')
    print(f"images: {len(images)}")
    for image in images:
        filename = image.filename
        print(f"processing: {filename}")
        # with open(os.path.join('./uploads', filename), 'wb') as f:
        #     f.write(await file.read())
    return PlainTextResponse('Upload success!')

app = Starlette(routes=[
    Route('/upload', endpoint=upload, methods=['POST']),
])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=5000)