# awsroms

Test the ROMS ocean model on AWS

### Why AWS?

We assume that AWS has currently the biggest market share of the mainstream public cloud providers, and therefore can be assumed to have relatively recent, representative technology. Focusing on a single provider allows us to use ”proprietary” (in the sense of ”non-portable”) helper tools to simplify the provisioning process (in the case of AWS that would be cloudfront etc. in general, and cfncluster in particular). Although this necessarily leads to non-portable code, it provides a proof of concept and yields a concrete hardware/networking topology pattern, which can later be adapted to other cloud providers.

The long-term goal is to produce configuration tools which are portable between cloud providers, to avoid ”provider lock-in”. Clearly, it is desirable to have configuration software that works in combination with most public cloud providers and popular open-source software platforms for private clouds (OpenStack, etc.)

### TODO

everything minus an ambitious Readme file
