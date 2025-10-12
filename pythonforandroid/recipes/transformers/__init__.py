from pythonforandroid.recipe import PyProjectRecipe
from os.path import join, realpath, dirname, exists
import os
import shutil

class TransformersRecipe(PyProjectRecipe):
    version = '4.57.0'  # Replace with the exact version you want to build
    url = 'https://github.com/huggingface/transformers/archive/refs/tags/v{version}.tar.gz'

    # Dependencies to include (excluding huggingface_hub, safetensors, tokenizers, etc.)
    # These are pulled from install_requires; add more if needed for your use case
    depends = ['filelock', 'packaging', 'pyyaml', 'regex', 'requests']

    # If you need to patch the source to remove excluded dep references, list patch files here
    #patches = ['patches/init.patch']

    # Optional: site-packages name if different
    site_packages_name = 'transformers'

    def get_recipe_dir(self):
        return dirname(realpath(__file__))

    # remove the original __init__ with Tokenizer & Config modules only
    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        recipe_dir = self.get_recipe_dir()
        print(f"Transformers build dir: {build_dir}")
        init_file = join(build_dir, 'src', 'transformers', '__init__.py')
        update_init = join(recipe_dir, 'patches', 'init.py')
        if exists(init_file):
            os.remove(init_file)
        shutil.copyfile(update_init, init_file)
        print(f"Copied transformers init from {update_init} to {init_file}")
        # trigger the main build
        super().build_arch(arch)

recipe = TransformersRecipe()