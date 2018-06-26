# This script is responsible for listening to a predefined mqtt topic for a host
# to ping.


# Import the mqtt module, used for message passing between tsilies' scripts.
import paho.mqtt.client as mqtt

# Import the threading module.
import threading

#import the subprocess module, used to execute the ping command.
import subprocess

# Define the name of the monitoring agent.
agent_nickname = "agent-1"

# Define the topic where the script will listen for hosts to ping.
host_topic = "tsilies/" + agent_nickname + "/to_ping/"

# Define the domain/ip of the mqtt server.
mqtt_broker = "iot.eclipse.org"

# Create the function to ping the hosts and publish the latency and host status
# in the predefined topics.
# This is the function that will be executed at the on_message callback.
def toPing(client, userdata, message):

    # Define the variable where the host domain/ip will be stored.
    host_ip = str(message.payload)

    # Print the host to-be-pinged
    print "Received message to ping: " + host_ip

    # Define the host latency reporting topic.
    host_latency_topic = "tsilies/" + agent_nickname + "/latency/" + host_ip + "/"

    # Define the host status reporting topic.
    host_status_topic = "tsilies/" + agent_nickname + "/status/" + host_ip + "/"

    # Define ping command to execute
    ping_cmd = "ping -c 3 -i 0.2 -W 1 " + host_ip + " | grep rtt | awk '{ printf $ 4 }' | cut -d'/' -f2 "

    # Execute the ping command
    ping = subprocess.Popen(ping_cmd, shell=True, stdout=subprocess.PIPE)

    # Wait for the process to terminate and collect the standard output.
    output, error = ping.communicate()

    # Check if the host responded to pings or not.
    # If it did, collect the latency.
    if output == "":
        # Set the host status to 0 which equals "Down"
        status = "0"

        # Set the latency to "infinite"
        latency = "INF"

        # Publish the host status to "host_status_topic"
        client.publish(host_status_topic, status)

        # Publish the latency status to "host latency_topic"
        client.publish(host_latency_topic, latency)

    else:
        # Set the host status to 0 which equals "Down"
        status = "1"

        # Set the host status to 0 which equals "Down"
        # .strip() is used to remove the blank line on the ping output.
        latency = output.strip()

        # Publish the host status to "host_status_topic"
        client.publish(host_status_topic, status)

        # Publish the latency status to "host latency_topic"
        client.publish(host_latency_topic, latency.strip())


# Create an instance of the mqtt client.
client = mqtt.Client(agent_nickname)
print "Created an instance of the mqtt client object."

# Connect to the mqtt broker.
client.connect(mqtt_broker)
print "Connected to the mqtt client."

# If the connection was successful, subscribe to the hosts-to-ping topic.
client.subscribe(host_topic)

# Define the function to call when a message is received on "host_topic".
client.on_message = toPing

# Make the script continuously listen for new messages.
client.loop_forever()
