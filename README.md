# QR Code Scanner

*A simple real-time QR Code Scanner built with Python and OpenCV. The application uses a webcam to detect and decode QR codes, display the extracted information, and save scan results for future reference.*

## Features

* Real-time QR code detection
* QR code decoding
* Webcam integration
* Save scanned QR data to text files
* Store scan history in CSV format
* Easy-to-use keyboard controls

## Technologies Used

* Python
* OpenCV

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd QR-Code-Scanner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

### Controls

| Key | Action               |
| --- | -------------------- |
| S   | Save scanned QR data |
| Q   | Quit the application |

## Project Structure

```text
QR-Code-Scanner/
│
├── main.py
├── requirements.txt
├── README.md
│
├── scans/
│
├── screenshots/
│
└── data/
    └── scan_history.csv
```

## Output

* Detected QR code data is displayed on the screen.
* Saved scans are stored in the `scans` folder.
* Scan history is maintained in `data/scan_history.csv`.

## Future Enhancements

* Barcode scanning support
* Scan QR codes from image files
* Automatic URL opening
* Graphical User Interface (GUI)
* Excel export support

## License

This project is open source and available under the MIT License.

---

## Author:
***Yash Kumar Singh***
