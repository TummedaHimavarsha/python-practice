# invisibility_cloak.py
# Requires: pip install opencv-python numpy

import cv2
import numpy as np
from collections import deque

def get_background(cap, frames=60):
    bg_buffer = deque(maxlen=frames)
    print("[i] Capturing background... hold still for ~2 sec")
    for _ in range(frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        bg_buffer.append(frame)
        cv2.waitKey(1)
    # Median to smooth tiny movements/noise
    return np.median(np.array(bg_buffer), axis=0).astype(np.uint8)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[!] Could not access camera.")
        return

    # Warm-up
    for _ in range(10):
        cap.read()

    background = get_background(cap, frames=60)

    print("[i] Ready! Show a RED cloth to become invisible.")
    print("[i] Keys: q=quit, b=re-capture background")

    kernel = np.ones((3, 3), np.uint8)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # ---- COLOR MASKS ----
        # Red wraps around HSV hue (0 and 180), so use two ranges.
        # Tweak these if your lighting differs.
        # For GREEN cloth, try: [(35, 40, 40)-(85, 255, 255)]
        # For BLUE cloth,  try: [(90, 40, 40)-(130, 255, 255)]
        lower_red1 = np.array([0,   120, 70])
        upper_red1 = np.array([10,  255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Clean mask: remove noise & fill small gaps
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.GaussianBlur(mask, (3, 3), 0)

        # Invert mask to keep non-cloak regions
        inv_mask = cv2.bitwise_not(mask)

        # Segment current frame and background
        current_part = cv2.bitwise_and(frame, frame, mask=inv_mask)
        background_part = cv2.bitwise_and(background, background, mask=mask)

        # Final composite
        output = cv2.addWeighted(current_part, 1, background_part, 1, 0)

        cv2.imshow("Invisibility Cloak (press q to quit, b to recapture bg)", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            background = get_background(cap, frames=60)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
