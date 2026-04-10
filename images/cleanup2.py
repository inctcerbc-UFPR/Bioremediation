import sys

path = r"c:\Users\ruanj\OneDrive\Documentos\RAM-pages-main\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

start_tag = "    <!-- Sponsors Section -->"
end_tag = "    <!-- Contact -->"

idx_start = text.find(start_tag)
idx_end = text.find(end_tag)

if idx_start != -1 and idx_end != -1:
    new_sponsors_section = """    <!-- Sponsors Section -->
    <section id="sponsors" class="sponsors">
        <div class="container">
            <div class="section-header">
                <h2>Financial Support</h2>
                <div class="header-line"></div>
            </div>

            <h3 class="sponsors-subtitle">Financial Support</h3>
            <div class="sponsors-grid">
                <div class="sponsor-item">
                    <img src="images/1-sf-CNPq.png" alt="CNPq Logo" loading="lazy">
                </div>
            </div>
        </div>
    </section>

"""
    before = text[:idx_start]
    after = text[idx_end:]
    
    text = before + new_sponsors_section + after

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done")
else:
    print("Tags not found.")
