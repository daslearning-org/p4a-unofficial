from pythonforandroid.recipe import RustCompiledComponentsRecipe
import os

class TokenizersRecipe(RustCompiledComponentsRecipe):
    # The name of the package
    name = 'tokenizers'

    # Use a specific, recent version from their GitHub releases
    version = '0.22.1'

    # The URL to download the source code tarball
    url = 'https://github.com/huggingface/tokenizers/archive/refs/tags/v{version}.tar.gz'
    sha512sum = "1a25ee6b218232112f10bc1e082e71ed1960ab7fa62c7341b38cc5f5dc0a735cf35b3e90d4a1c1cc0aedb7c198182c2e559662459a668a2fef4e633096a1cccc"

    # Point to the subdirectory containing the Python package
    #build_dir = 'bindings/python'
    # List of other recipes this one depends on
    depends = [] # will use only local files as we are skipping huggingface_hub

    def get_build_dir(self, arch):
        src_dir = super().get_build_dir(arch)
        return os.path.join(src_dir, 'bindings', 'python')

# Boilerplate to register the recipe with python-for-android
recipe = TokenizersRecipe()