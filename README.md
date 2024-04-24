**## Installation**

To install the necessary dependencies, follow these steps:

**1. Install Node.js and Yarn:**

   - **Recommended:** Download and install the latest stable version of Node.js from the official website ([https://nodejs.org/en](https://nodejs.org/en)). The installer typically includes Yarn.
   ```bash
   npm install --global yarn
   ```

**2. Verify Installation:**

   - Open a terminal or command prompt.
   - Type `node -v` and `yarn -v` to check if Node.js and Yarn are installed correctly. You should see the installed versions.

**3. Install Frontend Dependencies (Yarn):**

   Once Node.js and Yarn are installed, proceed with the frontend setup as you described:

   ```bash
   yarn install
   ```

   ```bash
   yarn dev
   ```

**4. Install Backend Dependencies (Python):**

   The backend instructions remain the same:
   ```bash
   cd backend
   ```

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   python app.py
   ```

**4. Add .env file:**

   Create a `.env` file in the backend directory and add the following environment variables:

   ```bash
   GOOGLE_API_KEY = ""
   ```