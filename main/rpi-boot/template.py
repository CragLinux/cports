pkgname = "rpi-boot"
pkgver = "1.20260513"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "69905ac1b4bce0d6e5b57d076b8e7dd6e086fdbf"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "aa8c40bc52f6a155cfdb8eaecfe5511c774d6ab74d771d61c47d27ee3a8900fa"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
