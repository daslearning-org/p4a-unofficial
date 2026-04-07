# Unofficial Usage
This repo is a fork of original P4A project. We may have some new thigs or customization as per our need.
> Note: You need to check other branches like `numpy2` to get the recipes or the modifications, not putting into `develop` to keep it clean.

## Added Recipes
We have creared some new recipies which might not be present in original repo.

1. [OnnxRuntime](./pythonforandroid/recipes/onnxruntime/)
2. [tokenizers](./pythonforandroid/recipes/tokenizers/) (it does not include the huggingface related modules.)


## Android XML & Arg part

### The XML

1. App Orientation Path: `pythonforandroid/bootstraps/_sdl_common/build/templates/AndroidManifest.tmpl.xml`

```xml
android:screenOrientation="fullSensor" <!-- or "fullUser" -->
```

## Customized Arguments
Manifest path: `pythonforandroid/bootstraps/_sdl_common/build/templates/AndroidManifest.tmpl.xml`, python path: `pythonforandroid/bootstraps/common/build/build.py`

1. Added `{{ args.extra_manifest_application_element }}`.
Equivalent p4a command `--extra-manifest-application-element`
