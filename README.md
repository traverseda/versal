versal
======

Versal will eventually be a secure, sandboxed, crossplatform, excecution enviroment for python code. It has a focus on multi-user game worlds and collaborative CAD -- bringing a lot of different cad tools together.

To accomplish this we're going to be using a lot of tools.

 * **Pypy** - A JIT compiler for python. We're using it to provide a blazing fast sandboxed python interpreter.

 * **RpyC** - Object proxying over pipe streams. It lets us access python libraries outside of our very limited sandbox. We're using it to manage things like network access. It also lets us transparently use libraries/extensions that don't work in pypy. Libraries that do run under pypy and that don't need any system priveledges should be made available as normal modules to our sandbox.

 * **verse** - Verse is a network protocol for real-time sharing of 3D data. It is intended mostly for graphical applications of colaborative virtual reality. It's provided as a library to our execution enviroment using RpyC. This *would* be just another bare-metal library, except we're working on integrating support for the verse protocol directly into the launcher. For example, typing verse://spacebattle.game.com into your launcher should download the appropriate code from that server and run.


Right now it's just a set of scripts for getting pypy and verse compiled though.
