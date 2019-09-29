import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('php7-debian9')


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
                                 ])
def test_72_packages(host, pkg):
    """ check if packages are installed
    """
    assert host.package(pkg).is_installed


def test_service(host):
    """ check if service is running
    """
    assert host.service('php7.0-fpm').is_enabled
    assert host.service('php7.0-fpm').is_running
    assert host.service('php7.2-fpm').is_enabled
    assert host.service('php7.2-fpm').is_running
