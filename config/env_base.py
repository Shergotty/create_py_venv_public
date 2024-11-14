from config.env_loader import EnvLoad
from pathlib import Path
import importlib.util

class EnvBase:
    """
    Base class for loading environment variables as instance attributes.
    Automatically loads variables from an `.env` file in the subclass's directory.
    Logs a message once loading is complete.
    """

    @classmethod
    def load_env_variables(cls, env_file_name: str = '.env'):
        # Use importlib to get the file path of the module where the class is defined
        module_spec = importlib.util.find_spec(cls.__module__)
        
        if module_spec and module_spec.origin:
            # Calculate the `.env` file path based on the module's directory
            env_file_path = Path(module_spec.origin).parent / env_file_name
            
            # Load environment variables into instance attributes
            EnvLoad.load_into_instance(cls, env_file_path=str(env_file_path))
            
            # Log the successful loading of environment variables
        else:
            raise FileNotFoundError(f"Could not determine the file path for module {cls.__module__}")