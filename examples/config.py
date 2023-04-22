
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FMO",
    settings_files=['settings.toml','core.toml','.secrets.toml'],
)
