import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('php7-ubuntu-bionic')


@pytest.mark.parametrize('pkg', ['php7.2-fpm',
                                 'php7.2-common',
                                 'php7.2-cli',
                                 'php7.2-curl',
                                 'php7.2-dev',
                                 'php7.2-gd',
                                 'php7.2-mysql',
                                 'php7.2-mbstring',
                                 'php7.2-intl',
                                 'php7.2-json',
                                 'php7.2-soap',
                                 'php7.2-xml',
                                 'php7.2-xmlrpc',
                                 'php7.2-zip',
                                 'php-imagick',
                                 'php-pear',
                                 'php7.2-bcmath',
                                 ])
def test_default_packages(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ check if service is running
    """
    assert host.service('php7.2-fpm').is_enabled
    assert host.service('php7.2-fpm').is_running
