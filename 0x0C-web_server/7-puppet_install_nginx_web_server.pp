# Puppet manifest for a configuration file in the server
include stdlib

# execute 'apt-get update'
exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

# install nginx package
package { 'nginx':
  require => Exec['apt-update'],
  ensure  => installed,
}

# Listning on port 80
exec { 'uvw':
  command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

# hello world HTML file
file { '/var/www/htmlindex.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx']
}

# replacing lines for the redirection
file_line { 'Redirection':
ensure  => present,
path    => '/etc/nginx/sites-available/default',
line    => "        server_name radientrider.tech;\n        location /redirect_me {\n                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n        }"
match   => '/s*server_name _;$',
}

