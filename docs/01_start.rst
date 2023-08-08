===============
Getting Started
===============


Installation
============

::
    
    pip install findmyorder


Example
=======

The following example illustrate how to use the module


.. literalinclude:: ../examples/example.py


PyScript
========

.. raw:: html

   <br>

   <html>
   <head>
      <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
      <script defer src="https://pyscript.net/latest/pyscript.js"></script>
   </head>
   <body>
   <py-config>
      packages = ["findmyorder"]
    </py-config>
    <py-script>
      from findmyorder import FindMyOrder

        fmo = FindMyOrder()
        print(fmo)
        msg_order = "buy btc"
        print(await fmo.search(msg_order))
        (await fmo.identify_order(msg_order))

    </py-script>
   </body>
   </html>