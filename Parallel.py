# Parallel Python in IPython
ipcluster local -n 6
from IPython.kernel import client
mec=client.MultiEngineClient()
mec.get_ids()

ipengine

mec.kill(controller=True)