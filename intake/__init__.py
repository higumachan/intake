# Plugin registry

from . import plugins
from .catalog import load_catalog

registry = plugins.registry

# Automatically create shortcut open methods
for key, value in registry.items():
    globals()['open_' + key] = value.open

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
