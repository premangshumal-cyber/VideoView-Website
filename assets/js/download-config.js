/* VideoView GitHub release downloads.
   Once all assets are uploaded to a published release with tag v1.1.0,
   set baseUrl to:
   "https://github.com/premangshumal-cyber/VideoView-Website/releases/download/v1.1.0/"
   Until then, software buttons lead to the releases overview, not a missing EXE. */
window.VideoViewDownloadConfig = Object.freeze({
  baseUrl: "",
  releasePage: "https://github.com/premangshumal-cyber/VideoView-Website/releases",
  files: Object.freeze({
    setup: "VideoView-Setup.exe",
    portable: "VideoView-Portable.zip",
    source: "VideoView-Source.zip",
    thirdparty: "VideoView-ThirdPartySources.zip",
    checksums: "SHA256SUMS.txt",
    notes: "RELEASE_NOTES.txt",
    qa: "QA_REPORT.md",
    checklist: "WINDOWS_TEST_CHECKLIST.md"
  })
});
