
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TEST",
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
)
