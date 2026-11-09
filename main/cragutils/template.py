pkgname = "cragutils"
pkgver = "15.1.2"
pkgrel = 1
# Crag's hardened userland fork (cragutils) — since 2026-11-08 this
# package builds CragLinux/cragutils, NOT upstream chimera-linux/chimerautils.
# pkgver tracks the upstream chimerautils base the fork content matches
# (the daily userland watch imports upstream changes into the fork);
# bump pkgrel on every fork content update (i.e. every _commit change).
_commit = "92d7bb8030834fbe11489c9a2a2a959fb8e983ef"
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib/cragutils",
    "-Dchimera_realpath=enabled",
]
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel",
    "bzip2-devel",
    "libedit-devel",
    "libxo-devel",
    "musl-bsd-headers",
    "ncurses-devel",
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = ["base-files", "debianutils"]
# compat
provides = [
    self.with_pkgver("musl-fts"),
    self.with_pkgver("musl-rpmatch"),
]
# rename takeover (was main/chimerautils)
replaces = ["chimerautils"]
pkgdesc = "Crag Linux userland, hardened fork of chimerautils"
license = "BSD-2-Clause"
url = "https://github.com/CragLinux/cragutils"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "eb379f7df80ce0ba39b9e16fa391bdf6592bb6f938a251ac4d58952feded602d"
hardening = ["vis", "cfi"]
# check disabled: the cragutils test suite runs in cragutils CI (meson
# test + fuzz + differential), not inside the cbuild sandbox
options = ["bootstrap", "!check"]

if self.stage > 0:
    makedepends += ["linux-headers", "zstd-devel"]
    configure_args += ["-Dtiny=enabled"]
    # don't bother in stage 0
    depends += [
        "cmd:systemd-tmpfiles!sd-tools",
        "cmd:systemd-sysusers!sd-tools",
    ]
else:
    makedepends += ["libxo-devel-static"]
    configure_args += ["-Dzstd=disabled"]


def init_configure(self):
    if self.stage > 0:
        return

    spath = str(self.bldroot_path / "usr/lib")

    # since meson translates all `-lfoo` into absolute paths to libraries,
    # and pkg-config's libdir is set to /usr/lib in this case, fool it
    # into giving out the correct paths to make meson happy
    self.env["PKG_CONFIG_LIBCRYPTO_LIBDIR"] = spath
    self.env["PKG_CONFIG_LIBEDIT_LIBDIR"] = spath


def post_install(self):
    # license
    self.install_license("LICENSE")
    # less
    self.uninstall("usr/bin/zless")
    self.uninstall("usr/share/man/man1/zless.1")
    # base shell
    self.install_shell("/usr/bin/sh")
    # tiny tools
    tdest = "usr/lib/cragutils/tiny"
    self.install_dir(tdest)
    for f in (self.destdir / "usr/bin").glob("*.tiny"):
        self.mv(f, self.destdir / tdest / f.stem)
    # etc files, handled with tmpfiles
    self.install_dir("usr/share/cragutils")
    self.install_tmpfiles(self.files_path / "cragutils.conf")
    self.install_tmpfiles(
        self.files_path / "cragutils-extra.conf", name="cragutils-extra"
    )
    for f in (self.destdir / "etc").iterdir():
        self.mv(f, self.destdir / "usr/share/cragutils")


@subpackage("cragutils-devel-man")
def _(self):
    # former conflicts with fts/rpmatch manpages
    self.replaces = ["man-pages-devel<6.9.1-r3", "chimerautils-devel-man"]
    return ["usr/share/man/man3"]


@subpackage("cragutils-devel")
def _(self):
    # compat
    self.provides = [
        self.with_pkgver("musl-fts-devel"),
        self.with_pkgver("musl-rpmatch-devel"),
    ]
    self.replaces = ["chimerautils-devel"]
    # explicitly non-lto
    self.options = ["ltostrip", "!splitstatic"]
    return self.default_devel()


@subpackage("cragutils-extra")
def _(self):
    self.subdesc = "additional tools"
    self.depends = [self.parent]
    self.replaces = ["chimerautils-extra"]

    return [
        "cmd:calendar",
        "cmd:cal",
        "cmd:compress",
        "cmd:cu",
        "cmd:ee",
        "cmd:ex",
        "cmd:fetch",
        "cmd:gencat",
        "cmd:indent",
        "cmd:locate*",
        "cmd:m4",
        "cmd:nc",
        "cmd:ncal",
        "cmd:nex",
        "cmd:nvi",
        "cmd:nview",
        "cmd:patch",
        "cmd:telnet",
        "cmd:tip",
        "cmd:uncompress",
        "cmd:vi",
        "cmd:view",
        "man:remote.5",
        "man:locate.updatedb.8",
        "man:updatedb.8",
        "usr/lib/cragutils/locate.*",
        "usr/lib/tmpfiles.d/cragutils-extra.conf",
        "usr/share/cragutils/locate.rc",
        "usr/share/vi",
    ]
