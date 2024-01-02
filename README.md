# Aeronautical-Networks

## Problem Statement
This research focuses on addressing the challenge of providing Internet access to 
thousands of aeroplanes flying over the North Atlantic region. The goal is to 
establish optimal data packet routing paths for each aeroplane to reach a ground 
station (GS) and enable passenger connectivity. Two metrics are considered for 
evaluating the routing paths: end-to-end data transmission rate and end-to-end 
latency The research findings showcase the optimal routing paths for each 
aeroplane, considering single-objective and multi-objective optimizations. The 
results highlight the trade-off between data transmission rate and latency, 
providing valuable insights into the best possible connectivity options for 
aeroplanes flying over the North Atlantic. The research contributes to the 
improvement of passenger Internet access and connectivity during flights, 
enhancing the overall in-flight experience.

## Objective
Routing Optimization for Aeronautical Networks: Maximizing Data 
Transmission Rate and Minimizing Latency

## Run the file locally
1) There is only one column in the CSV file, so we must divide it into five columns: flight, timestamp, altitude, latitude, and longitude. Refer to the [link](https://spreadsheetplanet.com/split-one-column-into-multiple-columns-excel/)
2) Run main.py

## Approach
![image](https://github.com/saadmdsabah/Aeronautical-Networks/assets/103499208/d811e2f4-8d79-4c80-83e2-2d19292f9850)

1. Define Objectives: Determine the specific objectives to be optimized, such as minimizing latency, maximizing throughput, minimizing energy consumption, etc. Each objective should be quantifiable and measurable.
2. Model the Network: Create a network model that represents the connectivity between aeroplanes and the ground station. This model should capture the physical and communication characteristics of the network, including the positions of aeroplanes, signal propagation, data transfer capabilities, and any other relevant parameters.

3. Formulate the Optimization Problem: Define the optimization problem considering the objectives and constraints. This could involve formulating a mathematical objective function that combines the desired objectives and any constraints, such as the capacity of communication links or limitations on routing paths.

4. Evaluate Solutions: Assess the quality of the generated solutions using appropriate metrics for each objective. This may involve simulation or mathematical analysis to estimate the performance of the routing paths.
5. Decision-making: Analyze the set of Pareto-optimal solutions and make a decision based on the preferences or priorities of the system stakeholders. This could involve selecting a single solution from the Pareto-optimal set or using decision-making techniques to find a compromise solution.

6. Implementation and Deployment: Implement the selected routing solution in the aeronautical network infrastructure. Monitor and evaluate the performance of the deployed solution to ensure it meets the desired objectives in a real-world setting.

## Output
### FOR SINGLE-OBJECTIVE OPTIMIZATION

![image](https://github.com/saadmdsabah/Aeronautical-Networks/assets/103499208/c8ee54bb-c505-477a-96e5-c3ffea01f5b3)

### MULTIPLE-OBJECTIVE OPTIMIZATION

![image](https://github.com/saadmdsabah/Aeronautical-Networks/assets/103499208/e57097a3-ec7f-46ce-84ce-9c3b2a4dab40)


