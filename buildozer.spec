[app]
title = Quantum Armour V20
package.name = quantumarmourv20
package.domain = com.quantum.v20
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 20.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license_agreement = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET
