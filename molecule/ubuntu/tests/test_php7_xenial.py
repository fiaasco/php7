import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('php7-ubuntu-xenial')


@pytest.mark.parametrize('pkg', ['php7.0-fpm',
                                 'php7.0-common',
                                 'php7.0-cli',
                                 'php7.0-curl',
                                 'php7.0-dev',
                                 'php7.0-gd',
                                 'php7.0-mysql',
                                 'php7.0-mbstring',
                                 'php7.0-intl',
                                 'php7.0-json',
                                 'php7.0-soap',
                                 'php7.0-xml',
                                 'php7.0-xmlrpc',
                                 'php7.0-zip',
                                 'php-imagick',
                                 'php-pear',
                                 ])
def test_default_packages(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ check if service is running
    """
    assert host.service('php7.0-fpm').is_enabled
    assert host.service('php7.0-fpm').is_running
