from .services import get_certs
from fastapi import APIRouter


router = APIRouter()
BASE_ROOT_IMAGE = "./images/"
RESPONSE_DES = "Возвращает изображение сертификата"


@router.get(
    "/ostrovok",
    name="Ostrovok certificate",
    response_description=RESPONSE_DES
)
async def get_certs_ostrovok():
    """
    Сертификат финалиста в хакатоне от компании Островок.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}ostrovok_cert.png")


@router.get(
    "/lesta-start",
    name="Lesta-Start BackEnd Developer certificate",
    response_description=RESPONSE_DES
)
async def get_certs_lesta_start():
    """
    Сертификат BackEnd Developer от компании Lesta-Start.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}lesta_cert.png")


@router.get(
    "/netology/python-advanced",
    name="Python-advanced certificate",
    response_description=RESPONSE_DES
)
async def get_certs_python_advanced():
    """
    Сертификат Python-разработчик: расширенный курс от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}python_advanced_cert.png")


@router.get(
    "/netology/django",
    name="Django certificate",
    response_description=RESPONSE_DES
)
async def get_certs_django():
    """
    Сертификат Django: создание backend-приложений от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}django_cert.png")


@router.get(
    "/netology/git",
    name="Git certificate",
    response_description=RESPONSE_DES
)
async def get_certs_git():
    """
    Сертификат Git — система контроля версий от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}git_cert.png")


@router.get(
    "/netology/python-database",
    name="Python-database certificate",
    response_description=RESPONSE_DES
)
async def get_certs_python_database():
    """
    Сертификат Базы данных для python- разработчиков от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}python_database_cert.png")


@router.get(
    "/netology/oop",
    name="OOP certificate",
    response_description=RESPONSE_DES
)
async def get_certs_oop():
    """
    Сертификат ООП и работа с API от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}oop_cert.png")


@router.get(
    "/netology/python-web",
    name="Python-web certificate",
    response_description=RESPONSE_DES
)
async def get_certs_python_web():
    """
    Сертификат Основы языка программирования Python от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}python_cert.png")


@router.get(
    "/netology/python-professional",
    name="Python professional certificate",
    response_description=RESPONSE_DES
)
async def get_certs_python_professional():
    """
    Сертификат Профессиональная работа с Python от компании Netology.
    """
    return await get_certs(f"{BASE_ROOT_IMAGE}python_professional_cert.png")
