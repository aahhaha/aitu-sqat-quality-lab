import threading
import pytest
from app import make_server
@pytest.fixture
def live_server(tmp_path):
    s=make_server(tmp_path/'browser.db','example-teacher-key-for-tests');t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
    yield f'http://127.0.0.1:{s.server_port}'
    s.shutdown();s.server_close();t.join()
