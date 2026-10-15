# VideoView website
Premium dark-navy and teal static website for **VideoView 1.1.0 (Windows x64 release candidate)**.

## Official production website — Vercel

- Domain: https://videoview.online/
- Preferred domain: https://www.videoview.online/ (Vercel redirect from apex, 308)
- Vercel project: https://vercel.com/premangshu/videoview-website
- GitHub `main` is the deployment source.
- DNS is hosted by **BigRock** (authoritative nameservers: `dns1.bigrock.in` through `dns4.bigrock.in`).
- The obsolete GitHub Pages root `CNAME` file was removed because this site is now hosted on Vercel.

**Domain DNS configuration:** Use the project-specific addresses Vercel currently recommends, not GitHub Pages IPs. In BigRock's DNS management panel:
1. For host `@`, retain/create two **A** records: `216.198.79.1` and `64.29.17.1` (Vercel's current preferred pair).
2. For host `www`, use one **CNAME** record to `b6f8e486dfa12b84.vercel-dns-017.com`.
3. Remove former GitHub Pages `@ A` records (`185.199.108.153` to `185.199.111.153`), and `www` records pointing to `premangshumal-cyber.github.io`. Remove conflicting `www` A/AAAA/CNAME records so only the correct Vercel CNAME remains.
4. Preserve unrelated MX/TXT records (email verification, SPF/DKIM/DMARC) and NS records. If the project later displays different Vercel DNS recommendations, follow the updated Vercel domain settings.
5. After DNS propagation, verify both domain names in **Vercel → Project → Settings → Domains** and check that HTTPS certificates are valid.

**Do not reactivate GitHub Pages custom-domain hosting for this domain.** GitHub is used for source control and binary GitHub Releases, while Vercel serves the website.

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

## Deployment and TLS

GitHub commits to `main` deploy automatically through the connected Vercel project. Vercel has verified both project domain names, but certificates and routing require correct DNS at the authoritative BigRock nameservers.

If you receive `NET::ERR_CERT_COMMON_NAME_INVALID` for `www.videoview.online`, first remove mixed GitHub Pages records, wait for propagation, and allow Vercel to issue the correct certificate. Do not bypass the browser's HTTPS warning. For live troubleshooting, open Vercel → Project → **Settings → Domains**.

This is a project website, not the Windows software itself. **Native Windows startup/playback and installation tests have not yet been completed**, per the QA report. Do not call this a stable/verified release without completing the Windows test checklist.

See [deployment guide](DEPLOYMENT_GUIDE.md) for alternate hosts and website deployment.

## Android download (published)

Android v1.0.0 is available as a public **pre-release**, tagged `android-v1.0.0`.

- [Download VideoView Android 1.0.0 APK](https://github.com/premangshumal-cyber/VideoView-Website/releases/download/android-v1.0.0/VideoView-Android-1.0.0.apk)
- GitHub Release: https://github.com/premangshumal-cyber/VideoView-Website/releases/tag/android-v1.0.0
- Exact asset name: `VideoView-Android-1.0.0.apk`
- Asset size: 4,491,951 bytes
- SHA-256 digest (reported by GitHub): `31f97cb3575388b4ab47dc1ee91a0ab6372353df06460a4ec074d8fa0439967f`

The Android download button in `downloads.html` now points to the published asset, and `assets/js/download-config.js` is configured with the same verified URL. The Windows v1.1.0 download links are unchanged.

**Note:** Publication does not constitute security or functionality testing. Minimum supported Android version, package identity, signing certificate and runtime playback have not been independently verified.
