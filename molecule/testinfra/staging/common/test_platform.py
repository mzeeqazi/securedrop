# We expect Ubuntu, either Trusty or Xenial, the two LTSes
# currently targeted for support.
SUPPORTED_CODENAMES = ('trusty', 'xenial')
SUPPORTED_RELEASES = ('14.04', '16.04')


def test_ansible_version(host):
    """
    Check that a supported version of Ansible is being used.

    The project has long used the Ansible 1.x series, ans now
    requires the 2.x series starting with the 0.4 release. Ensure
    installation is not being performed with an outdated ansible version.
    """
    localhost = host.get_host("local://")
    c = localhost.check_output("ansible --version")
    assert c.startswith("ansible 2.")


def test_platform(host):
    """
    SecureDrop requires Ubuntu Trusty 14.04 LTS. The shelf life
    of that release means we'll need to migrate to Xenial LTS
    at some point; until then, require hosts to be running
    Ubuntu.
    """
    assert host.system_info.type == "linux"
    assert host.system_info.distribution == "ubuntu"
    assert host.system_info.codename in SUPPORTED_CODENAMES
    assert host.system_info.release in SUPPORTED_RELEASES
