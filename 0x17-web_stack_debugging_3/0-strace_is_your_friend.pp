# Puppet manifest to fix typos
exec{ 'Fix file':
  provider => shell,
  command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
