 # This Puppet kills a process named killmeow
 exec { 'kill_killmenow_process':
   command     => '/usr/bin/pkill killmenow',
   refreshonly => true,
 }
