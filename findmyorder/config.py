import os
from dynaconf import Dynaconf, Validator

ROOT = os.path.dirname(__file__)

settings = Dynaconf(
    envvar_prefix="FMO",
    project_root=os.path.dirname(ROOT),
    settings_files=[
        os.path.join(ROOT, "default_settings.toml"),
        os.path.join(ROOT, "settings.toml"),
        os.path.join(ROOT, ".secrets.toml"),
    ],
    # settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
    environments=True,
    default_env="default",
    validators=[
        Validator("loglevel", default="INFO", apply_default_on_none=True),
        Validator("identifier", default=["BUY", "SELL", "buy", "sell","Buy","Sell"],apply_default_on_none=True),
        ]
)


# settings.validators.validate()