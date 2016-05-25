Pimotion
========

![PIMotion Logo](docs/logo-256.png?raw=true)

Pimotion is a motion detector application that runs on the Raspberry PI. It captures snapshots of movement and uploads the montage image to an [M2X](https://m2x.att.com) device.

### Installation

#### 1. System dependencies
```bash
$ sudo apt-get install libffi-dev
```
See: https://urllib3.readthedocs.io/en/latest/security.html#pyopenssl

#### 2. Getting the source code

Installation can be done through cloning the repo onto your Raspberry PI:

```bash
	$ git clone https://github.com/citrusbyte/pimotion.git
```

#### 3. Python package dependencies
Run the following command from the pimotion project root folder:
```bash
	$ pip install -r requirements.txt
```

### Configuration

Copy the `settings.cfg.example` file to `settings.cfg` and modify it with your CloudAPP and M2X credentials.

### Running

The application can be started by running:

	$ python pimotion/main.py

### Example Capture
![pimotion-demo-capture](https://raw.githubusercontent.com/citrusbyte/pimotion/master/docs/pimotion-demo-capture.jpg)

### License

This project is delivered under the MIT license. See [LICENSE](LICENSE) for the terms.

### Attributions

Written by [Sarah Henkens](https://github.com/sarahhenkens), sponsored by [Citrusbyte](https://citrusbyte.com/)

## About Citrusbyte

![Citrusbyte](http://i.imgur.com/W6eISI3.png)

Pimotion is lovingly maintained and funded by Citrusbyte.
At Citrusbyte, we specialize in solving difficult computer science problems for startups and the enterprise.

At Citrusbyte we believe in and support open source software.
* Check out more of our open source software at Citrusbyte Labs.
* Learn more about [our work](https://citrusbyte.com/portfolio).
* [Hire us](https://citrusbyte.com/contact) to work on your project.
* [Want to join the team?](http://careers.citrusbyte.com)

*Citrusbyte and the Citrusbyte logo are trademarks or registered trademarks of Citrusbyte, LLC.*
