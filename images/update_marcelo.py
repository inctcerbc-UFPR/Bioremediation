import sys

path = r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

marcelo = """                    <div class="team-member">
                        <img src="images/marcelo.jpg" alt="Marcelo Acacio Chammas" class="member-photo" loading="lazy">
                        <h4>Marcelo Acacio Chammas</h4>
                        <p>Technical Manager at Aquatrix Consulting and Projects</p>
                    </div>\n"""

target = "            <!-- International Partners -->"
idx_intl = text.find(target)

if idx_intl != -1:
    search_str = "                </div>\n            </div>\n"
    idx = text.rfind(search_str, 0, idx_intl)
    if idx != -1:
        text = text[:idx] + marcelo + text[idx:]
    else:
        print("search_str not found")
else:
    print("Target not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("Done")
