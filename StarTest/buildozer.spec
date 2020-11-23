[app]

# (str) Title of your application
title = KivyMD Star Demo

# (str) Package name
package.name = star_demo

# (str) Package domain (needed for android/ios packaging)
package.domain = com.heattheatr

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,md,kv,json

# (str) Application versioning (method 1)
version = 0.1

android.numeric_version = 1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.0.0rc3,https://github.com/kivymd/KivyMD/archive/master.zip,sdl2_ttf==2.0.15

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/assets/kivymd.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for new android toolchain)
android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 19b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /Users/macbookair/.buildozer/android/platform/android-ndk-r19b

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /Users/macbookair/.buildozer/android/platform/android-sdk

# (str) ANT directory (if empty, it will be automatically downloaded.)
android.ant_path = /Users/macbookair/.buildozer/android/platform/apache-ant-1.9.4/apache-ant-1.9.4

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
