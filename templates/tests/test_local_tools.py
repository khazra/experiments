import hashlib,json,os,pathlib,subprocess,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class LocalTools(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.base=pathlib.Path(self.tmp.name)
 def run_tool(self,action,path):return subprocess.run([sys.executable,str(ROOT/'local-tools.py'),action,str(path)],capture_output=True,text=True)
 def test_inventory_accounts_for_dotfiles_and_escaped_names(self):
  for name in ['.hidden','BUILD.json','MANIFEST.sha256','line\nbreak.txt']:(self.base/name).write_bytes(b'fixture')
  p=self.run_tool('inventory',self.base);self.assertEqual(p.returncode,0,p.stderr)
  rows=[json.loads(l) for l in p.stdout.splitlines()];self.assertEqual(len(rows),4)
  self.assertEqual({r['sha256'] for r in rows},{hashlib.sha256(b'fixture').hexdigest()})
  self.assertIn('line\nbreak.txt',{r['path'] for r in rows})
 def test_safe_scan(self):
  (self.base/'ok').write_text('ordinary public narrative');self.assertEqual(self.run_tool('scan',self.base).returncode,0)
 def test_multiline_secret_array_is_rejected_without_content(self):
  s='{'+json.dumps('secretKey')+': [\n'+','.join(['42']*32)+'\n]}'
  (self.base/'test').write_text(s);p=self.run_tool('scan',self.base)
  self.assertEqual(p.returncode,1);self.assertIn('secret-key-array',p.stderr);self.assertNotIn(',42',p.stderr)
 def test_api_token_is_rejected_without_value(self):
  secret='sk-'+('a'*32);(self.base/'test').write_text(secret);p=self.run_tool('scan',self.base)
  self.assertEqual(p.returncode,1);self.assertNotIn(secret,p.stdout+p.stderr)
 def test_nested_git_directory_is_not_exempt(self):
  p=self.base/'nested'/'.git';p.mkdir(parents=True);(p/'token').write_text('sk-'+('a'*32))
  self.assertEqual(self.run_tool('scan',self.base).returncode,1)
 def test_file_symlink_rejected(self):
  (self.base/'a').write_text('safe');(self.base/'b').symlink_to(self.base/'a')
  self.assertEqual(self.run_tool('inventory',self.base).returncode,2);self.assertEqual(self.run_tool('scan',self.base).returncode,2)
 def test_root_symlink_rejected(self):
  target=self.base/'dir';target.mkdir();link=self.base/'link';link.symlink_to(target,target_is_directory=True)
  self.assertEqual(self.run_tool('scan',link).returncode,2)
 def test_unreadable_and_absent_fail_closed(self):
  f=self.base/'file';f.write_text('fixture');f.chmod(0);self.addCleanup(lambda:f.chmod(0o600))
  self.assertEqual(self.run_tool('scan',self.base).returncode,2)
  self.assertEqual(self.run_tool('scan',self.base/'absent').returncode,2)
 def test_status_does_not_create_directory(self):
  p=self.base/'state';r=self.run_tool('status',p);self.assertEqual(r.stdout.strip(),'unmarked');self.assertFalse(p.exists())
 def test_marker_is_idempotent_and_does_not_claim_worker_stop(self):
  p=self.base/'state'
  for _ in range(2):self.assertEqual(self.run_tool('mark-paused',p).stdout.strip(),'paused-marker')
  self.assertEqual(self.run_tool('status',p).stdout.strip(),'paused-marker')
 def test_start_is_not_supported(self):
  p=self.base/'state';self.assertNotEqual(self.run_tool('start',p).returncode,0);self.assertFalse(p.exists())
 def test_pause_marker_symlink_rejected(self):
  target=self.base/'target';target.write_text('unchanged');(self.base/'PAUSED').symlink_to(target)
  self.assertEqual(self.run_tool('mark-paused',self.base).returncode,2);self.assertEqual(target.read_text(),'unchanged')
 def test_renderer_only_prints_configuration(self):
  marker=self.base/'never-created';cmd=[sys.executable,str(ROOT/'deploy/render-service.py'),'--program',str(marker),'--workdir',str(self.base),'--max-seconds','60']
  p=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(p.returncode,0,p.stderr);self.assertIn('RuntimeMaxSec=60',p.stdout);self.assertIn('KillMode=control-group',p.stdout);self.assertFalse(marker.exists())
  cmd[-1]='0';self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)
 def test_renderer_rejects_directive_injection(self):
  p=subprocess.run([sys.executable,str(ROOT/'deploy/render-service.py'),'--program','/bin/true\nRestart=always','--workdir','/tmp','--max-seconds','60'],capture_output=True)
  self.assertNotEqual(p.returncode,0)
if __name__=='__main__':unittest.main(verbosity=2)
