# Attack demonstration took kits for Industry 4.0 using AI and cloud

We introduce attack demonstration took kits for Industry 4.0 using actual machines (water supply pump system).

This tool kit is portable, and easy to prepare, so is useful for instructing the cyber-risks of ICS whenever and whenever we want.
In aspects of Industry 4.0, we especially focus on the security risks of ICS in the following aspects:
* When computers and devices are connected interactively
* When AI on the cloud is used for controlling the ICS

<img src="toolSummary.png" alt="Overview of the demo tool" title="Overview of the demo tool" width="50%" height="50%">

<a href="https://github.com/sisoc-tokyo/AttackDemoTookkit_Industry4/blob/master/AttackDemoTookkitsforIndustry4usingAIandCloud.pdf" download>Documentation of the tool is here</a>

## Demo Tool detail
Our demonstration tool consists of the following.
* the water supply pump system
* Attack tools

The structure of the water supply pump system is as follows.
* Water pump: Provides water for consumers.
* Controller: Controls the water level of the cylinder using Modbus/TCP.
* OPC / HMI Server (Windows Server 2008 R2): OPC server relays communications among Controller using Modbus/TCP. HMI visualizes the current water level.
* IoT sensor: Measure current temperature.
* Production control server (Windows Server 2008 R2): Stores the dataset of the past water level per time and temperature.
* AI server on the cloud (Cent OS 7): Instruct the desirable water level per time and temperature using the machine learning.

## Attack scenario
The following is the attacker's activities.
1. Infects a PC in the Business zone
2. A lateral movement to the Production control server
3. Contaminate the AI dataset on the Production control server

The following is the normal activities.
4. The contaminated dataset is sent to AI Server
5. The Production control server queries the desirable water level to the AI Server
6. AI Server returns incorrect water level  judged from the contaminated dataset
7. The Production control server sends incorrect  SetPOint to the OPC server
8. The water level is unintentionally changed
  
