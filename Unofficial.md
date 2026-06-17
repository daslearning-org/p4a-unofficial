# Unofficial Usage
This repo is a fork of original P4A project. We may have some new thigs or customization as per our need.
> Note: You need to check other branches like `dasfix` to get the recipes or the modifications, not putting into `develop` to keep it clean.

## Added Recipes
We have creared some new recipies which might not be present in original repo.

1. [OnnxRuntime](./pythonforandroid/recipes/onnxruntime/)
2. [tokenizers](./pythonforandroid/recipes/tokenizers/) (it does not include the huggingface related modules.)

## Android XML & Arg part

### The XML

1. XML Customisation can be done on: `pythonforandroid/bootstraps/_sdl_common/build/templates/AndroidManifest.tmpl.xml`

## Customized Arguments
Manifest path: `pythonforandroid/bootstraps/_sdl_common/build/templates/AndroidManifest.tmpl.xml`, python path: `pythonforandroid/bootstraps/common/build/build.py`

1. Added `{{ args.extra_manifest_application_element }}`.
Equivalent p4a command `--extra-manifest-application-element`

## What's new?
- It is having `onnxruntime 1.25.1` recipe.
- It is having `tokenizers 0.22.1` recipe which does not include the `huggingface_hub` related modules.
- It has an extra feature where you can place an entire xml block into `<application>` tag, for example a custom `service` tag. You can use `--extra-manifest-application-element` or `extra_manifest_application_element` if you use our [buildozer-unofficial](https://github.com/daslearning-org/buildozer-unofficial/tree/develop) with `develop` branch.
