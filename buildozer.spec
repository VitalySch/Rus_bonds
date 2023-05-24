[app]

# (str) Title of your application
title = Russian Bonds

# (str) Package name
package.name = rus_bonds

# (str) Package domain (needed for android/ios packaging)
package.domain = org.VitalySch

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas,po,mo

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.0.0

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/logo/presplash512okmin.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/logo/logo512min.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
# orientation = all



# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.0.0

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false




[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

