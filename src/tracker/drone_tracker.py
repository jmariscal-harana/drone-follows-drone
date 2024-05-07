import cv2

class DroneTracker:
    def __init__(self, tracker_type="MIL") -> None:
        """Initialise the drone tracking algorithm."""
        print("Tracking init!")
        if tracker_type == 'BOOSTING':
            tracker = cv2.legacy.TrackerBoosting_create()
        if tracker_type == 'TLD':
            tracker = cv2.legacy.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.legacy.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.legacy.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.legacy.TrackerCSRT_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()

        self.tracker = tracker
        self.tracker_type = tracker_type
        self.tracking = False

    def close(self) -> None:
        """Close the drone tracking algorithm."""
        print("Closing drone tracking!")

    def track(self, frame) -> None:
        """Track the drone in the frame."""
        print("Tracking drone!")

        if self.tracking:
            timer = cv2.getTickCount()

            ok, bbox = self.tracker.update(frame)

            cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else:
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    
            # Display tracker type on frame
            cv2.putText(frame, self.tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
        
            # Display FPS on frame
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    
            # Display result
            cv2.imshow("Tracking", frame)
            cv2.waitKey(1)

        else:
            bounding_box = cv2.selectROI(frame, False)
            self.tracker.init(frame, bounding_box)
            self.tracking = True