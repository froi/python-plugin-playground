"""Simple plugin loader"""

import importlib
from typing import Any
import factory

class ParserInterface:

    @staticmethod
    def initialize(factory:Any) -> None:
        """Initialize the plugin"""

def import_module(name: str) -> ParserInterface:
    return importlib.import_module(name)

def load_plugins(plugins: str) -> None:
    """Load plugins defined in plugins list"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize(factory)