#!/usr/bin/env python3
"""Render an inert Linux user-service example to stdout. Does not install or start it."""
import argparse,pathlib,re
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--program',required=True);p.add_argument('--workdir',required=True)
p.add_argument('--max-seconds',type=int,required=True);a=p.parse_args()
for v in [a.program,a.workdir]:
 if not pathlib.PurePosixPath(v).is_absolute() or not re.fullmatch(r'/[A-Za-z0-9_./ -]+',v):p.error('use a plain absolute path without control characters or substitutions')
if not 1<=a.max_seconds<=432000:p.error('max-seconds must be between 1 and 432000')
print(f'''[Unit]
Description=Bounded experiment worker template

[Service]
Type=simple
WorkingDirectory="{a.workdir}"
ExecStart="{a.program}"
Restart=no
RuntimeMaxSec={a.max_seconds}
KillMode=control-group
TimeoutStopSec=30
UMask=0077
NoNewPrivileges=yes

[Install]
WantedBy=default.target
''')
