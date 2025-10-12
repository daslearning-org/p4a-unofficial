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
        'patches/cargo.patch'
    ]

    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        print(f"Build dir: {build_dir}")
        tmp_tokenizer_dir = os.path.abspath(os.path.join(build_dir, "..", "temp_toneknizer"))
        tmp_tokenizer_dir_base = os.path.join(tmp_tokenizer_dir, "tokenizers")
        python_dir = os.path.join(build_dir, 'bindings', 'python')
        base_tokenizers = os.path.join(build_dir, 'tokenizers')
        shutil.copytree(python_dir, tmp_tokenizer_dir, dirs_exist_ok=True) # copy python binding to temp dir
        shutil.copytree(base_tokenizers, tmp_tokenizer_dir_base, dirs_exist_ok=True) # copy the tokenizers base
        shutil.rmtree(build_dir)  # Clean the default build directory
        shutil.copytree(tmp_tokenizer_dir, build_dir, dirs_exist_ok=True) # copy back only the python bindings folder
        shutil.rmtree(tmp_tokenizer_dir) # remove temp dir
        # Verify that pyproject.toml exists in the build directory
        if not os.path.exists(os.path.join(build_dir, 'pyproject.toml')):
            print(f"pyproject.toml not found in {build_dir}")
            raise FileNotFoundError(f"pyproject.toml not found in {build_dir}")
        # trigger the main build
        super().build_arch(arch)

recipe = TokenizersRecipe()