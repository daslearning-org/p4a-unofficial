from pythonforandroid.recipe import RustCompiledComponentsRecipe
import os
import shutil

class TokenizersRecipe(RustCompiledComponentsRecipe):
    name = 'tokenizers'
    version = '0.22.1'
    url = 'https://github.com/huggingface/tokenizers/archive/refs/tags/v{version}.tar.gz'
    sha512sum = "1a25ee6b218232112f10bc1e082e71ed1960ab7fa62c7341b38cc5f5dc0a735cf35b3e90d4a1c1cc0aedb7c198182c2e559662459a668a2fef4e633096a1cccc"
    depends = []  # No dependencies since we're skipping huggingface_hub
    patches = [
        'patches/pyproject.patch',
    ]

    def get_build_dir(self, arch):
        # Use the default build directory (e.g., .../other_builds/tokenizers/arm64-v8a__ndk_target_28/tokenizers)
        build_dir = super().get_build_dir(arch)
        # The bindings/python directory will be inside the extracted source
        src_dir = super().get_recipe_dir()  # Root of the extracted tarball
        python_dir = os.path.join(src_dir, 'bindings', 'python')
        
        # Ensure the build directory contains only the contents of bindings/python
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)  # Clean the default build directory
        shutil.copytree(python_dir, build_dir, dirs_exist_ok=True)
        
        # Verify that pyproject.toml exists in the build directory
        if not os.path.exists(os.path.join(build_dir, 'pyproject.toml')):
            self.logger.error(f"pyproject.toml not found in {build_dir}")
            raise FileNotFoundError(f"pyproject.toml not found in {build_dir}")
        
        return build_dir

recipe = TokenizersRecipe()