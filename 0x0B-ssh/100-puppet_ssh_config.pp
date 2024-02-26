file { '~/.ssh/config':
  ensure  => file,
  content => "Host *\n    IdentityFile ~/.ssh/school\n     PasswordAuthentication no",
}
