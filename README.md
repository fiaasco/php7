# Ansible Role: php7

![Debian](https://github.com/fiaasco/php7/actions/workflows/debian.yml/badge.svg)
![Ubuntu](https://github.com/fiaasco/php7/actions/workflows/ubuntu.yml/badge.svg)

This is an Ansible role to install php7-fpm on Debian and Ubuntu.
It will put the base configuration with the most important configurables and a standard pool.

Per default the role installs the distribution default php version. On Debian, it can also configure the Sury repo to install newer php7 versions than the default available. It's possible to run multiple PHP versions next to each other (example configuration in the default molecule scenario). Be aware that this will pull some dependencies and not every version combination might work.

Use the fiaasco.apache2\_php\_config role to configure Apache for PHP FPM usage.

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
