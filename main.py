import os, sys
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH+'/verse-entities/')
sys.path.append(PROJECT_PATH+'/verse/build/lib/python2.x')


import vrsent
import time

def main():
    """
    Function with main never ending verse loop
    """
    session = vrsent.VerseSession()
    session.debug_print = True

    node = vrsent.VerseNode(session)
    tg = vrsent.VerseTagGroup(node)
    tag = vrsent.VerseTag(tg)
    tag.value = (10,)

    while(session.state != 'DISCONNECTED'):
        session.callback_update()
        time.sleep(1.0/session.fps)

if __name__ == '__main__':
    main()


