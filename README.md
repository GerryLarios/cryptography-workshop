# cryptography-workshop
Cryptography Workshop following the content of "Computer &amp; Internet Security - A Hands-on Approach" by Wenliang Du

## Setup

Run the following command to build a docker image based on [seedvm-cloud-lab](https://github.com/seed-labs/seed-labs/blob/master/manuals/cloud/seedvm-cloud.md)

```bash
docker build . -t seedlab:v1
```

In order to create and log into the container using bash, run the following command.

```bash
docker run -a stdin -a stdout -i -t seedlab:v1 /bin/bash
```

Finally, install the dependencies.

```bash
cd src-cloud && ./install.sh
```
