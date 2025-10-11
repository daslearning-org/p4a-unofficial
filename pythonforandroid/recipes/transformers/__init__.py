from pythonforandroid.recipe import PyProjectRecipe

class TransformersRecipe(PyProjectRecipe):
    version = '4.57.0'  # Replace with the exact version you want to build
    url = 'https://github.com/huggingface/transformers/archive/refs/tags/v{version}.tar.gz'

    # Dependencies to include (excluding huggingface_hub, safetensors, tokenizers, etc.)
    # These are pulled from install_requires; add more if needed for your use case
    depends = ['filelock', 'packaging', 'pyyaml', 'regex', 'requests']

    # If you need to patch the source to remove excluded dep references, list patch files here
    patches = [
        'patches/init.patch',
    ]

    # Optional: site-packages name if different
    site_packages_name = 'transformers'

recipe = TransformersRecipe()