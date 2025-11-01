# Covert Audio Listener & Exfiltration PoC

This project is a proof-of-concept demonstrating the inherent security and privacy risks of applications that request microphone access. While it functions as a simple voice assistant, its core mechanism relies on capturing ambient audio and sending it to external Google servers for transcription, posing a significant data exfiltration risk.

This script is intended for **educational and security awareness purposes only**.

---

## ⚠️ SECURITY WARNING: This is a Privacy Risk

This script is **NOT** a secure, sandboxed assistant. It is a demonstration of a data leak.

* **Audio Exfiltration:** The `listen()` function captures audio directly from your microphone (`sr.Microphone()`).
* **Third-Party Processing:** This captured audio data is then sent over the internet to Google's servers using the `r.recognize_google(audio)` method for speech-to-text (STT) conversion.
* **Lack of Transparency:** The user is given no indication that their voice data is leaving their local machine. A malicious actor could easily modify this script to record and transmit *all* ambient audio, not just command triggers.

This tool demonstrates why it is critical to vet the permissions and source code of any application that requests access to sensitive hardware like a microphone or camera.

---

## 🔬 How the "Attack" Works

1.  **Listen (`sr.Microphone()`):** The script continuously listens to the microphone input.
2.  **Exfiltrate (`r.recognize_google()`):** Instead of processing speech locally (which is resource-intensive), the script sends the raw audio file to Google's API.
3.  **Transcribe:** Google's servers process the audio, transcribe it into text, and send that text back.
4.  **Execute:** The script parses the returned text for commands (e.g., "play," "search," "time").

The vulnerability is the unauthenticated and non-transparent data transmission in step 2.

---

## 🚀 Setup & Installation

**Note:** Running this script requires you to grant it microphone access. Proceed with caution.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install Dependencies:**
    This script requires several Python libraries. `PyAudio` is a necessary dependency for `SpeechRecognition` to access the microphone.

    ```bash
    # Install the core libraries
    pip install SpeechRecognition
    pip install pyttsx3
    pip install wikipedia
    pip install pywhatkit
    
    # This is required for microphone access
    pip install PyAudio
    ```
    *Note: `PyAudio` installation can sometimes fail on Windows/macOS. You may need to install it using a pre-compiled wheel or via a package manager like `brew` or `apt`.*

---

## 💻 How to Run the Demo

1.  Ensure you have a working microphone connected.
2.  Run the script from your terminal:
    ```bash
    python python.py
    ```
3.  The assistant will greet you.
4.  Try speaking a command, such as:
    * "what time is it"
    * "play knocking on heaven's door"
    * "search for python cybersecurity"
    * "wikipedia for the CIA"
    * "exit"

While you do this, consider that the raw audio for each command was sent to and processed by an external entity.

---

## ⚖️ License

This project is open-source and available under the [MIT License](LICENSE).
