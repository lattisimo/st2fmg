# FortiManager Integration Pack
This pack will allow manipulation of a FortiManager
 - This is very early concept and changing contstantly at this stage

The underlying module used is pyFMG - https://github.com/p4r4n0y1ng/pyfmg

The FNDN API refference - https://fndn.fortinet.net/ - Ask your Fortinet Rep

## CONFIG
- fortimanager: default fmg ip/host
- username: rpc user name
- password: rpc user password
- conn_ssl: use https
- conn_warn: use ssl cert warning
- conn_verify: require valid ssl cert
- conn_timeout: requests timeout

## get
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## add
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## delete
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## set
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## exec
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## free_form
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- conn_debug: enable pyFMG debug outpit
## track_task
- fortimanager: override fmg ip/host
- username: override rpc user name
- password: override rpc user password
- taskid: task id to be tracked
- conn_debug: enable pyFMG debug outpit