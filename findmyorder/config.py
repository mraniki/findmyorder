
from dynaconf import Dynaconf

fmosettings = Dynaconf(
    envvar_prefix="FMO",
    settings_files=['findmyorder/settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
)
