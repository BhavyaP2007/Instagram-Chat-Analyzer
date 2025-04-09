# 📦 Instagram Chat Analyzer using Streamlit

This is a Streamlit-based tool designed to analyze **Instagram message exports** and detect potentially inappropriate or suspicious content in chats — including messages, photos, and videos.

> 🧠 _A side project that took my blood, sweat, and lots of debugging — but here it is._

---

## 🚀 Features

- Upload your Instagram message JSON files (as ZIP)
- Automatically extracts and analyzes messages
- Flags suspicious messages, photos, and videos
- Categorizes and displays results clearly
- Stores output as CSV files in a folder
- Allows you to open result folders from the GUI

## Requirements
-pandas
-os
-json
-pathlib
-cv2
-nudenet
-detoxify
-zipfile
-tempfile
-streamlit

🧩 Limitations
1. Currently handles only one ZIP file at a time
2. Loading and analysis may take time on large files
3. No real-time progress bar (yet!)
4. Doesn't yet allow batch uploads

🎯 Future Improvements
1. Handle multiple ZIP uploads
2. Optimize file processing speed
3. Add real-time progress feedback
4. Add visual previews for flagged media
5. Use the program to detect potential threats, crimes, cyberbullying.
