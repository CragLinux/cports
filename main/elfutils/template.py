pkgname = "elfutils"
pkgver = "0.193"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-nls",
    "--disable-werror",
    "--enable-deterministic-archives",
    "--with-zstd",
    "--program-prefix=eu-",
]
# autoreconf generates junk configure
configure_gen = []
hostmakedepends = [
    "bison",
    "flex",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "bzip2-devel",
    "chimerautils-devel",
    "json-c-devel",
    "libarchive-devel",
    "linux-headers",
    "musl-bsd-headers",
    "musl-obstack-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
# transitional
provides = [self.with_pkgver("elftoolchain")]
pkgdesc = "Utilities and libraries to handle ELF files and DWARF data"
license = "GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later)"
url = "https://sourceware.org/elfutils"
source = (
    f"https://sourceware.org/elfutils/ftp/{pkgver}/elfutils-{pkgver}.tar.bz2"
)
sha256 = "7857f44b624f4d8d421df851aaae7b1402cfe6bcdd2d8049f15fc07d3dde7635"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-Wno-unaligned-access"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}

# debuginfod's dependency closure (libmicrohttpd -> gnutls -> unbound ->
# protobuf-c -> protobuf) cannot be cross-built for a self-hosted 32-bit
# arm repo: main/protobuf is marked broken for cross builds. Build
# elfutils without debuginfod there; everything else (libelf/libdw/tools)
# is unaffected.
_have_debuginfod = self.profile().arch not in ("armv7", "armhf")

if _have_debuginfod:
    configure_args += ["--enable-debuginfod", "--enable-libdebuginfod"]
    makedepends += ["curl-devel", "libmicrohttpd-devel"]
else:
    configure_args += ["--disable-debuginfod", "--disable-libdebuginfod"]

if self.profile().arch == "x86_64":
    makedepends += ["sysprof-capture"]
    configure_args += ["--enable-stacktrace"]


def post_build(self):
    self.ln_s("eustack", "build/src/stack")


def post_install(self):
    self.rename("usr/bin/eu-eustack", "eu-stack")


@subpackage("elfutils-debuginfod", _have_debuginfod)
def _(self):
    self.subdesc = "debuginfod"
    # transitional
    self.provides = [self.with_pkgver("debuginfod")]

    return [
        "usr/bin/debuginfod*",
        "usr/share/man/man[18]/debuginfod*",
    ]


@subpackage("elfutils-debuginfod-libs", _have_debuginfod)
def _(self):
    self.subdesc = "debuginfod library"
    # transitional
    self.provides = [self.with_pkgver("debuginfod-libs")]
    self.options = ["etcfiles"]

    return [
        "etc/profile.d",
        "usr/lib/libdebuginfod.so.*",
        "usr/lib/libdebuginfod-*.so",
    ]


@subpackage("elfutils-libs")
def _(self):
    # since the resolved (after symlinks) filename of the .so is without
    # a suffix, the automatic virtual version would be 0, which would
    # prevent upgrades from elftoolchain (which had 1)
    pv = pkgver[2:]
    self.provides = [
        self.with_pkgver("libelf"),  # transitional
        f"so:libasm.so.1={pv}",  # allow for upgrade
        f"so:libdw.so.1={pv}",
        f"so:libelf.so.1={pv}",
    ]

    return self.default_libs(extra=[f"usr/lib/*-{pkgver}.so"])


@subpackage("elfutils-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("elftoolchain-devel")]

    return self.default_devel()
