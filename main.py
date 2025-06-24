import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import time
import requests
import json
import os

# Copyright holder of UXCopyCheck AI Tool is Vinay Bhagat (June, 2025).

print("Copyright Notice: Copyright© 2025 Vinay Bhagat.")

OLLAMA_API_BASE_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma:2b" # CHANGE THIS LINE to a smaller, faster model

app = FastAPI(
    title="UXCopyCheck AI Tool",
    description="Lifetime free automated UX Copy Audits powered by your private local AI tool."
)

templates_dir = "templates"
if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)
with open(os.path.join(templates_dir, "index.html"), "w") as f:
    f.write("<!-- Placeholder for index.html -->")
templates = Jinja2Templates(directory=templates_dir)


# print("Script started.")
# start_overall = time.time()

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UXCopyCheck AI Tool (MVP)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f2f5;
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 30px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }
        textarea, input[type="text"] {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px;
            width: 100%;
            box-sizing: border-box;
            font-size: 1rem;
            transition: border-color 0.2s;
        }
        textarea:focus, input[type="text"]:focus {
            outline: none;
            border-color: #6366f1;
        }
        button {
            background-color: #6366f1;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s, transform 0.1s;
            box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
        }
        button:hover {
            background-color: #4f46e5;
            transform: translateY(-1px);
        }
        .loading-indicator {
            display: none;
            text-align: center;
            margin-top: 20px;
            font-weight: 500;
            color: #4a5568;
        }
        .error-message {
            color: #ef4444;
            font-weight: 500;
            margin-top: 20px;
            padding: 15px;
            background-color: #fef2f2;
            border: 1px solid #f87171;
            border-radius: 8px;
        }
        .audit-report {
            margin-top: 30px;
            background-color: #f9fafb;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 20px;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        .audit-report h3 {
            font-size: 1.25rem;
            font-weight: 700;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            color: #312e81;
        }
        .audit-report strong {
            color: #374151;
        }
    </style>
