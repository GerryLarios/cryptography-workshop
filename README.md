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

## Content
[Secret-Key Encryption](./section_1/README.md)
[One-Way Hash Function](./section_2/README.md)
[Public Key Cryptography](./section_3/README.md)
[Public Key Infrastructure](./section_4/README.md)
[Transport Layer Security](./section_5/README.md)
[Bitcoin and Blockchain](./section_6/README.md)
