 UXCopyCheck AI Tool

Conduct lifetime free audits of your UX Copy powered by your private local AI tool.

Demo of UXCopyCheck AI Tool

https://github.com/user-attachments/assets/fb6bebc0-925a-46d4-bac9-c86902e23253


👋 About UXCopyCheck AI Tool

UXCopyCheck is an innovative, open-source desktop application that brings the power of Artificial Intelligence directly to your machine to audit and enhance your UX copy. Designed for UX writers, product managers, and designers, it helps you craft clear, consistent, and effective user interface text.

We believe in privacy, control, and cost-effectiveness. Unlike cloud-based AI tools, UXCopyCheck runs entirely locally, ensuring your sensitive content never leaves your environment and you incur zero recurring API costs.

 ✨ Key Features (MVP)

With UXCopyCheck, you can quickly analyze your UI text for:

 🔍 Clarity & Conciseness: Identify jargon, ambiguity, and unnecessary words. Get suggestions to simplify and make your copy instantly understandable.  
 🗣️ Tone & Voice Consistency: Ensure your message aligns perfectly with your brand's unique tone (you tell the AI what to aim for!).  
 🎯 Actionability & Usability: Optimize your Calls-to-Action (CTAs) and confirm your copy effectively guides users to their next step.

 🚀 Why UXCopyCheck?

 🔒 Unmatched Privacy: Your proprietary content and user data remain strictly on your local computer or private server. No data is sent to external cloud APIs for processing.  
 💰 Cost-Effective: Powered by free, open-source Large Language Models (LLMs) run via Ollama, eliminating expensive per-use API charges.  
 ⚙️ Full Control: Choose your preferred AI model, and in future versions, customize its behavior with your specific style guides and knowledge bases.  
 ⚡ Professional Grade: Get actionable, structured audit reports to elevate your UX writing quality.

 🛠️ Getting Started (Windows Setup Guide)

This guide will help you get UXCopyCheck AI Tool up and running on your Windows machine. A basic understanding of command-line tools is helpful, but we'll walk you through each step.

Important Notes:

 This is a local application. Internet is primarily needed for initial setup and model downloads.  
 Performance (how fast the AI responds) depends on your computer's hardware. While optimized for CPU, a dedicated NVIDIA GPU will offer significantly faster results.

 Prerequisites:

1.  Operating System: Windows 10 (64-bit) or later.  
2.  Processor (CPU): Intel Core i3 (11th Gen) or equivalent AMD Ryzen. More cores/higher clock speed helps.  
3.  Installed RAM: Minimum 16 GB (32 GB+ recommended for smoother experience).  
4.  Storage: Solid State Drive (SSD) with at least 10 GB free space.  
5.  Python: Version 3.9 or newer. Download from [python.org](https://www.python.org/downloads/windows/). During installation, make sure to check "Add Python to PATH".  
6.  Ollama: Download and install the Ollama desktop application from [ollama.com](https://ollama.com/downloads). This will manage your local AI models.

 Step-by-Step Installation:

1.  Open Command Prompt: Search for `cmd` in your Windows search bar and open it.

2.  Create a Project Folder:

      
    mkdir uxcopycheck-ai-tool  
    cd uxcopycheck-ai-tool  
    

3.  Download UXCopyCheck AI Tool:

     This project requires Git. If you don't have Git installed, download it from [git-scm.com](https://git-scm.com/download/win).  
     Clone the repository:

        git clone [https://github.com/vinaybhagatd/UXCopyCheck-AI-Tool.git](https://github.com/vinaybhagatd/UXCopyCheck-AI-Tool.git) .  
         (The '.' clones into the current directory)  
        

4.  Set Up Python Environment:

     Create a virtual environment (a clean space for your project's dependencies):

        python -m venv venv  
        

     Activate the virtual environment:

        .venv\Scripts\activate  
        

     Install necessary libraries:

        pip install fastapi uvicorn requests pydantic jinja2  
        

5.  Start Ollama Server:

     Open a NEW, SEPARATE Command Prompt window.  
     In this new window, run the Ollama server:

        ollama serve  
        

     You should see a message like `Listening on 127.0.0.1:11434`. Keep this window open.

6.  Download the AI Model:

     In the same separate Command Prompt window where `ollama serve` is running, download the recommended model:

        ollama run gemma:2b  
        

     This model is optimized for CPU performance. It might take a few minutes to download (1-2 GB). Wait for it to complete.

7.  Launch UXCopyCheck AI Tool:

     Go back to your first Command Prompt window (where your `venv` is active and you `cd`'d into `uxcopycheck-ai-tool`).  
     Run the UXCopyCheck application:

        uvicorn main:app --reload --port 8000  
        

     You'll see messages indicating the server has started.

8.  Access in Your Browser:

     Open your web browser (Chrome, Firefox, Edge, etc.).  
     Go to the address: `http://localhost:8000/`

    You should now see the UXCopyCheck AI Tool interface! Paste your copy, select your desired tone, and click "Audit My UX Copy." The audit results will appear directly on the page.

 💲 Monetization & Sustainability (Open Source)

UXCopyCheck AI Tool is and will remain completely open-source under the GNU Affero General Public License v3.0 (AGPLv3). This means the core code is freely available for anyone to use, inspect, modify, and distribute.

Our commitment to open source and privacy is sustainable through these high-value offerings:

 Professional Consulting & Support: Tailored setup, customization, integration, and ongoing support for individuals and teams.  
 Premium AI Model Weights: Access to specifically fine-tuned and optimized open-source LLM models curated by our experts for advanced UX writing tasks.  
 Curated Knowledge Bases: Pre-built, specialized RAG datasets (e.g., industry-specific style guides, compliance packs) to enhance AI accuracy.  
 Training & Workshops: In-depth courses and certifications on mastering UXCopyCheck and advanced AI-powered UX writing techniques.  
 Managed Deployments: For enterprises seeking full privacy but lacking internal expertise, we offer services to deploy and maintain UXCopyCheck on their private cloud infrastructure.

 🤝 Support & Community

 Having Trouble? Please check the console where `uvicorn` and `ollama serve` are running for `DEBUG` or `ERROR` messages. These often pinpoint issues.  
 Feedback & Contributions: We welcome your feedback, bug reports, and contributions! Please open an issue or pull request on this GitHub repository.  
 Connect with Us: Email ID: bhagatvinayd@gmail.com, LinkedIn: https://www.linkedin.com/in/vinay-b-79b831215

 📜 License

This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for the full text.  
