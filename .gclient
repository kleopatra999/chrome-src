solutions = [
  { "name"        : "chrome-src",
    "url"         : "https://github.com/rkchrome/chrome-src.git",
    "deps_file"   : ".DEPS.git",
    "managed"     : True,
    "custom_deps" : {
      "src/content/test/data/layout_tests/LayoutTests": None,
      "src/chrome/tools/test/reference_build/chrome_win": None,
      "src/chrome_frame/tools/test/reference_build/chrome_win": None,
      "src/chrome/tools/test/reference_build/chrome_linux": None,
      "src/chrome/tools/test/reference_build/chrome_mac": None,
      "src/third_party/hunspell_dictionaries": None,
    },
    "safesync_url": "",
  },
]
cache_dir = None
