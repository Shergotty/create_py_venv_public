# config/env_loader.py

from pydantic_settings import BaseSettings
from pydantic import ValidationError
from pathlib import Path

class EnvHelperSettings(BaseSettings):
    """
    EnvHelperSettings loads environment variables using Pydantic's BaseSettings.
    Configured to allow extra variables without explicitly defining them.
    """
    class Config:
        extra = 'allow'  # Allows extra variables not explicitly defined

class EnvLoad:
    """
    EnvLoad class detects and loads environment variables from a specified `.env` file path,
    setting them as attributes on the specified instance.
    """
    
    @classmethod
    def load_into_instance(cls, instance, env_file_path: str):
        # Resolve the path to ensure it's absolute
        env_path = Path(env_file_path).resolve()

        # Check if the `.env` file exists
        if not env_path.exists():
            raise FileNotFoundError(f".env file not found at: {env_path}")

        try:
            # Load environment variables and set them as attributes on the instance
            loaded_settings = EnvHelperSettings(_env_file=str(env_path)).model_dump()

            for key, value in loaded_settings.items():
                setattr(instance, key, value)  # Dynamically set as an attribute on the instance

        except ValidationError as e:
            raise EnvironmentError(f"Missing or invalid environment variables: {e.errors()}")