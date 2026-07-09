# Whicker Family Homepage

This site is designed to be hosted on static hosting platforms like Cloudflare Pages, Netlify, or GitHub Pages.

## 🚀 Deployment Notes (Cloudflare Pages)

### Build Process
For optimal performance and proper asset handling within CI/CD environments:
1.  **Structure:** Keep all source files (`index.html`, `styles.css`) at the root of the project.
2.  **Build Command:** Cloudflare Pages should execute a minimal build script to copy the static assets into the deployment directory (e.g., 'dist').
    ```bash
    # Simple copy command for this current structure:
    cp index.html dist/
    cp styles.css dist/
    ```
3.  **Build Output Directory:** Set the Build Output Directory to `dist`.

### Customization Guidance
- **SEO/Metadata:** Update `<title>` and meta tags in `index.html` for search engine optimization.
- **Interactivity:** If adding complex interactivity (e.g., live maps, carousels), consider using a framework like basic Vanilla JS build steps which can be included via a dedicated `script.js` file.

## 🛠️ Local Development Workflow
- To run locally: Simply open `index.html` in the browser.
- Initial commit structure setup complete based on summer theme requirements.