</head>
<body class="p-4">
    <div class="container">
        <h1 class="text-3xl font-bold text-center text-indigo-800 mb-6">✍️ UXCopyCheck AI Tool (MVP)</h1>
        <p class="text-center text-gray-600 mb-8">Audit your UX Copy free for lifetime on your private local AI tool.</p>

        <div class="mb-6">
            <label for="uxCopyInput" class="block text-gray-700 text-sm font-semibold mb-2">1. Paste Your UX Copy:</label>
            <textarea id="uxCopyInput" rows="10" class="focus:border-indigo-500 transition-colors duration-200" placeholder="Enter here your UX copy to audit and improve."></textarea>
        </div>

        <div class="mb-8">
            <label for="desiredToneInput" class="block text-gray-700 text-sm font-semibold mb-2">2. Specify desired tone for your UX Copy:</label>
            <input type="text" id="desiredToneInput" class="focus:border-indigo-500 transition-colors duration-200" value="friendly and direct" placeholder="e.g., 'friendly and direct', 'formal and professional', 'empathetic'">
        </div>

        <button id="auditButton" class="w-full">Improve my UX Copy!</button>

        <div id="loadingIndicator" class="loading-indicator">
            Auditing your UX copy... Audit report generation time might vary based on your computer (if you run it on a CPU or a GPU) and hardware where you run this UXCopyCheck AI tool.
        </div>
        <div id="errorMessage" class="error-message hidden"></div>

        <div id="auditReport" class="audit-report hidden">
        </div>
    </div>

    <script>
        const auditButton = document.getElementById('auditButton');
        const uxCopyInput = document.getElementById('uxCopyInput');
        const desiredToneInput = document.getElementById('desiredToneInput');
        const loadingIndicator = document.getElementById('loadingIndicator');
        const errorMessage = document.getElementById('errorMessage');
        const auditReport = document.getElementById('auditReport');

        auditButton.addEventListener('click', async () => {
            const inputText = uxCopyInput.value.trim();
            const desiredTone = desiredToneInput.value.trim();

            errorMessage.classList.add('hidden');
            auditReport.classList.add('hidden');
            auditReport.innerHTML = '';

            if (!inputText) {
                errorMessage.textContent = "Please paste some UX copy to audit.";
                errorMessage.classList.remove('hidden');
                return;
            }

            loadingIndicator.style.display = 'block';
            auditButton.disabled = true;

            try {
                const response = await fetch('/audit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        input_text: inputText,
                        desired_tone: desiredTone
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || `HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                auditReport.innerHTML = data.report_markdown;
                auditReport.classList.remove('hidden');

            } catch (error) {
                console.error("Audit failed:", error);
                errorMessage.textContent = `Audit failed: ${error.message}`;
                errorMessage.classList.remove('hidden');
            } finally {
                loadingIndicator.style.display = 'none';
                auditButton.disabled = false;
            }
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    print(f"Serving HTML page. Overall startup took {time.time() - start_overall:.2f} seconds")
    return HTMLResponse(content=HTML_CONTENT)

class AuditRequest(BaseModel):
    input_text: str
    desired_tone: str

@app.post("/audit")
async def audit_copy_endpoint(request_data: AuditRequest):
    start_request_processing = time.time()
    input_text = request_data.input_text
    desired_tone = request_data.desired_tone

    print("Received audit request.")
    print(f"Your UX copy (first 50 chars): {input_text[:50]}...")
    print(f"Selected Tone: {desired_tone}")
    start_time_section = time.time()

    rag_context = ""

    print(f"Setting up style guides & knowledge bases. It took {time.time() - start_time_section:.2f} seconds")


    start_time_section_prompt = time.time()
    llm_prompt = f"""
    **System Role:** You are an expert UX writer and a meticulous AI auditor for the UXCopyCheck AI tool. Your primary goal is to provide precise, actionable feedback on UI text to improve user experience.

    **Task:** Analyze the provided `input_text` based on the following critical UX writing principles, tailored for the desired tone.

    ---

    **1. Clarity and Conciseness Audit:**
    * **Evaluate:** Is the copy free from jargon, ambiguity, and unnecessary words? Is it direct and easy for an average user to understand at a glance?
    * **Identify:** Wordiness, complex sentence structures, vague terms, or confusing phrasing.

    **2. Tone and Voice Consistency Audit:**
    * **Evaluate:** Does the copy consistently align with a '{desired_tone}' tone?
    * **Identify:** Deviations from the specified tone (e.g., too formal, too casual, robotic, overly aggressive, lacking empathy).

    **3. Actionability and Usability Audit:**
    * **Evaluate:** Is the Call-to-Action (CTA) clear, compelling, and unambiguous? Does the copy clearly guide the user towards their next intended action?
    * **Identify:** Passive CTAs, vague instructions, or a lack of clear direction.

    ---

    **Output Instructions:**

    * Provide your analysis in a structured Markdown format.
    * Start with an "Overall Assessment" summarizing the general quality.
    * Then, for each specific issue found, create a separate section using the exact format below.
    * If a category (Clarity, Tone, Actionability) has no significant issues, explicitly state "No significant issues found for [Category]." for that section.

    ---

    **Overall Assessment:**
    [Your overall summary of the copy's strengths and weaknesses across all categories.]

    ---

    **Detailed Audit Findings:**

    ### Issue: [Clarity/Conciseness/Tone/Actionability]
    **Original Copy:** "{input_text}"
    **Analysis:** "[Concise explanation of the specific issue identified by the AI. Be descriptive (e.g., 'The phrase uses technical jargon that may confuse new users.').]"
    **Suggested Revision:** "[Your concise, improved copy suggestion. Provide a single, best alternative.]"
    **Rationale:** "[Brief reason for the suggestion (e.g., 'Simplifies complex terminology to improve comprehension,' 'Aligns copy with the specified empathetic brand tone,' 'Makes the user's next step explicit and encourages interaction.').]"

    ---

    **Input Text for Analysis:**
    {input_text}

    **Desired Tone:**
    {desired_tone}

    {rag_context}
    """
    print(f"Prompt preparation took {time.time() - start_time_section_prompt:.2f} seconds")

    print("Making a call to LLM ...")
    start_time_section_llm_call = time.time()
    llm_response_content = "Error: Audit failed due to an internal server error."

    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": llm_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_API_BASE_URL, json=payload)
        response.raise_for_status()
        llm_response_content = response.json()["response"]
        print(f"LLM call took {time.time() - start_time_section_llm_call:.2f} seconds")
        print(f"Summarized suggestions to improve your UX Copy (first 500 chars):\n{llm_response_content[:500]}...")

    except requests.exceptions.ConnectionError:
        error_msg = "ERROR: Could not connect to Ollama server. Please ensure `ollama serve` is running and accessible at `http://localhost:11434`."
        print(error_msg)
        return {"report_markdown": f"<div class='error-message'>{error_msg}</div>", "detail": error_msg}, 500
    except requests.exceptions.HTTPError as e:
        error_msg = f"ERROR: HTTP error from Ollama: {e.response.status_code} - {e.response.text}"
        print(error_msg)
        return {"report_markdown": f"<div class='error-message'>{error_msg}</div>", "detail": error_msg}, e.response.status_code
    except json.JSONDecodeError:
        error_msg = "ERROR: Failed to parse JSON response from Ollama. Check Ollama server logs for more details."
        print(error_msg)
        return {"report_markdown": f"<div class='error-message'>{error_msg}</div>", "detail": error_msg}, 500
    except Exception as e:
        error_msg = f"An unexpected error occurred during LLM call: {e}"
        print(error_msg)
        return {"report_markdown": f"<div class='error-message'>{error_msg}</div>", "detail": error_msg}, 500

    print(f"Total request processing time: {time.time() - start_request_processing:.2f} seconds")
    return {"report_markdown": llm_response_content}

if __name__ == "__main__":
    print("Attempting to start Uvicorn server...")
    uvicorn.run(app, host="0.0.0.0", port=8000) # Changed port to 8000

# Copyright© 2025 Vinay Bhagat 
# This file is part of UXCopyCheck AI Tool.
# UXCopyCheck AI Tool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# UXCopyCheck AI Tool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with UXCopyCheck AI Tool. If not, see <https://www.gnu.org/licenses/>.

