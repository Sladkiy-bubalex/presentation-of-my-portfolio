from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse, RedirectResponse
from settings import settings
from api import router as api_router


app = FastAPI(
    title=settings.project.title,
    description=settings.project.description + '\n\n' + settings.project.contact_description(),
    version=settings.project.release_version,
    docs_url=None,
    redoc_url=None,
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix="/api")

@app.get("/docs", include_in_schema=False)
async def custom_docs():
    swagger_html = get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=settings.project.title,
        swagger_favicon_url="/static/logo.png",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui.css",
        swagger_ui_parameters={
            "docExpansion": "none",
            "defaultModelsExpandDepth": -1,
            "displayRequestDuration": True
        },
    )

    content = swagger_html.body.decode("utf-8").replace(
        "</head>",
        '<link rel="stylesheet" type="text/css" href="/static/custom_swagger.css">\n</head>'
    )

    content = content.replace(
        "</body>",
        '<script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui-standalone-preset.js"></script>\n</body>'
    )

    return HTMLResponse(content=content)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs#/Projects")
