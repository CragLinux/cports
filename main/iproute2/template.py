pkgname = "iproute2"
pkgver = "7.3.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--color", "auto"]
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = [
    "bison",
    "flex",
    "linux-headers",
    "perl",
    "pkgconf",
]
makedepends = [
    "elfutils-devel",
    "flex-devel-static",
    "iptables-devel",
    "libcap-devel",
    "libmnl-devel",
    "linux-headers",
]
pkgdesc = "IP routing utilities"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/iproute2/iproute2-{pkgver}.tar.xz"
sha256 = "5c1789d290bba048a6135ed1ab81b0402dd0fb528d1f1421765c42b1fc3d6289"
# causes some part of the build to silently break which drops support for various features
hardening = ["!vis"]


def init_configure(self):
    # upstream's hardcoded CC=clang is native-only; take the profile's
    # compiler so cross builds use the target triplet
    self.configure_env["CC"] = self.get_tool("CC")


def init_build(self):
    with self.use_profile("host"):
        self.make_build_args += [f"HOSTCC={self.get_tool('CC')}"]


def check(self):
    self.make.invoke(None, ["-C", "testsuite"])


def post_install(self):
    # nothing includes the one header here
    self.uninstall("usr/include")
    # 7.2.0 no longer ships man3 pages
