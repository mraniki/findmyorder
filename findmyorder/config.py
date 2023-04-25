
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FMO",
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
    validators=[
        Validator("loglevel", default="INFO", apply_default_on_none=True),
        Validator("identifier", default=["BUY", "SELL", "buy", "sell","Buy","Sell"],apply_default_on_none=True),
        ]
)
