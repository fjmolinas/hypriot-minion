# hypriot-OS based riotpi image

This allows setting up a Hypriot-OS based riotpi image. This is an alternative
to [pifleet-minion](https://github.com/kaspar030/pifleet-minion)

Currently it does the same as the pifleet-minion:

    - at first boot, set hostname to "pi-${cpu serial number}"
    - install salt-minion, set up pihub.riot-labs.de as master

But also can:

    - setup wifi
    - add a base docker configuration

But the main interest is running an optimized for Docker
Debian-based image. So if that does not interest you
checkout the above mentioned [pifleet-minion](https://github.com/kaspar030/pifleet-minion),
it does exactly what you need.

## Requirements

- Install [hypriot/flash](https://github.com/hypriot/flash)

Follow detailed install instructions [here](https://github.com/hypriot/flash#installation), otherwise

```
$ sudo apt-get install pv unzip hdparm
$ curl -O https://raw.githubusercontent.com/hypriot/flash/master/$(uname -s)/flash
$ chmod +x flash
$ sudo mv flash /usr/local/bin/flash
```

- Optionally generate a `user-data.yml` configuration file.

### `user-data.yml`

The `user-data.yml` [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html)
file can be generated from a jinja rendered template via a provided configuration
file:

```
$ python renderer.py --config-file user-data.cfg
```

See [sample-user-data.cfg](sample-user-data.cfg) for default configuration
files.

You can of course provide your own `user-data.yml`

## Bootstrapping

Assuming a `user-data.yml` is passed then:

```
$ flash --userdata user-data.yml <version>
```

with the hypriot-OS version of your choosing:

- HypriotOS/armv7 HypriotOS/armv6 all RPI: https://github.com/hypriot/image-builder-rpi/releases/download/v1.12.3/hypriotos-rpi-v1.12.3.img.zip

## Further setup

Further configuration should be done via [Salt](https://docs.saltproject.io/en/latest/).
So please follow setups in this [README.md](https://github.com/fjmolinas/pifleet-salt).
