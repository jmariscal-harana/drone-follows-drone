# Objective
Welcome to my new drone project! I want to get a Tello drone to follow another Tello drone autonomously. While the idea is simple, there are many avenues to explore!

# Project structure
There are three different elements that I will work on in parallel: object tracking, drone control, and real-time.

## Object tracking
- Traditional methods
- Deep learning methods
  - YOLO-based tracker (easier)
  - State-of-the-art tracker (harder)  

## Control
- Simple logic based on bounding box size and centre
- Kalman filters
- Deep learning (what!?)

## Fast feedback
- Is it required? (identify any SDK bottlenecks)
- C++
- SDK hacking

For the first iteration, I have decided to go for the simplest combination as a fast way to start testing: a traditional method for object tracking + a simple algorithm for drone control.

# Steps
1. Think about the code structure
2. Code the skeleton of the system including: connecting/configuring the drone; the model as a black box (input: image, output: bounding box); control based on detections and drone state
3. Identify a traditional object tracking algorithm and visualise it
4. Write a simple algorithm that uses the bounding boxes to send commands to the drone

# References
- https://github.com/fvilmos/tello_object_tracking

# Docker X11 (MACOS)
You need to follow some of [these steps](https://stackoverflow.com/questions/75386154/how-to-run-xeyes-in-docker-ubuntu) to enable X11 for your Docker container in MACOS:

- Install XQuartz
- Start XQuartz
- Goto XQuartz- > Settings -> Security and select "Authenticate Connections" and "Allow connections from network clients"
- Restart XQuartz

```
xhost + localhost
```