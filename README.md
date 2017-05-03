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
* Please check the config.ini file! and change config parameters according to your environment
* I know it's not the most generic script in the world :) but just a small wrapper for those services with option for ooping later on for making it more generic and expandable
