# VideoView website
Premium dark-navy and teal static website for **VideoView 1.1.0 (Windows x64 release candidate)**.

## Live site (after GitHub Pages activation)
https://premangshumal-cyber.github.io/VideoView-Website/

## Included
- Home, Features, Downloads, Release Notes, and Privacy & Licenses HTML pages
- Responsive CSS and plain JavaScript, no build tools or dependencies
- SVG brand mark and original landscape illustration (concept art, not a real product screenshot)
- SHA-256 checksum list, test reports, Windows test checklist and release notes

## Software installers — published pre-release

The software packages are hosted as **GitHub Release assets**, not regular git repository files. These direct-download links are configured in `assets/js/download-config.js`:

- [VideoView Windows installer](https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/VideoView-Setup.exe)
- [VideoView Portable ZIP](https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/VideoView-Portable.zip)
- [VideoView application source ZIP](https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/VideoView-Source.zip)
- [VideoView third-party source ZIP](https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/VideoView-ThirdPartySources.zip)

GitHub confirmed the v1.1.0 pre-release is public and these four assets were uploaded; their file sizes match those in the local release notes. Checksums, QA report, and Windows test checklist are available from the website's local `downloads/` directory, not GitHub Releases. Confirm the checksum of each downloaded binary before use.

## Enable GitHub Pages
Repository → **Settings** → **Pages** → Build and deployment → **Deploy from a branch** → Branch **main**, folder **/(root)** → Save.

Expected URL: https://premangshumal-cyber.github.io/VideoView-Website/

This is a project website, not the Windows software itself. **Native Windows startup/playback and installation tests have not yet been completed**, per the QA report. Do not call this a stable/verified release without completing the Windows test checklist.

See [deployment guide](DEPLOYMENT_GUIDE.md) for alternate hosts and website deployment.
