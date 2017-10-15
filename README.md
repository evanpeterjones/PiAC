# PiAC
Bringing my Air Conditioner into the internet of Things!

# What it does!

These scripts use an IR blaster to send binary to my A/C unit using its own code! Also connects to a database I set up through firebase, so I can trigger the script to run, turning on my A/C unit, from an application that connects to firebase! 

# DIY

-what's not on GitHub

Wrote a python script that reads the binary code coming from the remote for my non-smart Air Conditioner, at a set speed (5/1000 seconds), and then writes it to a file (IRFile.txt). This was done using a breakout board for the GPIO pins on the Raspberry Pi, and connecting an IR Receiver I bought from Amazon for a few dollars. 

-what IS on GitHub

1. The binary remote file!

2. The python script that reads the binary into the IR Blaster you'd connect to your raspberry Pi (which can be done without a breakout board!)
   -You can follow my pin-layout, or change the variables to fit yours!
   -Remove the firebase data.