_MAJOR = "0"
_MINOR = "15"
# On main and in a nightly release the patch should be one ahead of the last
# released build.
_PATCH = "0"
# This is mainly for nightly builds which have the suffix ".dev$DATE". See
# https://semver.org/#is-v123-a-semantic-version for the semantics.
_SUFFIX = ""

V2 = _MINOR
VERSION_SHORT = "{0}.{1}".format(_MAJOR, V2)
VERSION = "{0}.{1}.{2}{3}".format(_MAJOR, V2, _PATCH, _SUFFIX)
