import sys
with open(r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace Footer
text = text.replace("&copy; 2026 AMR Project - Antimicrobial Resistance. All rights reserved.", "&copy; 2026 Projeto de Biorremediação. All rights reserved.")
text = text.replace("<h3>Managers - National Focal Groups</h3>", "<h3>Membros Pesquisadores</h3>")

start_team = text.find("                    <!-- Row 1 -->")
end_delete = text.find("    <!-- Sponsors Section -->")

new_team = """                    <div class="team-member">
                        <img src="images/prof-Vania.jpeg" alt="Prof. V. A. Vicente" class="member-photo" loading="lazy">
                        <h4>Prof. Dra. Vania Aparecida Vicente</h4>
                        <p>Coordinator</p>
                    </div>
                    
                    <div class="team-member">
                        <img src="images/Walter.gif" alt="Walter Antonio Pereira Boeger" class="member-photo" loading="lazy">
                        <h4>Walter Antonio Pereira Boeger</h4>
                        <p>Oceanologist, Doctorate in Zoology<br>Collections of Microorganisms, Laboratory of Biological Interactions – UFPR</p>
                    </div>
                    
                    <div class="team-member">
                        <img src="images/Dra. Derlene Attili de Angelis.png" alt="Derlene Attili de Angelis" class="member-photo" loading="lazy">
                        <h4>Derlene Attili de Angelis</h4>
                        <p>Biologist, PhD in Biological Sciences (Plant Biology)<br>Curator of the Brazilian Collection of Environmental and Industrial Microorganisms – CBMAI/UNICAMP</p>
                    </div>
                    
                    <div class="team-member">
                        <img src="images/Dra. Valéria Maia de Oliveira.jpeg" alt="Valéria Maia de Oliveira" class="member-photo" loading="lazy">
                        <h4>Valéria Maia de Oliveira</h4>
                        <p>Bióloga, Doutora em Genética de Microrganismos e Biologia Molecular (IB/UNICAMP). Pesquisadora da DRM.</p>
                    </div>
                    
                    <div class="team-member">
                        <img src="images/MARLON.avif" alt="Dr. Marlon Roger Geraldo" class="member-photo" loading="lazy">
                        <h4>Dr. Marlon Roger Geraldo</h4>
                        <p>Biologist, Doctor in Microbiology, Parasitology and Pathology</p>
                    </div>
                </div>
            </div>

"""

if start_team != -1 and end_delete != -1:
    text = text[:start_team] + new_team + text[end_delete:]
else:
    print("Could not find start or end tags")

with open(r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("success")
