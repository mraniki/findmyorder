
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TEST",
    settings_files=['findmyorder/default_settings.toml','settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
    validators=[
        Validator("loglevel", default="INFO", apply_default_on_none=True),
        ]
)
