# Digital Menu 🍴📱

**Digital Menu** is a Django-based platform that helps vendors generate unique QR codes linking to their online menus. Vendors simply provide their business name and a link to their hosted digital menu (Google Drive, website, etc.). A scannable QR code is instantly generated, ready to be printed and placed on tables for commercial use.

## 🔧 How It Works

1. Vendor submits:
   - Business Name
   - Public link to their hosted digital menu (PDF, website, etc.)
2. System generates a **unique QR code** for that vendor.
3. Vendor can **download and print** the QR code.
4. Customers scan the QR using their smartphones to instantly view the menu.


## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **QR Code Library**: `qrcode`, `Pillow`
- **Frontend**: Django templates + Bootstrap

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/digital-menu.git
   cd digital-menu
