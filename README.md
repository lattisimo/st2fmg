# FortiManager Integration Pack
This pack will allow manipulation of a FortiManager
 - This is very early concept and changing contstantly at this stage

The underlying module used is pyFMG - https://github.com/p4r4n0y1ng/pyfmg

The FNDN API refference - https://fndn.fortinet.net/ - Ask your Fortinet Rep

## CONFIG
- fortimanager: default fmg ip/host
- username: rpc user name
- password: rpc user password
- conn_debug: enable pyFMG debug outpit
- conn_ssl: use https
- conn_warn: use ssl cert warning
- conn_verify: require valid ssl cert
- conn_timeout: requests timeout

## DVMDB
- ADOM Get
- Device Get - Only tested action so far
  - HA Slave
  - VDOM
- Folder Get
- Group Get


free_form

track_task