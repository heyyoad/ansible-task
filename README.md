# BigPanda DevOps Exercise - Yoad Submission
## INTRO
Hey! so my name is Yoad, and this is my submission of the excercise, hope you'd like it :)

### Actions
So what i've done is basically:

* I've created the requested services (if i understood those correctly :)) using node js.
* Instead of creating a role for each, i've decided to create a common role for the node.js apps, as it would be easier to update it - just copy a new app to the folder and add a new dict to the vars file.
* I've decided to use pm2 for local deployment of the node apps and for "local" monitoring. nagios/other should be used as well to centrally monitor it.
* I've added a small python wrapper script for running the playbook after deploying the machine
* In case i forgot something - everything else should be documented within the yaml files and inside the node projects files.

#### Script
* Should be run with "python panda_wrapper.py"
* You should define the hostname dns for the "base" machines in your /etc/hosts file. (e.g base 172.28.128.3)
* Please check the config.ini file! and change config parameters according to your environment
* I know it's not the most generic script in the world :) but just a small wrapper for those services asked, with an option for OOPing later on - for making it more generic and expandable

#### Last note
I've noticed the following vagrant error i had from the beginning: 

"ERROR! Attempted to execute "/home/user/panda/devops-exercise1.git/dev/hosts" as inventory script: Inventory script (/home/user/panda/devops-exercise1.git/dev/hosts) had an execution error: Traceback (most recent call last):
  File "/home/user/panda/devops-exercise1.git/dev/hosts", line 100, in <module>
    ssh_host = get_ip(machine_id, provider)
  File "/home/user/panda/devops-exercise1.git/dev/hosts", line 62, in get_ip
    raise RuntimeError("No IP for NIC %d machine %s" % (nic_id, machine_id))
RuntimeError: No IP for NIC 2 machine 11946f92-68d6-4486-8ec1-e64e5e75b639"
 
It seems like vagrant doesn't finish the deployment process before running the playbook.
running vagrant provision again seems to work well.
