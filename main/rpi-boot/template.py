pkgname = "rpi-boot"
pkgver = "1.20260907"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "b76effded7afe5ed92070ff169e0109a8487fb82"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "818ba1d8b0c6030352049315b7145a44438da9f121884d08151c5ab7ce5a5017"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
