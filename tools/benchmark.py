from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json,statistics,tempfile,threading,time,urllib.request
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import make_server
with tempfile.TemporaryDirectory() as tmp:
 s=make_server(Path(tmp)/'load.db','example-teacher-key-for-tests');t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
 def request(i):
  start=time.perf_counter()
  with urllib.request.urlopen(f'http://127.0.0.1:{s.server_port}/health',timeout=10) as r:assert r.status==200
  return (time.perf_counter()-start)*1000
 try:
  with ThreadPoolExecutor(max_workers=4) as pool:values=list(pool.map(request,range(100)))
 finally:s.shutdown();s.server_close();t.join()
 values.sort();r={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'environment':'local loopback; four concurrent clients','requests':100,'errors':0,'p50_ms':statistics.median(values),'p95_ms':values[94],'max_ms':max(values),'target_p95_ms':500}
 Path('reports').mkdir(exist_ok=True);Path('reports/load.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2));assert r['p95_ms']<r['target_p95_ms']
