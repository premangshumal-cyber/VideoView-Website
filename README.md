# VideoView website
Premium dark-navy and teal static website for **VideoView 1.1.0 (Windows x64 release candidate)**.

## Live site (after GitHub Pages activation)
https://premangshumal-cyber.github.io/VideoView-Website/

## Included
- Home, Features, Downloads, Release Notes, and Privacy & Licenses HTML pages
- Responsive CSS and plain JavaScript, no build tools or dependencies
- SVG brand mark and original landscape illustration (concept art, not a real product screenshot)
- SHA-256 checksum list, test reports, Windows test checklist and release notes

## Software installers
The software packages (**VideoView-Setup.exe**, **VideoView-Portable.zip**, application source and third-party source ZIP) are **not in this git repository**. They are too large to publish here as ordinary website files, and have not yet been uploaded to GitHub Releases.

Until those assets are published, software download buttons open the [GitHub Releases page](https://github.com/premangshumal-cyber/VideoView-Website/releases). They **do not download the software yet**. Text documentation and checksums are in the \`downloads/\` folder and do work.

To enable direct downloads:
1. In this repository, create a GitHub Release tag **v1.1.0**, titled **VideoView 1.1.0 — Release Candidate**.
2. Upload the four software files with these exact filenames: \`VideoView-Setup.exe\`, \`VideoView-Portable.zip\`, \`VideoView-Source.zip\`, \`VideoView-ThirdPartySources.zip\`. The checksums in \`downloads/SHA256SUMS.txt\` should match the actual files.
3. Edit \`assets/js/download-config.js\`: set \`baseUrl\` to \`https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/\`.
4. Verify every download on the public site and compare SHA-256 checksums.

## Enable GitHub Pages
Repository → **Settings** → **Pages** → Build and deployment → **Deploy from a branch** → Branch **main**, folder **/(root)** → Save.

Expected URL: https://premangshumal-cyber.github.io/VideoView-Website/

This is a project website, not the Windows software itself. **Native Windows startup/playback and installation tests have not yet been completed**, per the QA report. Do not call this a stable/verified release without completing the Windows test checklist.

See [deployment guide](DEPLOYMENT_GUIDE.md) for alternate hosts and website deployment.
