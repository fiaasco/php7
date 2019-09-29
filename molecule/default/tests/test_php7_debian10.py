import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('php7-debian10')


@pytest.mark.parametrize('pkg', ['php7.3-fpm',
                                 'php7.3-common',
                                 'php7.3-cli',
                                 'php7.3-curl',
                                 'php7.3-dev',
                                 'php7.3-gd',
                                 'php7.3-mysql',
                                 'php7.3-mbstring',
                                 'php7.3-intl',
                                 'php7.3-json',
                                 'php7.3-soap',
                                 'php7.3-xml',
                                 'php7.3-xmlrpc',
                                 'php7.3-zip',
                                 'php-imagick',
                                 'php-pear',
                                 'php7.3-bcmath',
                                 ])
def test_default_packages(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ check if service is running
    """
    assert host.service('php7.3-fpm').is_enabled
    assert host.service('php7.3-fpm').is_running
