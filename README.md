# Τσίλιες

_Τσίλιες_, pronounced as "tsilies" is a greek word which means; "to keep tabs on".

_Τσίλιες_ is an attempt to create a unified platform that performs host uptime monitoring in an easy to use and configure manner.

_Τσίλιες_ backend is mainly written in `bash` and `python`.

_Τσίλιες_ storage backend for host information is a JSON file. We chose this against a normal database like Mysql to remove unnecessary complexity and limit moving parts and points of failure.
The JSON object structure is the following:
```
[
    {
        "alert-method-down": "email-message",
        "alert-method-up": "sms-message",
        "grace-period": "60",
        "host-owner": "db_admins",
        "host-v4": "4.3.2.1",
        "host-v6": "2001:badf:00d::4321",
        "hostname": "influx_db-01",
        "last-down": "1530138795",
        "location": "med01-athens",
        "monitor-agent": "agent-1",
        "status": "up"
    }
]
```
In this object:

`hostname` is the name that will be used to identify the host. This name is used at the web interface and at the alert messages.

`host-v4` is the IPv4 Address of the host. If the host is IPv6 capable only, the value should be
`NULL`

`host-v6` is the IPv6 Address of the host. If the host is IPv4 capable only, the value should be `NULL`

`location` is the location where the host is placed. This field is optional, but is useful to identify where the device is located.

`alert-method-down` is the method(s) the platform will use to notify the user if the host goes down.
They are separated with comas, from the first method used to the last method used.

`alert-method-up` is the method the platform will use to notify the user that the host is again back up and responding to pings.

`grace-period` is the time in seconds the platform will wait before it starts issuing alerts. This can vary from 0s aka immediately to an indefinite amount of time.

`monitor-agent` is/are the monitoring agent(s) responsible for pinging the host, separated by comas.

`status` is the current status of the host. It is used by _notificationissuer.py_ together with the _grace-period_ and _last-down_ value to find out if it should issue an alert to the user or not. It is set from the _status.py_ script

`last-down` is the unix timestamp of the time the host was last detected as unresponsive to pings.

`host-owner` is the user or group of users that will be notified if the host goes down.

_Τσίλιες_ scripts use mqtt for message passing between them. Currently a public mqtt broker, `iot.eclipse.org`, provided by eclipse is used. _TODO: Set up custom mqtt broker using the `mosquitto` package and post instructions on how to do so._

## Scripts

### _ping.py_

ping.py is responsible for pinging the monitored hosts. It listens to a topic defined in the
`host_topic` variable for IP addresses to ping. When a new IP address is received it pings it and publishes it's latency and status at the topics defined in `host_latency_topic` and `host_status_topic` respectively. If the host does not respond after the 1 second ping timeout expires it sets it's status to `0` and it's latency to infinite or `INF`

__TODO:__

- Test the script with IPv6 Addresses. The script has only been tested with IPv4 addresses. While, issues are not expected with IPv6 addresses, it should be tested to ensure none arise.
- Improve error handling. The script currently has no logic to inform the user if the connection to the mqtt broker failed. It also does not have any logic to inform the user if the domain name supplied at the ping command is malformed. Instead it behaves as if the host never responded.
- Compartmentalise the code more in functions for improved readability.

### _adddelcheckhost.py_

adddelcheckhost.py is responsible for adding and deleting hosts at hosts.json and checking the correctness of the information added. Script is still a work in progress.



_Τσίλιες_ is still in a very early development stage where it's features are still being specced out. Check the issues page and feel free to comment or open an issue for a feature that you would like from an uptime monitoring platform but can't find in there.
