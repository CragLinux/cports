pkgname = "dhcpcd"
pkgver = "10.5.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libexecdir=/usr/lib",
    "--sysconfdir=/etc",
    "--rundir=/run/dhcpcd",
    "--dbdir=/var/lib/dhcpcd",
    "--privsepuser=_dhcpcd",
    "--enable-privsep",
]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera", "udev-devel", "linux-headers"]
depends = ["resolvconf"]
pkgdesc = "RFC2131 compliant DHCP client"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/dhcpcd"
source = f"https://github.com/NetworkConfiguration/dhcpcd/releases/download/v{pkgver}/dhcpcd-{pkgver}.tar.xz"
sha256 = "1fac7f914161c09e379c696c8c599f26b116f00fc695f999ca8365d144b61f8f"
# FIXME vis for usr/lib/dhcpcd/dev/udev.so
hardening = ["!vis", "!cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "dhcpcd")
