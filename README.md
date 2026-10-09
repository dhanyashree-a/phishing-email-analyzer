# Phishing & Email Security Analyzer 🔐

A Python-based cybersecurity project that analyzes email messages and URLs for potential phishing indicators using **rule-based detection and weighted risk scoring**. The application provides a risk assessment through an interactive Streamlit interface.

## 📌 Project Overview

Phishing is a social engineering attack in which attackers impersonate trusted organizations or individuals to trick users into revealing sensitive information, clicking malicious links, or performing unsafe actions.

This project analyzes user-provided messages and identifies suspicious characteristics. It calculates a risk score based on detected indicators and classifies the message into one of three risk levels: **LOW, MEDIUM, or HIGH**.

> **Note:** This tool identifies potential phishing indicators. It does not conclusively determine whether a message or URL is malicious.

## ✨ Features

- **URL Extraction:** Extracts HTTP and HTTPS URLs from email messages.
- **Suspicious URL Analysis:** Identifies IP-based URLs and URLs using HTTP.
- **Brand Impersonation Detection:** Flags suspicious domain structures that may misuse trusted brand names.
- **Lookalike Domain Detection:** Identifies domains that resemble known brands, such as `paypa1-login.com`.
- **Urgency Detection:** Identifies pressure-inducing phrases such as "urgent" and "immediately."
- **Threat Detection:** Detects suspicious language involving account suspension, deletion, blocking, and other threats.
- **Credential Indicator Detection:** Identifies mentions of passwords, OTPs, PINs, usernames, and verification codes.
- **Weighted Risk Scoring:** Assigns scores to detected indicators and calculates an overall risk level.
- **Interactive Dashboard:** Displays risk scores, detected indicators, explanations, and recommendations using Streamlit.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **User Interface:** Streamlit
- **Text Pattern Matching:** Regular Expressions (`re`)
- **URL Analysis:** `urllib.parse`
- **IP Address Validation:** `ipaddress`
- **Lookalike Detection:** `difflib.SequenceMatcher`

The project uses Python's built-in libraries for much of the detection logic, with Streamlit providing the interactive interface.

## 🏗️ Project Architecture

```text
User Input
    |
    v
Streamlit Interface (app.py)
    |
    v
Message Analysis (analyzer.py)
    |
    +----------------------+
    |                      |
    v                      v
Text Analysis          URL Analysis
(text_analyzer.py)     (url_analyzer.py)
    |                      |
    +-----------+----------+
                |
                v
       Risk Scoring Engine
         (risk_engine.py)
                |
                v
         Risk Assessment
       LOW / MEDIUM / HIGH
                |
                v
      Results in Streamlit
```

### Project Structure

```text
phishing-email-analyzer/
│
├── app.py
├── analyzer.py
├── url_analyzer.py
├── text_analyzer.py
├── risk_engine.py
├── requirements.txt
├── README.md
│
└── tests/
    └── test_cases.txt
```

## ⚙️ How It Works

### 1. Message Input

The user enters an email message or text into the Streamlit interface.

### 2. Text Analysis

The analyzer searches for suspicious language, including:
- Urgency and time pressure
- Threatening statements
- Mentions of sensitive authentication information

Regular expressions are used to identify predefined patterns.

### 3. URL Analysis

URLs are extracted from the message and analyzed individually. The application examines URL components, validates whether a hostname is an IP address, checks the URL scheme, and applies basic heuristics to identify possible brand impersonation and lookalike domains.

### 4. Risk Scoring

The risk engine assigns predefined weights to detected indicators. Threat and credential findings have score caps to limit the effect of repeated detections.

| Indicator | Weight |
|---|---:|
| Urgency | +1 |
| Threat | +2 per finding, capped at +4 |
| Credential indicator | +2 per finding, capped at +4 |
| HTTP URL | +1 |
| IP-based URL | +2 |
| Possible brand impersonation | +3 |
| Possible lookalike domain | +3 |

The urgency category contributes its weight once, even if multiple urgency phrases are detected. URL indicator scores are added for each detected URL indicator.

### 5. Risk Classification

The final score is mapped to a risk category.

| Risk score | Classification |
|---|---|
| 0–2 | LOW |
| 3–5 | MEDIUM |
| 6 and above | HIGH |

These thresholds are predefined heuristics, not statistically validated probability estimates.

### 6. Results and Recommendations

The Streamlit interface displays the risk score, risk level, detected indicators, explanations, and safety recommendations.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.9 or later recommended
- pip package manager
- Git (for cloning the repository)

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/phishing-email-analyzer.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Navigate to the project directory

```bash
cd phishing-email-analyzer
```

### Step 3: Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL that you can open in your browser.

## 🧪 Example Test Case

**Input:**

```text
URGENT! Your account will be suspended unless you
verify your password immediately:
http://paypa1-login.com/verify
```

**Expected indicators:**
- Urgency / time-pressure
- Threat / fear language
- Credential indicator
- HTTP URL
- Possible lookalike domain

**Expected result:** HIGH risk.

The exact result depends on the indicators detected by the current implementation. This example illustrates the expected behavior, not a guarantee that every phishing message will be detected.

## 🔒 Security Considerations

- Do not enter real passwords, OTPs, private emails, or other sensitive information into a demonstration application.
- The tool performs rule-based analysis and does not verify the actual reputation or ownership of a domain.
- An HTTPS connection does not guarantee that a website is trustworthy.
- A LOW risk result does not guarantee that a message is safe.
- Suspicious URLs should not be opened merely to test the analyzer.

## ⚠️ Limitations

- Detection depends on predefined rules and keyword patterns.
- Legitimate messages may be flagged as suspicious (**false positives**).
- Sophisticated phishing attempts may not match existing rules (**false negatives**).
- The simplified domain-analysis heuristics may not correctly handle every complex domain structure.
- The risk score is a heuristic assessment, not a calibrated probability of phishing.
- The current version does not use machine learning, live threat-intelligence feeds, or email authentication validation.

## 🔮 Future Enhancements

- Improve domain parsing using a Public Suffix List-aware library.
- Refine credential and threat detection to reduce false positives.
- Evaluate detection performance using a labelled phishing-email dataset.
- Explore machine learning for phishing classification.
- Integrate reputable threat-intelligence feeds for URL reputation checks.
- Add email-header analysis and SPF, DKIM, and DMARC validation.
- Expand automated tests for benign messages, suspicious URLs, and edge cases.

## 📚 Key Learnings

Through this project, I explored:
- Basic phishing and social engineering indicators
- Regular expressions for text analysis
- URL parsing and IP address validation
- Domain impersonation and lookalike detection heuristics
- Rule-based algorithms and weighted risk scoring
- False positives, false negatives, and limitations of heuristic detection
- Building a cybersecurity analysis interface with Streamlit

## 👩‍💻 Author

**Dhanyashree A**

B.Tech – Computer Science and Engineering (Artificial Intelligence and Machine Learning)

GitHub: [https://github.com/dhanyashree-a]

---

*This project was developed for learning and educational purposes. It is a basic phishing-risk assessment prototype and should not be used as the sole basis for security decisions.*