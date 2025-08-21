# __init__.py
# Minimal package init to expose the whiet_node to ComfyUI

from .whiet_node import WhietNode

# Optional: expose node mappings at package level
NODE_CLASS_MAPPINGS = {"WhietNode": WhietNode}
NODE_DISPLAY_NAME_MAPPINGS = {"WhietNode": "whiet"}
