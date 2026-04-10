import sys

path = r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Change header back to what user requested + english
text = text.replace("<h3>Research Members</h3>", "<h3>Managers - National Focal Groups</h3>")

# HTML to append into team-grid-national (just before the closing </div> of team-grid-national)
new_national = """
                    <div class="team-member">
                        <img src="images/jessica.jpg" alt="Jessica" class="member-photo" loading="lazy">
                        <h4>Jessica</h4>
                        <p>CNPq Industrial Technological Development Fellow</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-terezinha.jpeg" alt="Prof. Terezinha I. E. Svidzinski" class="member-photo" loading="lazy">
                        <h4>Prof. Terezinha I. E. Svidzinski</h4>
                        <p>CMRP/Taxonline-UEM/PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/Prof_Juliana.jpeg" alt="Prof. Juliana V. M. Bittencourt" class="member-photo" loading="lazy">
                        <h4>Prof. Juliana V. M. Bittencourt</h4>
                        <p>CMRP/Taxonline-UTFPR/PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Matsuura.jpeg" alt="Prof. A.B. J. Matsuura" class="member-photo" loading="lazy">
                        <h4>Prof. A.B. J. Matsuura</h4>
                        <p>Fiocruz Amazônia AM</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Marcia.jpeg" alt="Prof. Marcia S. C. Melhem" class="member-photo" loading="lazy">
                        <h4>Prof. Marcia S. C. Melhem</h4>
                        <p>UFMS - MS</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Emanuel.jpeg" alt="Prof. Emanuel M. de Souza" class="member-photo" loading="lazy">
                        <h4>Prof. Emanuel M. de Souza</h4>
                        <p>UFPR - PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Cristina.jpeg" alt="Prof. Cristina M. S. Motta" class="member-photo" loading="lazy">
                        <h4>Prof. Cristina M. S. Motta</h4>
                        <p>URM-UFPE - PE</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Conceicao.jpeg" alt="Prof. Conceição M. P. S. de Azevedo" class="member-photo" loading="lazy">
                        <h4>Prof. Conceição M. P. S. de Azevedo</h4>
                        <p>UFMA - MA</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Libera.jpeg" alt="Prof. Líbera M. Dalla Costa" class="member-photo" loading="lazy">
                        <h4>Prof. Líbera M. Dalla Costa</h4>
                        <p>IPP-PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Arnaldo.jpeg" alt="Prof. Arnaldo L. Colombo" class="member-photo" loading="lazy">
                        <h4>Prof. Arnaldo L. Colombo</h4>
                        <p>UNIFESP - SP</p>
                    </div>
                    <div class="team-member">
                        <img src="images/dra-Gloria.jpeg" alt="Dra. M. Glória S. Stafocker" class="member-photo" loading="lazy">
                        <h4>Dra. M. Glória S. Stafocker</h4>
                        <p>MT-USP/SP</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Flavio.png" alt="Prof. Flávio Queiroz-Telles" class="member-photo" loading="lazy">
                        <h4>Prof. Flávio Queiroz-Telles</h4>
                        <p>CHC-UFPR - PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Rafaella.jpeg" alt="Prof. Rafaella C. B. Santos" class="member-photo" loading="lazy">
                        <h4>Prof. Rafaella C. B. Santos</h4>
                        <p>UNILA - PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Keite.jpeg" alt="Prof. Keite Nogueira" class="member-photo" loading="lazy">
                        <h4>Prof. Keite Nogueira</h4>
                        <p>CHC-UFPR - PR</p>
                    </div>
                    <div class="team-member">
                        <img src="images/prof-Vanete.jpeg" alt="Prof. Vanete Thomaz-Soccol" class="member-photo" loading="lazy">
                        <h4>Prof. Vanete Thomaz-Soccol</h4>
                        <p>UFPR / PR - Parasitological Collection</p>
                    </div>
"""

new_international = """
            </div>

            <!-- International Partners -->
            <div class="team-section" style="margin-top: 50px;">
                <h3>International Partnership</h3>
                <div class="team-grid-international">
                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Sybren.jpeg" alt="Prof. Sybren de Hoog" class="member-photo" loading="lazy">
                            <h4>Prof. Sybren de Hoog</h4>
                            <p>Radboud University Netherlands</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/Radboud.png" alt="RadboudUMC Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>

                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Eelco.jpeg" alt="Prof. Eelco Meijer" class="member-photo" loading="lazy">
                            <h4>Prof. Eelco Meijer</h4>
                            <p>CWZ/RadboudUMC Netherlands</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/cyyz.png" alt="CWZ Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>

                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Amir.png" alt="Prof. Amir Seyedmousavi" class="member-photo" loading="lazy">
                            <h4>Prof. Amir Seyedmousavi</h4>
                            <p>NIH USA</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/nih.png" alt="NIH Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>

                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Nina.jpeg" alt="Prof. Nina Gunde-Cimerman" class="member-photo" loading="lazy">
                            <h4>Prof. Nina Gunde-Cimerman</h4>
                            <p>Ljubljana University Slovenia</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/university-Slovenia.png" alt="Ljubljana Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>

                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Laura.jpeg" alt="Prof. Laura Selbmann" class="member-photo" loading="lazy">
                            <h4>Prof. Laura Selbmann</h4>
                            <p>Tuscia University Italy</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/tuscia.png" alt="Tuscia Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>

                    <div class="international-member">
                        <div class="member-with-logo">
                            <img src="images/prof-Yinggai.jpeg" alt="Prof. Yinggai Song" class="member-photo" loading="lazy">
                            <h4>Prof. Yinggai Song</h4>
                            <p>Peking University China</p>
                        </div>
                        <div class="institution-logo">
                            <img src="images/peking.png" alt="Peking Logo" class="logo-img" loading="lazy">
                        </div>
                    </div>
                </div>
"""

# The HTML currently looks like:
#                    </div>
#                </div>
#            </div>
#
#    <!-- Sponsors Section -->
# Since I only want to append into the existing grid, I'll find the line before <!-- Sponsors Section -->
# Actually it's safer to find "    <!-- Sponsors Section -->"
target = "    <!-- Sponsors Section -->"
idx_sponsors = text.find(target)

if idx_sponsors != -1:
    # </div>\n            </div>\n are right before this. Let's find "</div>\n            </div>\n"
    # Actually, we can just replace the team-grid end.
    idx = text.rfind("                </div>\n            </div>\n", 0, idx_sponsors)
    if idx != -1:
        text = text[:idx] + new_national + new_international + text[idx:]
        
with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("done")
