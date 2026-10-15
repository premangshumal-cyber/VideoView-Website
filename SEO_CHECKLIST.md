# VideoView organic search operations

Reviewed 15 October 2026. Preferred URL: https://www.videoview.online/.

## Website implementation

- Keep all existing software release asset names, URLs, version tags and hashes intact.
- Eight substantive canonical pages: Home, Features, Downloads, Windows, Android, Help, Release Notes and Privacy.
- Static HTML download links work without JavaScript. Mobile navigation also has a no-script fallback.
- Sitemap and robots are at the root. `/index.html` permanently redirects to `/`.
- Page titles, descriptions, canonical URLs, breadcrumbs, social card and favicon assets are provided.
- SoftwareApplication entities use separate Windows/Android identities, accurate pre-release descriptions and direct release URLs. Original Windows licensing is linked to the published MIT text.
- There are no invented ratings. Google software rich-result eligibility requires a genuine rating or review; valid Schema.org data alone does not establish eligibility. Do not add fake values to satisfy a validator.
- FAQ content helps readers; this software site should not expect Google's restricted FAQ rich result.
- No visitor tracking, ad scripts, tracking cookies or paid services are required.

## Release gate

Run `python3 tools/verify_site.py` and `node --check assets/js/site.js` before publishing. Verify the intended Vercel project (`videoview-website`, team `premangshu`) and exact commit. After production reaches READY, GET every sitemap URL, robots.txt, the sitemap, images and download documents; check apex and index redirects, invalid-path 404s and all GitHub asset links. Inspect desktop/mobile layout, navigation, keyboard focus and checksum-copy behavior.

`tools/submit_indexnow.py` shows the URLs without sending. After a verified live update, run `python3 tools/submit_indexnow.py --submit` to notify participating engines. Its root verification text file must remain deployed. HTTP 200 means received; 202 means received with key validation pending. Neither proves crawling, indexing or ranking. Do not repeatedly submit unchanged pages.

## Google Search Console — account action remains

1. Sign in to the intended Google account and inspect existing properties first.
2. If absent, add the **Domain** property `videoview.online`.
3. Add only Google's exact new TXT verification record at BigRock. Retain existing Vercel A/CNAME, email TXT/MX and nameserver records. Do not replace unrelated records.
4. Verify ownership, then submit `https://www.videoview.online/sitemap.xml`.
5. Inspect `/`, `/downloads.html`, `/windows.html` and `/android.html`: record indexed status, last crawl, Google-selected canonical and live-test result. Request indexing where available.
6. Review Page indexing, Search results, Core Web Vitals, manual actions and security issues. Do not treat a search-engine `site:` query as conclusive indexing evidence.

If DNS cannot be changed, a URL-prefix property for `https://www.videoview.online/` can use the exact HTML verification file or meta tag provided by Google. It covers only that prefix; do not invent a verification token.

## Bing Webmaster Tools — account action remains

Sign in and inspect existing sites. Import the verified property from Search Console if convenient, or use Bing's supplied verification method. Submit the same sitemap, inspect the main pages, run Site Scan and review Search Performance. IndexNow notifications complement this setup; they do not create a Webmaster Tools account or verify a dashboard property.

## Query-to-page map

| Search intent | Primary page |
| --- | --- |
| VideoView / VideoView official website / VideoView media player | `/` |
| VideoView download / media player download | `/downloads.html` |
| VideoView Windows video player / for Windows / install on Windows | `/windows.html` |
| VideoView Android / VideoView APK / APK installation | `/android.html` |
| VideoView features / playlists / playback controls | `/features.html` |
| VideoView shortcuts / subtitles / formats / troubleshooting | `/help.html` (specific sections) |
| VideoView versions / release status | `/release-notes.html` |

The broad name overlaps Android's `android.widget.VideoView` API. Use “VideoView media player”, the official domain, platform name and publisher handle consistently. Do not imply affiliation with Google, Microsoft or VideoLAN. Do not claim unsupported search volume, trademark ownership, ratings or store publication.

## Free promotion sequence

1. Correct repository About: website `https://www.videoview.online/`; description “Official VideoView media-player website and pre-release downloads for Windows and Android.” Suggested topics: `videoview`, `media-player`, `video-player`, `windows`, `android`, `subtitles`, `playlist`.
2. Add the official website and guides to release descriptions. Preserve asset links and pre-release flags. Review related repositories before changing them.
3. Complete native installation/playback tests, then record real screenshots and a short demonstration. Existing site artwork is concept illustration, not test evidence.
4. Publish an original guide or launch note through the owner's accounts. Disclose ownership and the pre-release status. Read community rules before posting and seek moderator permission where required.
5. Prioritize an actual walkthrough and useful issue responses over directory submissions. Avoid paid links, fake reviews and repetitive announcements.

## Measurement without website tracking

Use Search Console and Bing reports first. Record a baseline after verification; export weekly during the first month and monthly afterward. Use the same date windows and country/device filters. Compare 28-day periods only when enough data exists.

Record: indexed pages out of eight submitted canonical pages; impressions; clicks; CTR; average position; branded query totals (contains `videoview` or `video view`); remaining non-branded queries; clicks to each platform/download page; and indexing errors. Query rows may omit anonymized searches, so segment totals need not equal whole-property totals. Average position is not a fixed rank.

No confirmed baseline exists until the account reports are accessible. Download-page clicks are not download counts. GitHub asset-download counts can be a coarse separate measure but do not attribute users, search sources, installations or successful playback. Do not label them organic conversions.

## Publication gates for future claims

Windows: complete clean-machine install/uninstall/upgrade, graphical playback/audio, GPU, subtitles, keyboard/accessibility and supported-OS tests. Android: verify APK identity, minimum SDK, architectures, certificate, permissions, upgrade signing continuity and actual device behavior. Only then publish stronger compatibility or stability claims. Keep application tests distinct from website QA.

## Primary references

- https://developers.google.com/search/docs/appearance/structured-data/software-app
- https://developers.google.com/search/docs/appearance/site-names
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/blog/2023/08/howto-faq-changes
- https://www.indexnow.org/documentation
- https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed
