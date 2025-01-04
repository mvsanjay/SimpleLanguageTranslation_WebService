# Simple_LanguageTranslation_WebService

## Project Overview
This project implements a **Language Translation Web Service** using a client-server architecture. It leverages Python sockets and threads for communication and integrates the Google Translate API for machine translation.  
The service allows users to translate text from one language to another by sending requests from the client to the server, which processes the translation and returns the result.

---

## Project Features
- **Server:** Listens for incoming connections, processes text translations, and sends responses.  
- **Client:** Sends text and target language details to the server and displays the translation.  
- **Multithreading:** Manages multiple client connections simultaneously.  
- **Google Translate Integration:** Uses the `googletrans` library for translations.  

---

## Requirements
- **Python 3.x**  
- **Googletrans Library** (`pip install googletrans`)  
- **Active Internet Connection**

---

## Usage
1. Start the server script on the desired host and port.  
2. Run the client script to connect to the server.  
3. Enter the text to translate and the target language code (e.g., `es` for Spanish, `fr` for French).  
4. View the translated text on the client.

---

## Sample Output

**Server:**  
Translation service is up and running on 127.0.0.1:8000...

**Client:**  
Enter text to be translated: Hello
Enter target language (default is 'en'): es
Waiting for response from server...
Translated Text: Hola

---

## Conclusion
This project demonstrates the implementation of a basic translation web service using sockets, threads, and a third-party API. It serves as a foundation for further enhancements such as improved performance, better scalability, and added features like support for additional languages or offline translation.

---

## References
- **Google Translate API:** [Google Translate API](https://github.com/ssut/py-googletrans)
- **GeeksforGeeks:** [GeeksforGeeks](https://www.geeksforgeeks.org/)
