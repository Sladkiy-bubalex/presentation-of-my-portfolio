from fastapi.responses import FileResponse


async def get_certs(path: str):
    return FileResponse(path)
