!pip install wikipedia-api pydantic --quiet

from pydantic import BaseModel
import wikipediaapi
import re

class InstitutionDetails(BaseModel):
    founder: str = "N/A"
    founded: str = "N/A"
    summary: str

def get_details(name):
    page = wikipediaapi.Wikipedia("App/1.0", "en").page(name)
    if not page.exists(): return "Not Found"
    
    yr = re.search(r"\b(18|19|20)\d{2}\b", page.text)
    fndr = re.search(r"founded by ([A-Z][a-zA-Z\s]+)", page.text, re.IGNORECASE)
    
    return InstitutionDetails(
        founder=fndr.group(1) if fndr else "N/A",
        founded=yr.group() if yr else "N/A",
        summary=page.summary[:150] + "..."
    )

print(get_details(input("Enter Institution: ")))
