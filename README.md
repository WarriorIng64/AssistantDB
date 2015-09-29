# AssistantDB
AssistantDB is intended to take commands processed by an earlier part of an AI
assistant toolchain and take appropriate actions with them. It can either be run
on its own as part of a shell script or interactive session, or imported as a
module in a larger Python program.

It will both carry out the indicated command and reply to the user using the
`espeak` program, which can be installed on Ubuntu using the following command:

    sudo apt-get install espeak

This module requires Python 3 and was written for my senior project at LTU.
