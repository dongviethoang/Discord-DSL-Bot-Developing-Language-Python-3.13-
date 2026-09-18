"""
discordpkg - Discord Bot DSL Package

A Domain-Specific Language (DSL) for creating Discord bots with simplified syntax.

Components:
-----------
- pth.py: Linker layer between DSL and Discord API
- Command system with dynamic mapping
- Environment configuration support
- Real-time console command interface

Usage:
------
from discordpkg.pth import pth, systemcommands

Author: [Beta]
Version: vBeta Testing
"""

# Package version
__version__ = "0.1.0-beta"

# Import main components for easy access
try:
    from .pth import pth, systemcommands
except ImportError:
    # Handle case where dependencies aren't installed
    pass

# Package metadata
__author__ = "[Beta]"
__email__ = ""
__description__ = "Discord Bot DSL Runtime System"
__url__ = ""

# Export main functions
__all__ = [
    'pth',
    'systemcommands'
]
