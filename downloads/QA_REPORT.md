# VideoView 1.1.0 — release candidate QA

Date: 2026-10-12. Target: Windows x64. **Actual compiled application and installer;
native Windows startup/playback/UI and installation remain unverified.**

## Build and package evidence

- Ubuntu 24.04 x64; writable workspace and successful official tool/package
  downloads. No Windows desktop/runtime, PowerShell, or Inno Setup execution.
- .NET SDK 10.0.401; Release WPF compilation and self-contained win-x64 publication.
  Actual output is in `build.log`/`publish.log`. No compiler warnings/errors.
- 59 core assertions pass: settings atomic storage/recovery, invalid preferences,
  old-schema migration, resume/history, Unicode/playlist paths, shuffle/repeat,
  group reorder/current identity, metadata sorting/filtering, bounded recursive
  import, timeline math and control-hiding policy. Evidence: `tests.log`.
- .NET/Windows Desktop 10.0.12, LibVLCSharp 3.10.1, native x64 VLC 3.0.24 and
  321 plugins packaged. Static verification checks required files, native PE
  architecture, runtime configuration, imports and payload SHA-256. Counts and
  imported system DLLs are in `dependency-verification.json`.
- NSIS 3.09 creates the real per-user setup. Its 32-bit bootstrapper installs an
  AMD64 payload. `installer-build.log` contains actual compiler output.
- `package-verification.json` records setup extraction and portable ZIP comparison
  against every file in the payload manifest. This checks bytes, not execution.
- Bash release script executed; PowerShell equivalent supplied but unexecuted.
  Exact sizes and checksums are in Release/ARTIFACTS.json and SHA256SUMS.txt.

## Playback scope

The headless harness links the production PlaybackService and uses Linux VLC
3.0.20, software decode, memory video output and dummy audio. The bundled Windows
engine is 3.0.24. Linux results cannot certify Windows behavior.

The harness checks synthetic Unicode/spaced H.264/AAC MP4, MKV remux, VP9/Opus
WebM, short 3840×2160 H.264, PCM WAV and FLAC. It exercises pause/resume, seeking,
all eleven rate setters, stop/start-time resume, delay setters, external subtitle
track discovery (SRT/VTT/ASS/SSA), eight open/seek/stop cycles, end event and
missing-file errors. See `PlaybackSmoke/results.json` and `playback-smoke.log`
for the current run. Callback counts and snapshot existence alone do not prove
correct rendering; actual images and independent comparison are separate evidence.

An earlier run in this conversation failed snapshot capture after rapid rate/seek
changes. Waiting for fresh playback and pausing before capture succeeded; the
result matched an independently decoded source frame pixel for pixel. The temporary
workspace then reset. The harness and fixtures were restored and rerun for this
release; current raw evidence is included. Native converter/decoder warnings during
initialization and rapid stops remain in logs; sample frames can be delivered via
fallback. Rate acceptance does not guarantee smooth 4× or sustained 4K playback.

Subtitle tests establish discovered tracks only, not glyph rendering/style or
synchronization quality. Dummy audio establishes clock/track behavior, not audible
sound, volume/mute or hardware devices. No sustained playback/memory-leak test,
multi-audio switching or native Windows GUI run was performed.

## Remaining acceptance and limitations

- Published Windows startup/shutdown, actual D3D rendering/audio, GPU acceleration,
  screenshots, fullscreen, mini mode, rotation, resize/minimize and multi-monitor DPI.
- WPF pointer/keyboard/focus, drag/drop/reorder, theme appearance, accessibility,
  shell thumbnails, device selection and native file dialogs.
- Explorer/Open With and same-user pipe forwarding, Windows file permissions,
  unavailable shares, corrupt-media recovery and real Windows settings persistence.
- Install/uninstall/reinstall/upgrade and clean-machine dependency execution.
  Source preserves user data and deletes only enumerated installed files.
- No code signing; unknown-publisher prompts are possible. Portable deployment
  requires all extracted files and uses LocalAppData, not an isolated USB profile.
- Cached shell thumbnails only; no timeline frame previews. Buffer percentage
  does not represent buffered timeline coverage. External subtitle paths/track
  choices are per-session. URLs, DRM, casting and disc-menu workflows are out of scope.
- Rotation uses software decode. Hardware-dependent high rates may drop frames.
  Inaccessible UNC requests may wait for Windows timeouts. Imports cap at 10,000.
- Third-party source ZIP includes VLC/LibVLCSharp and contrib recipes, not every
  transitive source tarball; source links and license notices are supplied.

## Acceptance gates

| Gate | Result |
| --- | --- |
| Actual Windows EXE / Release build | PASS; compiler and PE evidence |
| Published Windows app starts | NOT TESTED |
| Windows playback | NOT TESTED; Linux diagnostics have narrower scope |
| Runtime/native libraries | PASS static inventory; execution unverified |
| Third-party notices | Included in source and payload |
| Actual setup and matching contents | Compiled; extraction/hash report supplied |
| Installation/uninstallation | NOT TESTED |
| Data handling | Core tests pass; native upgrade test pending |
| Sizes/checksums/source/build scripts | Included in Release |

Minimum remaining action: run `WINDOWS_TEST_CHECKLIST.md` on a clean Windows x64
VM with no separately installed .NET or VLC. Correct any failure before describing
this as production-ready or clean-machine verified. Previous Wine launch attempts
were blocked by `wineserver: socket: Operation not permitted`; no successful Wine
or Windows execution is claimed. No permission bypass was attempted.