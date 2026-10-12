# Windows acceptance — NOT EXECUTED

Use a standard-user Windows 11 x64 VM and a compatible Windows 10 x64 system.
Record OS/GPU/DPI, build SHA-256 and observations. Use a clean VM snapshot without
VLC/.NET installed. A checkbox needs observed evidence, not source inspection.

- [ ] Extract the full portable ZIP outside the source tree. Start and shut down.
- [ ] Play Unicode/spaced MP4, MKV, WebM, WAV, FLAC and supplied 4K sample.
      Confirm moving picture and audible tone; measure sustained 4K separately.
- [ ] Pause/resume/stop, seek by click/drag/keys, volume/mute/wheel, each speed.
- [ ] Open multiple files and nested folders. Drag/drop from Explorer. Add without
      replacing the queue; multi-select, drag reorder, move, remove, clear/cancel.
- [ ] Search/sort all keys, resize/collapse sidebar, verify current-item highlight,
      actual metadata and honest thumbnail fallback. Save/reload Unicode M3U8.
- [ ] Previous/next, shuffle, repeat off/one/all, auto-next/end and missing entries.
- [ ] Fullscreen double-click/F/F11/Esc; inactivity hide and mouse/key reveal.
      Mini mode/topmost, minimize/restore, resizing, multiple monitors and DPI.
- [ ] Track menus with multi-audio media; external SRT/VTT/ASS/SSA; inspect glyphs,
      enable/disable, auto-match, positive/negative delay, font/color/position.
- [ ] Aspect/fit/original/zoom/rotation; Automatic/D3D renderers, hardware on/off,
      device selection; verify reconfiguration preserves position/paused state.
- [ ] Screenshot PNG visually matches the video frame. Test capture after seeking.
- [ ] Restart to check theme, speed, volume, geometry, queue, resume and subtitles.
      Clear history, reset defaults and recover malformed JSON without data loss.
- [ ] Keyboard reference works; text boxes, dialogs and slider navigation unaffected.
      Inspect light/dark contrast, keyboard focus and screen-reader names.
- [ ] Command-line Unicode/space paths while closed and already open; one instance.
- [ ] Missing/moved/unsupported/corrupt files, permissions and unavailable UNC shares
      produce recoverable behavior. Do not delete or alter original media.
- [ ] Repeated/rapid open/seek/stop and long playback; inspect native resources/memory.
- [ ] Move portable directory; re-test without source/build tooling. In a test copy,
      remove an engine/plugin file and check the error, then restore from clean ZIP.
- [ ] Install as standard user; Start Menu/uninstall entry. Optional Desktop/Open With
      with existing defaults retained. Cancel installation and handle copy failures.
- [ ] Reinstall/upgrade; settings/playlists/media hashes preserved. Running-app guard.
- [ ] Uninstall: owned files/shortcuts removed, personal data and unlisted files kept.
- [ ] No telemetry/runtime downloads. User-selected UNC paths may use normal SMB.

Attach results and fix failures before marking native acceptance complete.