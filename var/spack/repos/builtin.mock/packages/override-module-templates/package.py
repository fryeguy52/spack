# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class OverrideModuleTemplates(Package):
    homepage = "http://www.fake-spack-example.org"
    url = "http://www.fake-spack-example.org/downloads/fake-1.0.tar.gz"

    version("1.0", md5="0123456789abcdef0123456789abcdef")

    tcl_template = "override.txt"
    lmod_template = "override.txt"
