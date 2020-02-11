import os

# external monitor
#-----------------------------------------------#
PreferredOption = 'DisplayPort-1-1'
#-----------------------------------------------#

# default monitor
#-----------------------------------------------#
DefaultOption = 'eDP-1'
#-----------------------------------------------#

# all connected / disconnected monitors
#-----------------------------------------------#
connected_monitors = []
disconnected_monitors = []
#-----------------------------------------------#

# retrive a list of connected / disconnected monitors
#-----------------------------------------------#
xrandr_cmd = os.popen("xrandr").read()
xrandr_cmd = xrandr_cmd.split("\n", 1)[1]

temp = []

for line in xrandr_cmd.splitlines():
    if not line.startswith(' '):
        temp.append(line)

for line in temp:
    if line.split(' ')[1] == 'connected':
        connected_monitors.append([line.split(' ')[0], line.split(' ')[1]])
    else:
        disconnected_monitors.append([line.split(' ')[0], line.split(' ')[1]])
#-----------------------------------------------#

# set preferred monitor if available or default otherwise
#-----------------------------------------------#
if [PreferredOption, 'connected'] in connected_monitors:
    
    # set all connected monitor interfaces to '--off'
    for i in range(0, len(connected_monitors)):
        os.system('xrandr --output ' + connected_monitors[i][0] + ' --off ' )
    
    # set PreferredOption connected monitor interfaces to '--auto'
    os.system('xrandr --output ' + PreferredOption + ' --auto ' )

else:
    os.system('xrandr --output ' + DefaultOption + ' --auto ' )
#-----------------------------------------------#
