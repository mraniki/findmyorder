
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TEST",
    settings_files=['findmyorder/default_settings.toml','settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
)
