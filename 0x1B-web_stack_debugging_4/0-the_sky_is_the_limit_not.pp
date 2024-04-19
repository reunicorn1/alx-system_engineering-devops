# Puppet manifest to modify the fd limit
exec{ 'modify limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 70000\"/" /etc/default/nginx && service nginx restart',
}
