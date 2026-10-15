# VideoView Website — Deployment Guide
**Current hosting:** VideoView's official production website is on Vercel, with GitHub providing source control and Releases. GitHub Pages instructions are obsolete for `videoview.online`.


## 1. Which package should I use?

- **VideoView-Website-Only.zip**: just the HTML/CSS/JS site, imagery, license notices, and small text assets. Recommended with GitHub Releases for the large software downloads.
- **VideoView-Website-Full.zip**: same website plus installer, portable ZIP, application source, and third-party source ZIP; intended for a server or shared host that accepts files over 100 MB and supports the necessary storage/bandwidth.

The app release is **1.1.0 (release candidate)**, not verified on native Windows. The release notes and QA report explain the remaining checks.

## 2. Option A — shared hosting / cPanel (simplest for an existing domain)

1. Buy or use shared hosting with static-file hosting, enough quota for **at least 300 MB** of files plus expected download bandwidth, and permission to serve `.exe` and `.zip` downloads.
2. Add a domain and enable SSL/HTTPS in the hosting dashboard.
3. Extract `VideoView-Website-Full.zip` on your computer.
4. Upload the **contents of the extracted `VideoView-Website` folder** to the domain's `public_html` (or equivalent document-root folder), not the folder itself.
5. Confirm `public_html/index.html` exists and the large files sit in `public_html/downloads/`.
6. Open `https://your-domain.example/` and `https://your-domain.example/downloads.html` and click every download.
7. If downloads fail, contact the host about file-size limits, MIME types, bandwidth limits, or blocked executables. A shared-host upload form may impose an upload cap even if the server can ultimately host the file; SFTP may be an alternative.

**No PHP, MySQL, Node.js, or framework is required.**

## 3. Option B — GitHub Releases + Cloudflare Pages (good static hosting architecture)

### Upload the release binaries to GitHub Releases

1. Create or choose a public GitHub repository for VideoView.
2. Open its **Releases → Draft a new release** screen.
3. Create tag `v1.1.0` and name it `VideoView 1.1.0 — Release Candidate`.
4. Upload these files **with exact, unmodified names**:
   - `VideoView-Setup.exe`
   - `VideoView-Portable.zip`
   - `VideoView-Source.zip`
   - `VideoView-ThirdPartySources.zip`
   - `SHA256SUMS.txt`
   - `RELEASE_NOTES.txt`
   - `QA_REPORT.md`
   - `WINDOWS_TEST_CHECKLIST.md`
5. State clearly in the release body that clean native Windows testing is pending; include source licenses and notices.
6. Publish the release, then copy its release-asset base URL. The URL generally resembles `https://github.com/YOUR-USERNAME/YOUR-REPO/releases/download/v1.1.0/`. Confirm by opening a real asset URL, rather than assuming its spelling.

### Set up the download links

Open `assets/js/download-config.js` in the website-only files. Set only `baseUrl` to the actual GitHub release asset base URL, including trailing slash. The JS automatically changes all eight download/documentation links on the site. The site supports a subpath such as `username.github.io/repo/` because its page and CSS links are relative.

### Publish the site on Cloudflare Pages

1. Log in to Cloudflare, choose **Workers & Pages → Create → Pages** (UI wording may vary).
2. Choose Git integration for a repository containing **only the website-only files**, or use direct upload.
3. No build command is needed; publish the folder containing `index.html` as the output directory. In many setups this is the repository root (often represented as `.`).
4. Deploy and visit the generated `*.pages.dev` URL.
5. To use a custom domain, add it through the Cloudflare Pages custom-domain settings and follow the DNS records Cloudflare gives you.
6. Check file buttons and SHA-256 against the downloaded binary.

**Important:** Cloudflare Pages limits individual static site files to **25 MiB**, so do **not** upload the full site with large `.exe` / `.zip` assets to Pages. Keep those on GitHub Releases or another large-file delivery service.

## 4. Current production hosting — Vercel + GitHub Releases

**The official VideoView website is hosted on Vercel, not GitHub Pages.** GitHub stores its source and download release assets; Vercel deploys from the `main` branch of `premangshumal-cyber/VideoView-Website`.

- Vercel project: https://vercel.com/premangshu/videoview-website
- Preferred domain: https://www.videoview.online/
- Apex domain: https://videoview.online/ (308 redirect to WWW)
- DNS provider: BigRock (registrar-level authoritative nameservers are `dns1.bigrock.in` to `dns4.bigrock.in`).
- Vercel's project-specific WWW CNAME target: `b6f8e486dfa12b84.vercel-dns-017.com`.
- Vercel's preferred apex A records at the time of migration: `216.198.79.1`, `64.29.17.1`. Follow Vercel project settings if these are changed in future.

**Do not point the official domain to GitHub Pages or re-create the former GitHub `CNAME` file.** The GitHub Pages-only `.nojekyll` file was also removed. The site's `index.html`, other assets, source code and GitHub Releases must remain, because they power the active Vercel website and its downloads.

If GitHub Pages is still enabled in GitHub's repository settings, its administrator should open **Settings → Pages**, choose **Unpublish site**, and disable Pages publishing (for example set the deployment branch to **None**, when shown). The connected GitHub tool cannot alter repository Pages configuration directly.

### Troubleshooting old GitHub Pages 404/invalid TLS after migration

An old resolver can still direct `www.videoview.online` to `premangshumal-cyber.github.io` or IPv4 `185.199.108.153`–`185.199.111.153` / IPv6 `2606:50c0:8000::153` etc. Deleting files or unpublishing GitHub Pages **does not clear upstream DNS caches**.

Compare the default system DNS with public resolvers:
```powershell
nslookup -type=CNAME www.videoview.online
nslookup -type=CNAME www.videoview.online 1.1.1.1
nslookup -type=CNAME www.videoview.online 8.8.8.8
Get-DnsClientServerAddress
```
If only the default resolver returns `premangshumal-cyber.github.io`, correct that resolver or its upstream network. Do not continue deleting website source files.

## 5. Local preview and tests

On Windows, install Python if you don't already have it. From the extracted website folder:

```powershell
py -m http.server 8000
```

Open `http://localhost:8000/` in your browser. Website-only local downloads of `.exe`/`.zip` will not work until the binary files have been copied into `downloads/` or a valid `baseUrl` has been configured.

Verify the 4 release binaries after downloading with PowerShell:

```powershell
Get-FileHash .\VideoView-Setup.exe -Algorithm SHA256
```

Compare the output with `downloads/SHA256SUMS.txt`. You should receive exactly the published hashes. Make sure your deployed host hasn't renamed or altered the file bytes.

## 6. Before publishing a production site

- Run `WINDOWS_TEST_CHECKLIST.md` on clean Windows 10 and Windows 11 x64 test systems; record observed behavior.
- If this becomes a stable product release, update all release-candidate descriptions and QA status **only when verified**.
- Consider Windows code signing; the current installer is unsigned and may show unknown-publisher prompts.
- Replace generic business identity/contact wording with your real details, and review legal/privacy requirements.
- Turn on HTTPS, backups and ordinary hosting security updates; do not expose admin credentials in JavaScript.
- Test responsive layout, keyboard menu navigation, screen-reader labels, browser downloads, links, and QR/marketing redirects if added later.
- Put a meaningful malware/reputation scanning process in place before widely distributing executables.

## Source references for hosting limits (checked 12 October 2026)

- GitHub repository single-file limits: https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits
- GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Cloudflare Pages single-file cap: https://developers.cloudflare.com/pages/platform/limits/