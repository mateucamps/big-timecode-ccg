# big-timecode-ccg
Big Timecode display for CasparCG, designed to be used in Broadcast Control Rooms.

Tested on Windows, Ubuntu and Raspberry Pi 4B.

It supports two channels, named "Player 1" and "Player 2" by default.

![Interface](/screenshot.gif?raw=true "Interface")


## How to use:
1. Clone or download this repository
2. Install Python 3
3. Install python-osc module:
```bash
~$ pip3 install python-osc
```
4. Modify ```settings.py``` to fit your needs.
5. Modify ```casparcg.conf``` and add the following lines:
```xml
<osc>
    <predefined-clients>
        <predefined-client>
            <address> #BIG TIMECODE MACHINE'S IP# </address>
            <port>5253</port>	
        </predefined-client>		
    </predefined-clients>
</osc>

```
6. Run ```main.py```
7. Start playing media on your CasparCG Server to see some output. If nothing comes up, check ```settings.py``` > OSC Routes strings.