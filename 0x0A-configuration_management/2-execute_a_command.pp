# This Puppet kills a process named killmeow
exec { 'pkill':
	command => 'pkill kkillmenow'
	provider => 'shell'
}
