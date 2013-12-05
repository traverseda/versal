#!/usr/bin/env python2.7
import os, sys
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH+'/verse/build/lib/python2.x')
sys.path.append(PROJECT_PATH+"/install/pypy/pypy-2.1-src/rpython/bin/")

#jesus if that isn't overcomplicated. I can't figure out how it's supposed to work.
sys.path.insert(0, os.path.dirname(os.path.dirname(
                       os.path.dirname(os.path.realpath(PROJECT_PATH+"/install/pypy/pypy-2.1-src/rpython/bin/rpython")))))

from rpython.translator.sandbox.sandlib import SimpleIOSandboxedProc
from rpython.translator.sandbox.sandlib import VirtualizedSandboxedProc
from rpython.translator.sandbox.vfs import Dir, RealDir, RealFile
import pypy


import conf
#import vrsent
import time
import verse as vrs

class MySession(vrs.Session):

    def _receive_user_authenticate(self, username, methods):
        """Callback function for user authenticate"""
        print("MY user_authenticate(): ",
              "username: ", username,
              ", methods: ", methods)
        if username=="":
            username = input('username: ')
            self.send_user_authenticate(username, vrs.UA_METHOD_NONE, "")
        else:
            if methods.count(vrs.UA_METHOD_PASSWORD)>=1:
                password = input('password: ')
                self.send_user_authenticate(username, vrs.UA_METHOD_PASSWORD, password)
            else:
                print("Unsuported authenticate method")

    def _receive_connect_accept(self, user_id, avatar_id):
        """Custom callback function for connect accept"""
        # Subscribe to node that is root of node tree
        self.send_node_subscribe(prio=vrs.DEFAULT_PRIORITY, node_id=0, version=0)

    def _receive_node_create(self, node_id, parent_id, user_id, custom_type):
        """Custom callback function that is called, when client received"""
        """command node_create"""
        self.send_node_subscribe(vrs.DEFAULT_PRIORITY, node_id, 0)

def main():
    session = MySession("localhost", "12345", vrs.DGRAM_SEC_DTLS)
    print(sys.path)
    while(True):
        session.callback_update()
        time.sleep(1)

if __name__ == '__main__':
    main()

