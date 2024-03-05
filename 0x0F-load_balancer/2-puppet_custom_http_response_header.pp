# Puppet manifest for a configuration file in the server

# replacing lines for the redirection
exec {'configure':
  provider => shell,
  command  => 'sudo apt-get update -y ; sudo apt-get install nginx -y ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "s#server_name _;#server_name radientrider.tech;\n        location /redirect_me {\n                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n        }#" /etc/nginx/sites-available/default ; sudo service nginx restart ; hostname=$(hostname) ; string="\n\tadd_header X-Served-By \"$hostname\";" ; sudo sed -i "/server_name _;/ a\\
$string" /etc/nginx/sites-available/default ; sudo service nginx restart',
}
