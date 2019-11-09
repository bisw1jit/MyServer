# Tool Name :- MyServer
# Author :- LordReaper
# Date :- 9/11/2019
# Powered By :- H1ckPro Software's

import sys
import os
from time import sleep
from system import *
from logo import *

if sys.argv[1]=="-s":
  if os.path.exists(spath+".serv.lock"):
    s=open(spath+".serv.lock","r")
    sr=s.read()
    s.close()
    if system=="ubuntu":
      os.system("sudo python core/server.py "+sr)
    else:
      os.system("python core/server.py "+sr)
  else:
    pass
elif sys.argv[1]=="-h":
  if os.path.exists(spath+".h.lock"):
    s=open(spath+".h.lock","r")
    sr=s.read()
    s.close()
    if system=="ubuntu":
      os.system("sudo python core/host.py "+sr)
    else:
      os.system("python core/host.py "+sr)
  else:
    pass
