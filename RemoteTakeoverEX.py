from yeelight import discover_bulbs, Bulb
import time

if __name__ == '__main__':

    #Variable devices contains a list of dictionaries providing information regarding yeelight bulbs in particular
    #including IP address and Port Number
    devices = discover_bulbs()

    # assuming the first listed device is the one you want to remotely control, use index 0
    ip_address_1 = devices[0]['ip'] #stores ip address of bulb 1

    #make additional variables for each characteristic you'd like to keep track of and access
    #port_1 = devices[0]['port'] #stores port number of bulb 1

    #Once you have a bulb's IP Address, you can make commands from a python script
    bulb_1 = Bulb(ip_address_1)
    bulb_1.turn_on()
    bulb_1.effect = "sudden"

    #There are more commands possible that you can enact once you have control over a bulb. Check Online.
    
    #This is a simple subscript that will generate a strobe light effect for 30 seconds
    time_end = time.time() + 60 * 0.5 #time_end is set 30 seconds after current time
    while time.time() < time_end:
        bulb_1.set_rgb(0, 0, 255)
        bulb_1.set_rgb(255, 255, 0)

    #We are able to remotely control these bulbs due to a lack of encryption and secure connection protocols as a design flaw made by the manufacturer.
