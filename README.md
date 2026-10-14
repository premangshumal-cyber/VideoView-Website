# VideoView website
Premium dark-navy and teal static website for **VideoView 1.1.0 (Windows x64 release candidate)**.

## Official domain (DNS and GitHub Pages activation pending)
https://videoview.online/

The repository root `CNAME` file is set to `videoview.online`.

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

Expected custom-domain URL: https://videoview.online/ (after DNS and Pages verification).

### DNS setup at your domain registrar
Create four A records for host `@` pointing to:
- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

Add a CNAME record for host `www` pointing to `premangshumal-cyber.github.io` (without the repository suffix). Remove conflicting old parking/forwarding A, AAAA, or CNAME records for these hostnames. Do not delete unrelated MX or TXT records.

In GitHub Pages settings, confirm the **Custom domain** is `videoview.online` and save if necessary. When DNS validation and the TLS certificate finish, enable **Enforce HTTPS**. DNS propagation can take up to 24 hours.

This is a project website, not the Windows software itself. **Native Windows startup/playback and installation tests have not yet been completed**, per the QA report. Do not call this a stable/verified release without completing the Windows test checklist.

See [deployment guide](DEPLOYMENT_GUIDE.md) for alternate hosts and website deployment.

## Android app publishing status

An Android APK named `VideoView-Android-1.0.0(1).apk` was provided in the ChatGPT conversation (approximately 4.3 MiB); this repository **does not yet contain a public Android APK release**. The package's application ID, Android version requirements, signing and runtime behavior have not been verified.

The website now includes an Android feature callout and an Android download card, explicitly marked **release pending**. Do not replace that status with a download link until a public GitHub Release asset actually exists.

### Finish Android release upload

1. Rename a copy of the provided APK to `VideoView-Android-1.0.0.apk` (do not modify the APK content).
2. In this GitHub repository, go to **Releases → Draft a new release**.
3. Use tag `android-v1.0.0` and title `VideoView Android 1.0.0 — Pre-release`. Select **Pre-release** until Android testing is complete.
4. Add brief testing/compatibility notes and upload `VideoView-Android-1.0.0.apk` under **Attach binaries**.
5. Publish, confirm the asset is really present, then set `android.url` in `assets/js/download-config.js` to the **confirmed asset URL**. The website switches the Android button to **Download Android APK** automatically.
6. Optionally add a verified SHA-256 for the Android APK once its bytes can be independently checked.

Windows installer links are unaffected.
