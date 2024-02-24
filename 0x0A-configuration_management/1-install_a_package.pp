#!/usr/bin//pup
# This Puppet installs flast from pip3
package {'flask':
	ensure => '2.1.0',
	provider => 'pip3'
}
