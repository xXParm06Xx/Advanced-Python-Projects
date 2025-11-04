# 👁️ Simple Face Detection System with OpenCV

A lightweight Python application that uses OpenCV to detect faces, eyes, and smiles in real-time through your webcam. Perfect for learning computer vision basics or building upon for more advanced projects!

## ✨ Features

- 🎭 **Face Detection** - Automatically detects and tracks faces in real-time
- 👀 **Eye Recognition** - Identifies and highlights eyes within detected faces
- 😊 **Smile Detection** - Recognizes when you're smiling
- 📸 **Screenshot Capture** - Save the current frame with a single keypress
- 🎥 **Video Recording** - Record your webcam feed with detection overlays
- ⏸️ **Pause/Resume** - Freeze the frame while keeping the window open
- 📊 **FPS Display** - Real-time frames per second counter
- 🔴 **Recording Indicator** - Visual feedback when recording is active
- ⚙️ **Configurable Controls** - Customize keyboard shortcuts via config file
- 🎯 **High Performance** - Optimized for smooth real-time detection at 144 FPS

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
| `P` | Pause/Resume the video feed |
| `R` | Start/Stop recording |

### Customizing Controls

Want to use different keys? No problem! Create or edit the `config.ini` file:

```ini
[KEYS]
exit = q
screenshot = s
pause = p
record = r
```

Change the values to any key you prefer, and the app will automatically use your custom shortcuts.

## 📁 Project Structure

```
OpenCV_vid_detection/
│
├── main.py           # Main application file
├── config.ini        # Configuration file for keyboard shortcuts
├── screenshots/      # Saved screenshots (created automatically)
├── recordings/       # Saved video recordings (created automatically)
└── README.md         # You are here!
```

## 🛠️ How It Works

The application uses **Haar Cascade Classifiers** from OpenCV, which are pre-trained models that can detect specific objects (in our case, faces, eyes, and smiles). Here's the basic flow:

1. Captures video feed from your webcam at up to 144 FPS
2. Converts each frame to grayscale for better processing
3. Applies histogram equalization to improve detection accuracy
4. Uses cascade classifiers to detect faces, then eyes and smiles within face regions
5. Draws bounding boxes and labels on detected features
6. Displays FPS counter and recording indicator
7. Shows everything in real-time with optional recording capability

### Detection Details

- **Face Detection**: Uses frontal face cascade on the entire frame
- **Eye Detection**: Searches for eyes only within detected face regions
- **Smile Detection**: Focuses on the lower half of detected faces for better accuracy

## 📸 Screenshots & Recordings

- **Screenshots**: Saved to `screenshots/screenshot_X.jpg`
- **Video Recordings**: Saved to `recordings/recording_X.mp4` where X increments automatically (recording_1.mp4, recording_2.mp4, screenshot_1, screenshot_2 etc.)
- Both folders are created automatically when you first use these features

### Recording Format

Videos are saved in MP4 format with H.264 encoding at 20 FPS, compatible with Mac, Windows, and Linux.

## 🎬 Using the Features

### Taking Screenshots
Press `S` at any time to capture the current frame with all detection overlays visible.

### Recording Video
1. Press `R` to start recording - you'll see a red dot and "REC" indicator
2. Press `R` again to stop recording
3. Your video is automatically saved with an incremented filename

### Pausing
1. Press `P` to freeze the current frame
2. While paused, you can still take screenshots
3. Recording is disabled while paused
4. Press `P` again to resume

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

- ✅ ~~Add video recording functionality~~ (Done!)
- ✅ ~~Implement pause/resume feature~~ (Done!)
- 🎨 Apply filters or effects to detected faces
- 📊 Track and log detection statistics
- 🔊 Add audio alerts for specific detections
- 🌈 Color-coded emotions based on smile intensity
- 💾 Unique screenshot filenames with timestamps
- ⚡ GPU acceleration for better performance
- 🎭 Additional facial feature detection (nose, mouth, etc.)
- 📹 Configurable recording quality and FPS

## 🙏 Acknowledgments

- OpenCV team for the amazing computer vision library
- Haar Cascade classifiers for making face detection accessible

---

**Made with ❤️ and lots of ☕**

If you find this project helpful, consider giving it a ⭐!