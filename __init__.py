# __init__.py
# Minimal package init to expose the whiet_node to ComfyUI

from .whiet_node import WhietNode
from .midi_node_01  import WhietMidi01Node

# Optional: expose node mappings at package level
NODE_CLASS_MAPPINGS = {"WhietNode": WhietNode}
NODE_DISPLAY_NAME_MAPPINGS = {"WhietNode": "whiet"}
NODE_CLASS_MAPPINGS = {"WhietMidi01Node": WhietMidi01Node}
NODE_DISPLAY_NAME_MAPPINGS = {"WhietMidi01Node": "whiet"}
