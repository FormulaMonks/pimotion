Pimotion
========

Pimotion is a motion detector application that runs on the Raspberry PI. It captures snapshots of movement and uploads the montage image to an [M2X](https://m2x.att.com) feed.

### Package Dependencies

```
numpy==1.6.2
PIL==1.1.7
requests==2.4.3
picamera==1.8
m2x==0.3
```

### Installation

Installation can be done through cloning the repo onto your Raspberry PI:

	$ git clone https://github.com/citrusbyte/pimotion.git
	$ cd pimotion
	$ pip install -r requirements.txt


### Configuration

Copy the `settings.cfg.example` file to `settings.cfg` and modify it with your CloudAPP username and password.

### Running

The application can be started by running:

	$ python pimotion/main.py

### License

This project is delivered under the MIT license. See [LICENSE](LICENSE) for the terms.