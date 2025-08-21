# Minimal ComfyUI Node for testing
# Node Name: "whiet"
# Creator: "drWhiet"

class WhietNode:
    """
    Minimal Node to verify loading in ComfyUI
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "x": ("INT", {"default": 1}),
                "y": ("INT", {"default": 2}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "double"
    CATEGORY = "_drWhiet"  # Creator name shown as subcategory

    def double(self, x):
        # Simple test function
        return (x*2,)

# Node registration
NODE_CLASS_MAPPINGS = {"WhietNode": WhietNode}
NODE_DISPLAY_NAME_MAPPINGS = {"WhietNode": "whiet"}
