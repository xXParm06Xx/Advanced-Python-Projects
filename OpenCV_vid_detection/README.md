# 👁️ Simple Face Detection System with OpenCV

A lightweight Python application that uses OpenCV to detect faces, eyes, and smiles in real-time through your webcam. Perfect for learning computer vision basics or building upon for more advanced projects!

## ✨ Features

- 🎭 **Face Detection** - Automatically detects and tracks faces in real-time
- 👀 **Eye Recognition** - Identifies and highlights eyes within detected faces
- 😊 **Smile Detection** - Recognizes when you're smiling
- 📸 **Screenshot Capture** - Save the current frame with a single keypress
- ⚙️ **Configurable Controls** - Customize keyboard shortcuts via config file
- 🎯 **High Performance** - Optimized for smooth real-time detection

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. Clone this repository:
```bash
git clone https://github.com/xXParm06Xx/OpenCV_vid_detection.git
cd OpenCV_vid_detection
```

2. Install the required dependencies:
```bash
pip install opencv-python
```

3. Run the application:
```bash
python main.py
```

That's it! Your webcam should open and start detecting faces automatically.

## 🎮 Controls

The default keyboard shortcuts are:

| Key | Action |
|-----|--------|
| `Q` | Quit the application |
| `S` | Take a screenshot |

### Customizing Controls

Want to use different keys? No problem! Just edit the `config.ini` file:

```ini
[KEYS]
exit = q
screenshot = s
```

Change the values to any key you prefer, and the app will automatically use your custom shortcuts.

## 📁 Project Structure

```
face-detection/
│
├── main.py           # Main application file
├── config.ini        # Configuration file for keyboard shortcuts
├── screenshots/      # Saved screenshots (created automatically)
└── README.md         # You are here!
```

## 🛠️ How It Works

The application uses **Haar Cascade Classifiers** from OpenCV, which are pre-trained models that can detect specific objects (in our case, faces, eyes, and smiles). Here's the basic flow:

1. Captures video feed from your webcam
2. Converts each frame to grayscale for better processing
3. Applies histogram equalization to improve detection accuracy
4. Uses cascade classifiers to detect faces, then eyes and smiles within face regions
5. Draws bounding boxes and labels on detected features
6. Displays everything in real-time!

## 📸 Screenshots

Screenshots are automatically saved to the `screenshots/` folder when you press the screenshot key. Each image captures the current frame with all detection boxes and labels visible.

## 🤝 Contributing

Found a bug or have an idea for improvement? Feel free to:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 💡 Ideas for Enhancement

Want to take this project further? Here are some ideas:

- 🎥 Add video recording functionality
- ⏸️ Implement pause/resume feature
- 🎨 Apply filters or effects to detected faces
- 📊 Track and log detection statistics
- 🔊 Add audio alerts for specific detections
- 🌈 Color-coded emotions based on smile intensity

## 🙏 Acknowledgments

- OpenCV team for the amazing computer vision library
- Haar Cascade classifiers for making face detection accessible

---

**Made with ❤️ and lots of ☕**

If you find this project helpful, consider giving it a ⭐!
