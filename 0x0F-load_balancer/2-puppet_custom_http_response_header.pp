# Puppet manifest for a configuration file in the server
# execute 'apt-get update'
exec { 'apt-update':
	command => '/usr/bin/apt-get update'
}

# install nginx package
package { 'nginx':
	require => Exec['apt-update'],
	ensure  => installed,
}

# hello world HTML file
file { '/var/www/htmlindex.html':
	ensure  => file,
	content => 'Hello World!',
	require => Package['nginx']
}

# replacing lines for the redirection
exec { 'Redirection':
	provider => shell,
	command  => 'sudo sed -i "s#server_name _;#server_name _;\n        location /redirect_me {\n                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n        }#" /etc/nginx/sites-available/default ; sudo service nginx restart',
}

# custom header creation 
exec { 'custom_header':
	provider => shell,
	command  => 'hostname=$(hostname) ; string="\tadd_header X-Served-By \"$hostname\";" ; sudo sed -i "/server_name _;/ a\\ $string\n" /etc/nginx/sites-available/default ; sudo service nginx restart',
}
