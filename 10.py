!pip install wikipedia-api pydantic --quiet

from pydantic import BaseModel
import wikipediaapi

class IPCResponse(BaseModel):
    section: str = "N/A"
    explanation: str

wiki = wikipediaapi.Wikipedia("IPC/1.0", "en")
ipc_text = wiki.page("Indian Penal Code").text.lower()

def ask_ipc(q):
    topics = {"theft": "378", "murder": "300", "cheating": "415"}
    for topic, sec in topics.items():
        if topic in q.lower():
            idx = ipc_text.find(f"section {sec}")
            snippet = ipc_text[idx:idx+150] if idx != -1 else f"Refer to IPC Section {sec}"
            return IPCResponse(section=sec, explanation=snippet)
    return IPCResponse(explanation="Topic not found. Ask about theft, murder, or cheating.")

print(ask_ipc(input("Ask about IPC: ")))
