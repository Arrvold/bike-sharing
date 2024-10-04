Analysis Project

A data analysis project focusing on creating an interactive dashboard to analyze and visualize bike sharing data patterns and trends
Overview

This repository contains code for a Streamlit-based dashboard that allows users to explore bike sharing data patterns. The live version of the dashboard can be accessed at [Streamlit.app](https://bike-share-fika.streamlit.app/).

> **Note**: The repository is primarily used for deploying the Streamlit app. If running locally, you'll need to modify the data directory paths in the code. The complete runnable code for local execution is included in the Dicoding project submission zip file.

## Dataset

# Dicoding Collection Dashboard 
The analysis uses the Bike Sharing Dataset, which can be found on Kaggle:
[Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

## Setup Environment

### Prerequisites
- Visual Studio Code (or any preferred code editor)
- Python 3.x

### Required Libraries
Install the following Python libraries by running this command in your terminal (administrator privileges recommended):

```bash
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```

## Installation Guide

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/taufika94/bike-share.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bike-sharing-py
   ```

3. Enter the dashboard directory:
   ```bash
   cd dashboard
   ```
4. Setup Environment - Anaconda
   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds
   pip install -r requirements.txt
   ```

5. Launch the Streamlit application:
   ```bash
   streamlit run dashboard.py
   ```

6. To stop the application, use:
   ```bash
   ctrl + c
   ```

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs found or improvements suggested.

## License

This project is open source and available under the [MIT License](LICENSE).
