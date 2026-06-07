import cv2
import os
import csv
import webbrowser
from datetime import datetime

# Create folders
os.makedirs("scans", exist_ok=True)
os.makedirs("data", exist_ok=True)

history_file = "data/scan_history.csv"

if not os.path.exists(history_file):
    with open(history_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Data"])

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

last_scanned = ""
opened_urls = set()

while True:

    success, frame = cap.read()

    if not success:
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None and data:

        bbox = bbox.astype(int)

        for i in range(len(bbox[0])):

            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])

            cv2.line(
                frame,
                pt1,
                pt2,
                (0, 255, 0),
                3
            )

        cv2.putText(
            frame,
            "QR CODE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            data[:60],
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

        # Auto-open URLs
        if (
            data.startswith("http://")
            or data.startswith("https://")
        ) and data not in opened_urls:

            webbrowser.open(data)

            opened_urls.add(data)

            print(f"Opened URL: {data}")

    cv2.putText(
        frame,
        "Press S to Save | Q to Quit",
        (20, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    cv2.imshow(
        "QR Code Scanner",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s") and data:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        filename = (
            f"scans/scan_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(data)

        if data != last_scanned:

            with open(
                history_file,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    timestamp,
                    data
                ])

            last_scanned = data

        print(f"Saved: {filename}")

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
