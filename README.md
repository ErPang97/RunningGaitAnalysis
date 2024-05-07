# RunningGaitAnalysis


## **Running Gait YOLOv8 Analyzer**


## **Overview**

**Project Summary**
 
 Have you been experiencing pains and injuries after starting your new hobby
 in running? Perhaps, you're feeling some pain in your legs, or ankles, etc.
 Aside from strength training, one thing you should do is get your gait
 analyzed. However, a full gait analysis isn't cheap and may not be always 
 necessary. Our project here aims to help give quick, accessible advice to runners, 
 providing feedback on the deviation of their arms from the ideal 90 degree angle,
 the difference between stride length of their left and right foot, the 
 deviation of their back leg from the ideal 180 degree angle, and the cadence
 of the runner. You, the user, can simply upload a short video of you running, and
 you will receive feedback in a matter of moments. 

 TODO:
 Include the link to your Devpost project page here: 
 (https://mosa-spring-hackathon-2024.devpost.com/)

**Authors**

- Ryan Lim Pangilinan - ryanpang – ryanpang@seas.upenn.edu - [GitHub](https://github.com/ErPang97)
- Samuel Lee - leesamuel423 – samlee1@seas.upenn.edu - [GitHub](https://github.com/leesamuel423)
- Cara Ma - cteoong – cteoong@seas.upenn.edu - [GitHub](https://github.com/carateoong)
- Katherine Zhang - zhkat – zhkat@seas.upenn.edu - [GitHub](https://github.com/zhkat)


## **Usage**

The user can get their running gait analzyed my uploading a video of themselves running, and the application will display to the user information on the deviation of their arms from the ideal 90 degree angle,
the difference between stride length of their left and right foot, the 
deviation of their back leg from the ideal 180 degree angle, and the cadence
of the runner.

### **Prerequisites** 

Ensure you have Python 3.8+ and pip installed on your system. Additionally,
ensure you have Node.js installed.

### **Installation**

Follow these steps to install:

1. Clone the project repository:

```bash
git clone https://github.com/ErPang97/RunningGaitAnalysis
cd RunningGaitAnalysis
```

#### Backend Server
2. Make the backend your working directory:
```bash
cd backend
```

3. Create a virtual environment. A virtual environment is recommended to keep dependencies required by the project separate and to avoid conflicts with other projects.

```bash
# For Unix or MacOS
python3 -m venv venv

# For Windows
python -m venv venv
```

4. Activate the virtual environment:

```bash
# For Unix or MacOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

5. Install required python packages specified in the requirements.txt file:

```bash
pip install -r requirements.txt
```

6. Run your flask backend server:
```bash
flask run
```

#### Frontend Client
7. Make the frontend your working directory:
```bash
cd frontend
```

8. Install required node packages:
```bash
npm i
```

9. Run the frontend:
```bash
npm run dev
```

## **Additional information**

### **Tools used**

YOLOv8, Python, Flask, TypeScript, JavaScript, React, HTML, CSS

## **Acknowledgments**

Thank you to MCIT for imparting valuable knowledge on us. Thank you to MOSA for hosting this hackathon. 

## MIT License
Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
