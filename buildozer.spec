[app]
title = Quantum Armour V20
package.name = quantumarmourv20
package.domain = com.quantum.v20

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 20.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
archs = arm64-v8a, armeabi-v7a
