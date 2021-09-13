import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('php7-debian11')


@pytest.mark.parametrize('pkg', ['php7.4-fpm',
                                 'php7.4-common',
                                 'php7.4-cli',
                                 'php7.4-curl',
                                 'php7.4-dev',
                                 'php7.4-gd',
                                 'php7.4-mysql',
                                 'php7.4-mbstring',
                                 'php7.4-intl',
                                 'php7.4-json',
                                 'php7.4-soap',
                                 'php7.4-xml',
                                 'php7.4-xmlrpc',
                                 'php7.4-zip',
                                 'php-imagick',
                                 'php-pear',
                                 'php7.4-bcmath',
                                 ])
def test_default_packages(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ check if service is running
    """
    assert host.service('php7.4-fpm').is_enabled
    assert host.service('php7.4-fpm').is_running
