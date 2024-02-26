# Puppet manifest for a configuration file
include stdlib
$home_dir = $facts['home']

file { "${home_dir}/.ssh":
  ensure  => directory,
  mode    => '0700',
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
  path   => "${home_dir}/.ssh/config",
  line   => 'PasswordAuthentication no',
  ensure => present,
}
file_line { 'Declare identity file':
  path   => "${home_dir}/.ssh/config",
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}
