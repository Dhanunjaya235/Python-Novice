# Python Novice Practice Repository

Welcome to the Python Novice Practice Repository! This repository is designed to help beginners practice and improve their Python programming skills.

## Getting Started

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/python-novice-practice.git
```

## Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

## Update Python and Pip Environment Variables in System

### **Windows**  
1. **Check Python Installation Path**  
   - Open Command Prompt and run:  
     ```sh
     where python
     ```  
   - Note the path (e.g., `C:\Python39\python.exe`).  

2. **Check Pip Installation Path**  
   - Run:  
     ```sh
     where pip
     ```  
   - Note the path (e.g., `C:\Python39\Scripts\pip.exe`).  

3. **Add Python and Pip to Environment Variables**  
   - Search for **"Environment Variables"** in Windows Search and open **"Edit the system environment variables"**.  
   - In the **System Properties** window, click **"Environment Variables"**.  
   - Under **System Variables**, find and select **Path**, then click **Edit**.  
   - Click **New** and add the following paths:  
     - `C:\Python39\` (Replace with your actual Python installation path)  
     - `C:\Python39\Scripts\`  
   - Click **OK** to save changes.  

4. **Verify Changes**  
   - Open a new Command Prompt and run:  
     ```sh
     python --version
     pip --version
     ```  
   - If the paths are set correctly, the commands should return their respective versions.  

### **Linux/Mac**  
1. **Find Python and Pip Paths**  
   - Run:  
     ```sh
     which python3
     which pip3
     ```

2. **Add Paths to Environment Variables**  
   - Open `.bashrc` (or `.zshrc` for macOS using Zsh) in an editor:  
     ```sh
     nano ~/.bashrc   # or nano ~/.zshrc
     ```  
   - Add the following lines at the end:  
     ```sh
     export PATH="$HOME/.local/bin:$PATH"
     export PATH="/usr/local/bin/python3:$PATH"
     ```  
   - Save and exit.  

3. **Apply Changes**  
   - Run:  
     ```sh
     source ~/.bashrc   # or source ~/.zshrc
     ```

4. **Verify Installation**  
   - Run:  
     ```sh
     python3 --version
     pip3 --version
     ```

## Setting Up a Virtual Environment in a Python Project

To create and use a virtual environment for your Python project, follow these steps:

### **Step 1: Install Virtual Environment (if not installed)**
Run the following command to install `venv` (if not already installed):
```sh
pip install virtualenv
```

### **Step 2: Create a Virtual Environment**
Navigate to your project directory and create a virtual environment using one of the following methods:
- Using `venv`:
  ```sh
  python -m venv venv_name
  ```
- Using `virtualenv`:
  ```sh
  virtualenv venv_name
  ```
Replace `venv_name` with your preferred environment name.

### **Step 3: Activate the Virtual Environment**
- **Windows**:
  ```sh
  venv_name\Scripts\activate
  ```
- **Linux/Mac**:
  ```sh
  source venv_name/bin/activate
  ```
- **Using Relative Path** (Applicable for both Windows and Linux/Mac):
  ```sh
  ./venv_name/Scripts/activate  # Windows
  ./venv_name/bin/activate      # Linux/Mac
  ```

### **Step 4: Install Dependencies**
Once the virtual environment is activated, install the required dependencies:
```sh
pip install -r requirements.txt
```

### **Step 5: Deactivate the Virtual Environment**
To exit the virtual environment, run:
```sh
deactivate
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Dhanunjaya Andavarapu** 
