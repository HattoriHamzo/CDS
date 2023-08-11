import os

from types import SimpleNamespace
from dotenv import load_dotenv


class Settings(SimpleNamespace):
    """
    Configuration settings for the application.

    This class loads environment variables from a .env file using the `dotenv` library.

    Attributes:
        Any environment variable defined in the .env file.

    Methods:
        __init__(): Initializes the Settings instance and loads environment variables.
    """

    def __init__(self):
        """
        Initializes a new Settings instance and loads environment variables from .env.
        """
        load_dotenv()
        super().__init__(**os.environ)


settings = Settings()
