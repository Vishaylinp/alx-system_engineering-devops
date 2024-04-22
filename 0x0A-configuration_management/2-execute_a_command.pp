# Execute bash
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
