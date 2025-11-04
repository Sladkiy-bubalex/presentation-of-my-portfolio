from fastapi import APIRouter
from .projects.views import router as project_router
from .сertificates.views import router as certificate_router


router = APIRouter()
router.include_router(project_router, prefix="/projects", tags=["Projects"])
router.include_router(certificate_router, prefix="/certificates", tags=["Certificates"])
