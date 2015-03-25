Installation Guide
==================

This guide will explain step by step how to set up your Raspberry PI to run the pimotion application.

## Raspberry PI Setup

### Hardware

The camera module is required for this application to run. For the installation of the hardware I refer to the [official guide](http://www.raspberrypi.org/help/camera-module-setup).

### Operating System

I recommend the [operating system name] OS, this is the OS that the pimotion application has been developed on.

### Enabling the camera module

There are 2 ways of enabling the camera module:

1. During the OS installation
	During the installation of the operating system, you will be promted for additional actions to take. In this menu, one of the options is to enable/disable the camera module.

2. After installation
	If your Raspberry PI already has a running operating system you can call up the same setup menu by running the following command:

	```
	$ sudo raspi-config
	```

	Select `Enable camera` and hit `Enter`, then go to `Finish` and you'll be prompted to reboot.

### Testing the camera

Make sure your Raspberry PI is connected to a monitor/tv with an hdmi cable and login to the shell. Make sure to login on the PI itself, not through SSH.

In the shell, run the following command to trigger the preview window of the camera:

```
$ raspistill -d
```

You should see a preview window for a couple of seconds which closes by itself. If you see this, your camera module is working correctly.

In case the preview does not show or you receive an error, refer to the [troubleshooting guide](http://www.raspberrypi.org/documentation/troubleshooting/hardware/camera.md) on the Raspberry PI website.

## Preparing the system

### Required packages

Run the following command to install the required system packages:

```
$ sudo apt-get update
$ sudo apt-get install python-dev python-pip imagemagick
```

### Generate your SSH key pair

You will need to generate a SSH key pair to be able to pull from our private repo. In your Raspberry PI shell run the following command to generate this key pair:

```
$ ssh-keygen -t rsa -C "your_email@example.com"
```

### Gain access to the private repo

You will need to add the generated public key as a deploy key to the pimotion private repo.

Copy the contents of the id_rsa.pub file in your clipboard.

```
cat ~/.ssh/id_rsa.pub
```

And add it as a deploy key to the private repo: `https://github.com/citrusbyte/pimotion/settings/keys`.

For additional help with the SSH key pair setup please refer to the [GitHub guide](https://help.github.com/articles/generating-ssh-keys/).


## Pimotion application installation

### Python

Confirm that python is installed on the system.

```
$ python --version
Python 2.7.3
```

### Getting the source code

The pimotion application's source code is in a private repo on our github account. Run the following command to pull the latest version:

```
$ mkdir ~/projects
$ cd ~/projects
$ git clone git@github.com:citrusbyte/pimotion.git
```

### Dependency installation

In the pimotion folder run the following command to install all the dependent python packages:

```
$ sudo pip install -r requirements.txt
```

### Additional setup

Create the tmp folder that will hold the captured images:

```
$ mkdir ~/projects/pimotion/captures
```

### Configuration

Make a copy of the provided `settings.cfg.example` configuration file:

```
$ cd ~/projects/pimotion
$ cp settings.cfg.example settings.cfg
```

Open up the `settings.cfg` file in your favorite editor and update the configuration values.

__cloudapp__:
 * username: Your CloudApp username
 * password: Your CloudApp password

__m2x__:
 * api_key: Your master API key or the device specific API key
 * device_id: The Device ID
 * stream: The name of the stream in your M2X device

### Running pimotion

Make sure you are in the correct working directory:

```
$ cd ~/projects/pimotion
```

Start the application with the following command:

```
$ python pimotion/main.py
```

Example output of a correct running pimotion application:

	$ python pimotion/main.py 
	Waiting 2 seconds for the camera to warm up
	Started recording
	Started working on capturing
	Captured detected-01.jpg
	Captured detected-02.jpg
	Captured detected-03.jpg
	Captured detected-04.jpg
	Captured detected-05.jpg
	Captured detected-06.jpg
	Captured detected-07.jpg
	Captured detected-08.jpg
	Captured detected-09.jpg
	Captured detected-10.jpg
	Captured detected-11.jpg
	Captured detected-12.jpg
	Captured detected-13.jpg
	Captured detected-14.jpg
	Captured detected-15.jpg
	Generating the montage
	Finished capturing
	Public URL: http://cl.ly/image/*******/download/montage.jpg
	Posted URL to M2X channel motion-photos

