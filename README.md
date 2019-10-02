[![Build Status](https://travis-ci.org/fiaasco/php7.svg?branch=master)](https://travis-ci.org/fiaasco/php7)

# Ansible Role: php7

This is an Ansible role to install php7-fpm on Debian and Ubuntu.
It will put the base configuration with the most important configurables and a standard pool. Apache mod php is removed by the role, as it requires the inefficient prefork mpm.

Per default the role installs the distribution default php version. On Debian, it can also configure the Sury repo to install newer php7 versions than the default available. It's possible to run multiple PHP versions next to each other (example configuration in the default molecule scenario). Be aware that this will pull some dependencies and not every version combination might work.

The role will remove mod-php when it's installed and enable mod proxy fcgi in Apache (set to false to disable php7\_apache2\_enable\_proxy\_fcgi).

Not included in the role:
* Creation of other fpm pools
* Creation of vhosts with php-fpm enabled
In our use case, this is done with the fiaasco.createresources role.


## Requirements

None.


## Role Variables


Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies

None.


## Examples

Include the role in your playbook:

```
    - hosts: servers
      roles:
         - role: fiaasco.php7
```

## Tags

No tags available.

## License

MIT

## Further Reading



## Author Information

Luc Stroobant
