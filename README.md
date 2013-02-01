Based on https://github.com/deliciousrobots/ubuntu-hp-folio-13

Some scripts to make Ubuntu 12.04 and Fedora 18 on HP Folio 13 a better experience.

* suspend-lid-closed: checks every 2 seconds to see if lid is closed and suspends
laptop if it is, fix for https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1010926 .
This does not respect system "When lid is closed" setting in Power settings, it always
just suspends if the lid is closed.

WARNING:
This may cause your laptop to explode in a ball of fire. RUN AT YOUR OWN RISK.

INSTRUCTIONS
============

Suspend on lid-close
--------------------
### Ubuntu 

First install supervisor

$ sudo apt-get install supervisor

Copy the scripts into /usr/local/sbin

    sudo cp scripts/* /usr/local/sbin/

Copy the supervisor configs

    sudo cp supervisor_conf/* /etc/supervisor/conf.d/

Restart supervisor:

    sudo service supervisor restart

### Fedora 18 

    sudo cp scripts/* /usr/local/sbin

Give it execute permission
    chmod u+x /usr/local/sbin/lid-suspend

    cp systemd/* /lib/systemd/system/lid-suspend.service

Make symbolic link
    cd /etc/systemd/system/
    ln -s /lib/systemd/system/lid-suspend.service lid-suspend.service

Make systemd take notice of it
    systemctl daemon-reload

Activate a service immediately
    systemctl start lid-suspend.service

Enable a service to be started on bootup
    systemctl enable lid-suspend.service


Brightness Keys
---------------

Generic way to set arbitrary brightness up/down keys since the builtin ones
don't work on this laptop.

    sudo apt-get install xdotool

Open "Keyboard" settings app, go to Shortcut tab, click Custom Shortcut, then
the little + button to add a shortcut.

    name: Brightness Up
    command: xdotool key XF86MonBrightnessUp

and another:

    name: Brightness Down
    command: xdotool key XF86MonBrightnessDown

Click where it says "Disabled" and then hit the key-combo you want, I use F2 and F3.
