# Redo the task #0 but by using Puppet

exec {'apt-get-update':
  command => '/usr/bin/apt-get update'
}

package {'apache2.2-common':
  ensure  => 'absent',
  require => Exec['apt-get-update']
}

package { 'nginx':
  ensure  => 'installed',
  require => Package['apache2.2-common']
}

service {'nginx':
  ensure  =>  'running',
  require => file_line['adding a location'],
}

file { '/data/web_static/releases/test/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require =>  Package['nginx']
}

file { '/data/web_static/releases/test/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require =>  Package['nginx']
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'This is my sample content',
  require =>  Package['nginx']
}

file_line { 'adding a location':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => '\n\n\tlocation \/hbnb_static\/ \{\
\n\t\talias \/data\/web_static\/current\/\;\
\n\t\tautoindex off\;\
\n\t\}',
  before  => '^\tlocation+',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
