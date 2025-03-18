# DA323: Multimodal Data Analysis and Learning 2.0
## Assignment-cum-Project-01 (Jan-May 2025, IIT Guwahati)

This project explores scalable data collection, multimodal analysis, and computational matching techniques across different data types: images, text, audio, and structured data. The tasks involve automated data collection, preprocessing, analysis, and documentation. The final goal is to demonstrate insights through well-structured code, visualizations, and findings.

## Tasks Overview

### 1. Scalable Data Collection
- **Image Dataset:**
  - Collected images for 20 categories (50 images per category) using automated scripts.
  - Stored metadata (image URL, filename, resolution) in a structured format.
  - Organized images into labeled folders.
- **Text Dataset:**
  - Scraped text data from websites spanning 20 categories.
  - Processed text (cleaning, stop-word removal, formatting).
- **Audio Dataset:**
  - Recorded audio streams from public sources.
  - Extracted metadata and stored the dataset in WAV/MP3 format.
- **Weather Dataset:**
  - Collected real-time and historical weather data for 20 Indian cities.
  - Stored temperature, humidity, wind speed, and other parameters in CSV format.

### 2. Search for a Match
- Analyzed 45 muted video clips and 45 corresponding audio files.
- Designed an approach to match each audio with its corresponding silent video.
- Submitted the final matches in a structured CSV format.

### 3. Flags and Anthems Analysis
- **Flags:** Extracted color features from images of 100+ national flags and performed visual analysis.
- **Anthem Texts:** Pre-processed and analyzed linguistic patterns in national anthems.
- **Anthem Audio:** Conducted feature extraction and examined musical properties.
- **Multimodal Correlation:** Explored relationships between flag colors, anthem lyrics, and musical features.

## Repository Structure
```
DA323_Project/
├── data/
│   ├── images/
│   ├── text/
│   ├── audio/
│   ├── weather/
├── search_match/
├── flags_anthems/
├── notebooks/
└── results/
```

## How to Run
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run Jupyter notebooks in `notebooks/` for each analysis task.
4. Review generated visualizations and results in `results/`.

## Summary
This project provides hands-on experience with scalable data collection, multimodal feature extraction, and correlation analysis across different data types. The structured workflow enables effective data-driven insights into real-world problems.
