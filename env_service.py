"""
Tableau Service Environment Loader Module

This module, `env_service`, provides a specialized environment loading service 
for Tableau-related modules. It ensures that each service instance loads environment 
variables automatically from a `.env` file located in the service's directory.

Classes:
    - EnvService: Inherits from `EnvBase` and is designed specifically for use in 
      Tableau service modules. It loads the environment variables when initialized, 
      allowing seamless access to configuration settings without repetitive code.

Usage:
    The `EnvService` class should be used as a base for any service module that 
    requires automatic environment variable loading. When instantiated, it loads 
    environment variables from the directory-specific `.env` file, making the 
    configuration accessible throughout the class.

Example:
    To use `EnvService` in a service module, simply inherit from it and initialize 
    the instance. The environment variables will be loaded automatically:
    
    ```python
    from tableau_service.env_service import EnvService

    class ExampleService(EnvService):
        def __init__(self):
            super().__init__()
            # Environment variables are now loaded and accessible
    ```

Dependencies:
    - config.env_base.EnvBase: The base class responsible for setting up environment 
      loading functionality. `EnvService` extends `EnvBase` to automate the loading 
      process in service modules.

"""

from config.env_base import EnvBase


class EnvService(EnvBase):
    """
    Service-specific environment loader that inherits from EnvBase.
    Automatically loads variables from the specified `.env` file in the service's directory.
    """
    
    def __init__(self):
        # Load environment variables with minimal code
        self.load_env_variables()