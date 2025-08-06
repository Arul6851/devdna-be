# DevDNA Backend and Agents

# Introduction

This is the main backend used to serve the requests of the DevDNA Project which is an AI powered Project Management Tool which also gives insights about developers.

# Docker Files for Clenz

## Setup

1. **Clone the Repository Locally**

   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create .env file**

   - Create a .env file inside the root directory by following the .env.sample format.

3. **Download Postgres - either as container or server**

   - For container, download the image and run using docker run command with necessary env variables.
   - For server, set the necesarry varibles and use in the .env file.

4. **Install the required packages**
   - Run:
     ```sh
     pip install -r requirements.txt
     ```
5. **Run the server**
   - Run:
     ```sh
     python main.py
     ```
