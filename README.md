# 🔍 AI Image Super-Resolution

Enhance your low-resolution images with AI-powered super-resolution using this web app powered by EDSR and Streamlit. Upload your photos to apply 4x upscaling and save the enhanced results with a click!

---

## ✨ Key Features

### 🤖 AI-Powered Super-Resolution
- **4x Image Upscaling** - Enhances low-resolution images using deep learning
- **EDSR Model** - Enhanced Deep Super-Resolution for high-quality results
- **Realistic Detail Reconstruction** - Restores facial features, edges, and fine textures
- **GPU/CPU Support** - Automatic detection and support for CUDA acceleration

### 🎨 User-Friendly Interface
- **Simple Upload** - Drag-and-drop or click to upload images (JPG, JPEG, PNG)
- **One-Click Enhancement** - Instant processing with progress indicator
- **Side-by-Side Comparison** - View original and enhanced images
- **Download Support** - Export enhanced images in PNG format

### ⚡ Advanced Features
- **Real-time Processing** - Fast inference on both GPU and CPU
- **Batch Processing Ready** - Architecture supports multiple image processing
- **Memory Efficient** - Optimized tensor operations and caching
- **Cross-platform** - Works on Windows, macOS, and Linux

---

## 🏗️ Architecture

### **Backend (Python)**
- **Main Application** (`app.py`) - Streamlit web interface and image processing
- **Super-Resolution Engine** - EDSR model integration
- **PyTorch Framework** - Deep learning inference
- **Image Processing** - PIL and OpenCV for image handling

### **Frontend (Streamlit)**
- **Modern Web Interface** - Built-in Streamlit UI components
- **Responsive Design** - Works on desktop and tablet devices
- **Real-time Feedback** - Loading indicators and status messages
- **File Management** - Direct download functionality

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda package manager
- Git
- 2GB+ RAM (4GB+ recommended for GPU)
- CUDA 11.0+ (optional, for GPU acceleration)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AkshathaaRk/AI-Image-Super-Resolution.git
   cd AI-Image-Super-Resolution
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

---

## 🚀 Usage

1. **Open the Application** - Navigate to the Streamlit interface
2. **Upload Image** - Click "📤 Upload a low-resolution image" and select a JPG, JPEG, or PNG file
3. **Enhance** - Click the "🚀 Enhance Image" button
4. **View Results** - Compare original and enhanced versions side-by-side
5. **Download** - Click "⬇️ Download Enhanced Image" to save the result

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:
- **streamlit** - Web application framework
- **torch** - Deep learning framework
- **torchvision** - Computer vision utilities
- **pillow** - Image processing
- **opencv-python** - Advanced image operations
- **numpy** - Numerical computing
- **super-image** - EDSR model package
- **basicsr** - Basic SR research utilities
- **realesrgan** - Real-ESRGAN model support

---

## 🔧 Development Setup

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
   ```bash
   git commit -m "Add: your feature description"
   ```
6. Push to your fork
   ```bash
   git push origin feature/your-feature
   ```
7. Submit a Pull Request

---

## 🎯 Supported Image Formats
- **JPG/JPEG** - Lossy compression format
- **PNG** - Lossless compression format
- **Recommended**: PNG for best quality preservation

---

## 💡 How It Works

1. **Upload** - User uploads a low-resolution image
2. **Processing** - Image is converted to tensor format
3. **Super-Resolution** - EDSR model performs 4x upscaling
4. **Output** - Enhanced image is converted back to displayable format
5. **Download** - User can download the high-quality result

---

## 📊 Performance

- **Processing Time** - 2-15 seconds per image (depends on image size and GPU)
- **Output Quality** - 4x resolution enhancement
- **Memory Usage** - ~2GB for GPU, variable on CPU
- **Supported Image Sizes** - Up to 1024x1024 pixels

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **EDSR Model** - Enhanced Deep Super-Resolution research
- **Streamlit** - For the amazing web framework
- **PyTorch** - Deep learning framework
- **OpenAI/Research Community** - For advancing image processing research

---

## 👤 Author

**Akshatha RK**
- GitHub: [@AkshathaaRk](https://github.com/AkshathaaRk)
- Email: Contact via GitHub profile

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Report bugs
2. Suggest new features
3. Submit pull requests
4. Improve documentation

---

## 📞 Support

For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include error messages and system details

---

**Made with ❤️ for image enhancement enthusiasts**
