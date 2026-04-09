import sys

path = r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

start_tag = "    <!-- Team -->"
end_tag = "    <!-- Sponsors Section -->"

idx_start = text.find(start_tag)
idx_end = text.find(end_tag)

if idx_start != -1 and idx_end != -1:
    new_team_section = """    <!-- Team -->
    <section id="team" class="team">
        <div class="container">
            <div class="section-header">
                <h2>Executing Team</h2>
                <div class="header-line"></div>
            </div>

            <!-- National Managers -->
            <div class="team-section">
                <h3>Managers - National Focal Groups</h3>
                <div class="team-grid-national">
                    <div class="team-member">
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
                        <p>Biologist, PhD in Genetics of Microorganisms and Molecular Biology (IB/UNICAMP). Researcher at DRM.</p>
                    </div>
                    
                    <div class="team-member">
                        <img src="images/MARLON.avif" alt="Dr. Marlon Roger Geraldo" class="member-photo" loading="lazy">
                        <h4>Dr. Marlon Roger Geraldo</h4>
                        <p>Biologist, Doctor in Microbiology, Parasitology and Pathology</p>
                    </div>

                    <div class="team-member">
                        <img src="images/jessica.jpg" alt="Jessica" class="member-photo" loading="lazy">
                        <h4>Jessica</h4>
                        <p>CNPq Industrial Technological Development Fellow</p>
                    </div>

                    <div class="team-member">
                        <img src="images/marcelo.jpg" alt="Marcelo Acacio Chammas" class="member-photo" loading="lazy">
                        <h4>Marcelo Acacio Chammas</h4>
                        <p>Technical Manager at Aquatrix Consulting and Projects</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

    # We also need to remove Marcelo from his incorrect location (which was around Objectives)
    # The string to remove:
    marcelo_incorrect = """                    <div class="team-member">
                        <img src="images/marcelo.jpg" alt="Marcelo Acacio Chammas" class="member-photo" loading="lazy">
                        <h4>Marcelo Acacio Chammas</h4>
                        <p>Technical Manager at Aquatrix Consulting and Projects</p>
                    </div>\n"""
                    
    # Only replace before Team section
    before_team = text[:idx_start]
    after_team = text[idx_end:]
    
    before_team = before_team.replace(marcelo_incorrect, "")
    
    text = before_team + new_team_section + after_team

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done")
else:
    print("Tags not found.")
