pkgname = "crag-bootstrap-virtual"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
# armv7 has no Chimera binary repo, so the usual bootstrap:cbuild
# provider (base-cbuild, a host-side meta package) cannot resolve for
# target sysroot installs of *-bootstrap packages (e.g. gnutls-bootstrap
# in curl's dependency chain). Provide the virtual directly instead of
# building the real base-cbuild for the target (which would pull
# llvm/clang into the target sysroot).
provides = ["bootstrap:cbuild=9999-r0"]
pkgdesc = "Bootstrap:cbuild provider for arches without a binary base-cbuild"
license = "custom:meta"
url = "https://github.com/CragLinux/CragLinux"
options = ["empty", "bootstrap"]
