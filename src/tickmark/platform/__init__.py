"""Access to the operating system: cursor, screen pixels, global hotkeys.

``base`` defines the interfaces the UI programs against. Each operating system
gets its own backend module; a backend states what it can do through
``capabilities`` instead of failing silently.
"""
