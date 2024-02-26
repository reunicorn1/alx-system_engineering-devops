# Puppet manifest for a configuration file in the server
include stdlib
$home_dir = $facts['home']

file { "${home_dir}/.ssh":
  ensure => directory,
  mode   => '0700',
}
file { "${home_dir}/.ssh/config":
  ensure  => file,
  mode    => '0600',
  content => "
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => "${home_dir}/.ssh/config",
  line   => 'PasswordAuthentication no',
  }
file_line { 'Declare identity file':
  ensure => presnet,
  path   => "${home_dir}/.ssh/config",
  line   => 'IdentityFile ~/.ssh/school',
}
