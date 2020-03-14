import sys
sys.path.insert(0, "..")


from opcua import Client,ua
from opcua.crypto import security_policies

if __name__ == "__main__":

    # Specify OPC-UA server's URI
    #client = Client("opc.tcp://192.168.2.30:52240")

    # user authentication
    client = Client("opc.tcp://Administrator@192.168.2.30:52240")
    client.set_password('Passw0rd!')

    # Client certification
    pc = getattr(security_policies, 'SecurityPolicy' + "Basic256Sha256")
    # param1: client cert, param2: client secret key, param3: server cert
    client.set_security(pc, "certificate-example.der", "private-key-example.pem", "UaServer.der", ua.MessageSecurityMode.SignAndEncrypt)

    # application_uri must equal to URI in client cert
    client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"

    try:
        client.connect()

        root = client.get_root_node()
        print("root node is: ", root)

        objects = client.get_objects_node()
        print("Objects node is: ", objects)

        print("Children of root are: ", root.get_children())


    finally:
        client.disconnect()
