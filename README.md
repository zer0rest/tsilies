# Τσίλιες

_Τσίλιες_, pronounced as "tsilies" is a greek word which means; "to keep tabs on".

_Τσίλιες_ is an attempt to create a unified platform that performs host uptime monitoring in an easy to use and configure manner.

_Τσίλιες_ backend is mainly written in `bash` and `python`.

_Τσίλιες_ is still in a very early development stage where it's features are still being specced out. Check the issues page and feel free to comment or open an issue for a feature that you would like from an uptime monitoring platform but can't find in there.

_Τσίλιες_ scripts use mqtt for message passing between them. Currently a public mqtt broker, `iot.eclipse.org`, provided by eclipse is used. _TODO: Set up custom mqtt broker using the `mosquitto` package and post instructions on how to do so._

## Scripts

### _ping.py_

ping.py is responsible for pinging the monitored hosts. It listens to a topic defined in the
`host_topic` variable for IP addresses to ping. When a new IP address is received it pings it and publishes it's latency and status at the topics defined in `host_latency_topic` and `host_status_topic` respectively. If the host does not respond after the 1 second ping timeout expires it sets it's status to `0` and it's latency to infinite or `INF`

__TODO:__

- Test the script with IPv6 Addresses. The script has only been tested with IPv4 addresses. While, issues are not expected with IPv6 addresses, it should be testes to ensure none arise.
- Improve error handling. The script currently has no logic to inform the user if the connection to the mqtt broker failed. It also does not have any logic to inform the user if the domain name supplied at the ping command is malformed. Instead it behaves as if the host never responded.
- Compartmentalise the code more in functions for improved readability.
