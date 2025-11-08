from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Project(BaseSettings):
    """
    Настройки проекта.
    """

    title: str = "Рочев Максим. Backend-разработчик. Портфолио."
    description: str = "Портфолио описывает все мои проекты, достижения и успехи на пути разработчика."
    contact: dict = {
        "name": "Sladkiy-bubalex",
        "email": "shadow.ru_93@mail.ru",
        "url": "https://github.com/Sladkiy-bubalex",
        "telegram": "https://t.me/ynikum_man",
        "hh": "https://spb.hh.ru/resume/59563580ff0e4805bc0039ed1f385a57596347",
        "github_icon": "https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white",
        "telegram_icon": "https://img.shields.io/badge/Telegram-0088cc?style=flat&logo=telegram&logoColor=white",
        "email_icon": "https://img.shields.io/badge/Email-0078D4?style=flat&logo=mail&logoColor=white",
        "hh_icon": "https://img.shields.io/badge/HeadHunter-00A3E0?style=flat&logo=headhunter&logoColor=white",
    }
    release_version: str = Field(..., alias="PROJECT__RELEASE_VERSION")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="allow"
    )

    def contact_description(self):
        # Используем HTML для более точного контроля над выравниванием
        github_link = f'<a href="{self.contact["url"]}" target="_blank"><img src="{self.contact["github_icon"]}" style="vertical-align: middle; margin-right: 10px;"></a>'
        telegram_link = f'<a href="{self.contact["telegram"]}" target="_blank"><img src="{self.contact["telegram_icon"]}" style="vertical-align: middle; margin-right: 10px;"></a>'
        email_link = f'<a href="mailto:{self.contact["email"]}"><img src="{self.contact["email_icon"]}" style="vertical-align: middle; margin-right: 10px;"></a>'
        hh_link = f'<a href="{self.contact["hh"]}" target="_blank"><img src="{self.contact["hh_icon"]}" style="vertical-align: middle; margin-right: 10px;"></a>'
        
        # Разделяем контакты на разные строки
        return f"{github_link}<br>{telegram_link}<br>{email_link}<br>{hh_link}"


class Settings(BaseSettings):
    """
    Настройки проекта.
    """

    debug: bool = Field(default=True)
    log_level: str = Field(default="INFO")
    project: Project = Field(default_factory=Project)
    base_url: str = Field(default="http://0.0.0.0:8000")
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="allow"
    )


settings = Settings()