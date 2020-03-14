import sys
import time

sys.path.insert(0, "..")

from opcua import ua, Server
from opcua.crypto import security_policies

import urllib.request
import json

def get_data():
    url = 'http://127.0.0.1:5000/preds?data=status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        #body = res.read()
        body = json.load(res)
    print("status from AI server:"+str(body))
    return str(body)

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # load server certificate and private key. This enables endpoints
    # with signing and encryption.
    pc = getattr(security_policies, 'SecurityPolicy' + "Basic256Sha256")

    server.load_certificate("certificate-example.der")
    server.load_private_key("private-key-example.pem")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()
    try:
        while True:
            # Get desireble status from AI server
            #status = get_data()
            status =1
            myvar.set_value(status)
            time.sleep(10)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()

