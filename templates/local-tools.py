#!/usr/bin/env python3
"""Offline inventory, privacy scan and pause marker. No network or worker launch."""
import argparse, hashlib, json, os, pathlib, re, stat, sys

def tree(root):
    root=pathlib.Path(root)
    if root.is_symlink() or not root.is_dir(): raise ValueError('input must be a real local directory')
    for parent, dirs, files in os.walk(root, followlinks=False, onerror=lambda e: (_ for _ in ()).throw(e)):
        dirs.sort(); files.sort()
        if pathlib.Path(parent)==root and '.git' in dirs: dirs.remove('.git')
        for name in dirs+files:
            p=pathlib.Path(parent)/name; mode=p.lstat().st_mode
            if stat.S_ISLNK(mode): raise ValueError('symlinks are not supported')
            if not (stat.S_ISDIR(mode) or stat.S_ISREG(mode)): raise ValueError('special files are not supported')
            if stat.S_ISREG(mode):
                if mode & 0o444 == 0: raise ValueError('unreadable file')
                yield p, p.relative_to(root).as_posix()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['inventory','scan','status','mark-paused'])
    parser.add_argument('directory'); args=parser.parse_args(); root=pathlib.Path(args.directory)
    if args.action in ['status','mark-paused']:
        if root.is_symlink(): raise ValueError('state directory must not be a symlink')
        marker=root/'PAUSED'
        if marker.is_symlink(): raise ValueError('pause marker must not be a symlink')
        if args.action=='mark-paused':
            root.mkdir(parents=True,exist_ok=True)
            fd=os.open(marker,os.O_CREAT|os.O_WRONLY|os.O_EXCL,0o600) if not marker.exists() else None
            if fd is not None:os.close(fd)
        print('paused-marker' if marker.is_file() else 'unmarked');return 0
    records=list(tree(root)) # validate whole tree before emitting any partial inventory
    if args.action=='inventory':
        for p,rel in records:
            data=p.read_bytes();print(json.dumps({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()},sort_keys=True))
        return 0
    spec=json.loads((pathlib.Path(__file__).parent/'privacy-patterns.json').read_text())
    patterns=[(p['id'],re.compile(p['regex'],re.I if 'i' in p['flags'] else 0)) for p in spec['patterns']]
    hits=[]
    for p,rel in records:
        s=p.read_bytes().decode('utf-8',errors='replace')
        for name,pattern in patterns:
            if pattern.search(s):hits.append({'file':rel,'detector':name})
    # Never print matched text. This is a detector check, not complete anonymization.
    for hit in hits:print(json.dumps(hit,sort_keys=True),file=sys.stderr)
    return 1 if hits else 0

if __name__=='__main__':
    try:sys.exit(main())
    except (OSError,ValueError,UnicodeError,json.JSONDecodeError) as e:
        print('Local check failed: '+type(e).__name__+'; no clean result issued.',file=sys.stderr);sys.exit(2)
