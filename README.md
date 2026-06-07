# QR Code Scanner 📷

<p align="center">
  A real-time QR Code Scanner built with <strong>Python</strong> and <strong>OpenCV</strong>.<br>
  Detect, decode, save, and automatically open QR code URLs using your webcam.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## ✨ Features

✔️ Real-time QR Code Detection  
✔️ QR Code Decoding  
✔️ Automatic URL Opening  
✔️ Save Scanned Data to Text Files  
✔️ Scan History Logging (CSV)  
✔️ Webcam-Based Scanning  
✔️ QR Boundary Highlighting  
✔️ Simple & User-Friendly Controls  

---

## 🖼️ Demo

### QR Code Detection:

### Scanned Result

```md
![Scanned Result](screenshots/scanned_qr.png)
```

---

## 📂 Project Structure:

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

---

## 🚀 Getting Started:

### 1️⃣ Clone the Repository

```bash
git clone <https://github.com/caffineblud/QR-Code-Scanner>
cd QR-Code-Scanner
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

Point your webcam toward a QR code and start scanning.

---

## ⌨️ Controls

| Key | Action |
|------|---------|
| **S** | Save scanned QR data |
| **Q** | Quit the application |

---

## 📁 Output:

### Saved Scan Files

```text
scans/
├── scan_20260607_101530.txt
├── scan_20260607_101842.txt
```

### Scan History

All unique scans are automatically logged in:

```text
data/scan_history.csv
```

Example:

| Timestamp | Data |
|-----------|------|
| 2026-06-07 10:15:30 | https://example.com |

---

## 🔗 Automatic URL Opening

If the scanned QR code contains a URL:

```text
https://github.com/
```

The application will:

- Detect the QR code
- Decode the URL
- Open it in your default browser
- Store it in scan history

---

## 🛠️ Technologies Used:

- *Python*
- OpenCV
- CSV Module
- WebBrowser Module

---

## 💡 Future Enhancements:

- Barcode Scanner Support
- Scan QR Codes from Images
- Export History to Excel
- Tkinter GUI Version
- Multiple QR Detection
- Dark Theme Dashboard

---

## 📜 License

This project is open-source and available under the MIT License.

---
## Author:
***Yash Kumar Singh***

---

<p align="center">
  ⭐ If you like this project, consider giving it a star on GitHub! ⭐
</p>
