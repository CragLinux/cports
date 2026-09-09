pkgname = "dinit"
pkgver = "0.22.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--disable-strip",
    "--enable-shutdown",
    "--platform=Linux",
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/v{pkgver}.tar.gz"
sha256 = "8907d4f668259c4f66d9d2c7cbbb55d455c28dc433596ab29005d589cb572e1e"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
