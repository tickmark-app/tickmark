import os

# Run Qt without a display unless the developer asks for a real one.
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
