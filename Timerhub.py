from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool
import time

log = core.getLogger()



class TimerHub (object):
  
  def __init__ (self, connection):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection
  
    self.num = 0

 
    def loopre():
        self.loopre1()
        core.callDelayed(10,loopre);
    loopre()


  def loopre1 (self):
    
    msg = of.ofp_flow_mod()
    if self.num == 0:
        log.debug("Hello World0")
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        self.num = 1
    elif self.num == 1:
        log.debug("Hello World1")
        msg.actions = []
        self.num = 0
    self.connection.send(msg)




class hub (object):
  """
  Waits for OpenFlow switches to connect and makes them learning switches.
  """
  def __init__ (self):
    """
    Initialize
    """
    core.openflow.addListeners(self)

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % (event.connection,))
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)
    TimerHub(event.connection)

def launch ():
  """
  Starts an Timerhub
  """

  core.registerNew(hub)
