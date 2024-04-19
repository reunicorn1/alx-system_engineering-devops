# Puppet manifest to modify the user limit
exec{ 'modify limit':
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 65536/" /etc/security/limits.conf && sed -i "s/holberton soft nofile 4/holberton soft nofile 65536/" /etc/security/limits.conf',
}
