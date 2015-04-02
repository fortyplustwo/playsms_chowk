playsms_chowk
=============

This is a quick-dirty version of chowk(https://github.com/fortyplustwo/chowk) for playSMS

It acts as an interface between playSMS and any number of Kannel servers that you have by
passing messages to and fro in a format that both will understand.

Who and how does chowk help ?
----------------
If you have multiple Kannel servers and need to pass on each message originating from Kannel
to the "right" kannel server based on the number series of the recipient (ie. the network operator),
chowk helps you.

Please note that chowk only helps in case of 1-to-N connections of playSMS and Kannel servers and *not* vice versa.

Currently it:
-------------

* Forward a message from any Kannel server to the playSMS instance.

In future it will:
------------------
* Takes a message from playSMS and sends it to the Kannel server b
* Send a confirmation report to playSMS, of the message being successfully handed over to a Kannel server.
* Send a delivery reprot to playSMS, when a Kannel server informs of message being delivered.
* Send a failure report to playSMS, of any failures reported by any Kannel server.
* Have better error messsages and email based reporting and file based logging of exceptions, errors and warnings.
* Support SSL in connections with playSMS and Kannel.
* Use Greenlet/eventlets to make things better, faster and easier (??)
* Authenticate requests from playSMS and Kannel to ensure they are actually coming from where they say they are coming.
* Will be probably merged with the chowk project in a better and modular way.

What's in the name?
--------------------

chowk is Hindi/Marathi/Indian vernacular slang for a traffic square where different routes meet and traffic is controlled and directed.
