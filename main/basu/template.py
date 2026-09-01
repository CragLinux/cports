# Crag Linux addition (not in cports upstream; docs/06 §3, AD-016): basu
# is the systemd-free sd-bus extraction — the Crag system daemon's D-Bus
# client library, wrapped in exactly one Zig module. libcap/audit stay
# off: musl target, and the daemon runs unprivileged by design
# (docs/02 §7). Candidate for upstreaming to Chimera cports (standard
# package, no Crag-specific content).
pkgname = "basu"
pkgver = "0.2.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dlibcap=disabled",
    "-Daudit=disabled",
]
hostmakedepends = ["gperf", "meson", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Sd-bus library extracted from systemd, without systemd"
license = "LGPL-2.1-or-later"
url = "https://git.sr.ht/~emersion/basu"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "43b327073d1ac7bc6cbc0d3dfff729348fc970dfff0551ad40e366332e990204"
# !lto: cbuild's LTO emits LLVM-bitcode archive members into libbasu.a
# (verified: readelf reports "LLVM bitcode file"), which Zig's linker
# rejects ("not an ELF file") when statically linking the Crag system
# daemon. Plain ELF objects cost nothing measurable for a library this
# small.
options = ["!lto"]


@subpackage("basu-devel")
def _(self):
    return self.default_devel()
