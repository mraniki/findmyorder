
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FMO",
    settings_files=['core.toml','settings.toml','.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
)
