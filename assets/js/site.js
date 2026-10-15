"use strict";
document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("[data-nav]");
  const toggle = document.querySelector("[data-nav-toggle]");
  function setNav(open) {
    if (!nav || !toggle) return;
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
  }
  if (nav && toggle) {
    toggle.closest(".site-header")?.classList.add("nav-ready");
    toggle.addEventListener("click", () => setNav(!nav.classList.contains("is-open")));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && nav.classList.contains("is-open")) { setNav(false); toggle.focus(); } });
    nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => setNav(false)));
  }
  document.querySelectorAll("[data-year]").forEach(el => el.textContent = new Date().getFullYear());
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.body.classList.add("js-reveal");
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, {threshold:0.08,rootMargin:"0px 0px 30px 0px"});
    document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
  }
  const toast = document.querySelector("[data-toast]");
  let toastTimer;
  function announce(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 2500);
  }
  document.querySelectorAll("[data-copy]").forEach(btn => {
    btn.addEventListener("click", async () => {
      const value = btn.getAttribute("data-copy") || "";
      try {
        await navigator.clipboard.writeText(value);
        announce("SHA-256 checksum copied");
      } catch (e) {
        const field = document.createElement("textarea");
        field.value = value;
        field.style.position = "fixed"; field.style.opacity = "0";
        document.body.append(field);field.select();
        const copied = document.execCommand("copy");
        field.remove();
        announce(copied ? "SHA-256 checksum copied" : "Select the checksum text to copy");
      }
    });
  });
  const androidDownload = document.querySelector("[data-android-download]");
  if (androidDownload && window.VideoViewDownloadConfig?.android) {
    const a = window.VideoViewDownloadConfig.android;
    if (typeof a.url === "string" && /^https:\/\//i.test(a.url)) {
      androidDownload.href = a.url;
      androidDownload.textContent = "Download Android APK";
      androidDownload.classList.remove("btn-secondary");
      androidDownload.classList.add("btn-primary");
      androidDownload.removeAttribute("download");
    } else {
      androidDownload.href = a.releasePage;
      androidDownload.textContent = "View Releases (APK pending)";
      androidDownload.removeAttribute("download");
    }
  }
  const cfg = window.VideoViewDownloadConfig;
  if (cfg && cfg.files) {
    const files = cfg.files;
    const hosted = typeof cfg.baseUrl === "string" && /^https:\/\//i.test(cfg.baseUrl);
    const software = new Set(["setup","portable","source","thirdparty"]);
    document.querySelectorAll("[data-download]").forEach(a => {
      const key = a.getAttribute("data-download");
      if (!Object.prototype.hasOwnProperty.call(files,key)) return;
      if (hosted && software.has(key)) {
        a.href = cfg.baseUrl.replace(/\/?$/, "/") + encodeURIComponent(files[key]);
        a.removeAttribute("download");
        a.rel = "noopener noreferrer";
      } else if (software.has(key)) {
        a.href = cfg.releasePage;
        a.removeAttribute("download");
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.title = "Visit GitHub Releases. Software assets are not yet published.";
        const txt = [...a.childNodes].findLast(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim());
        if (txt) txt.textContent = "View GitHub Releases";
      } else {
        a.href = "downloads/" + files[key];
      }
    });
    if (!hosted && document.body.classList.contains("page-downloads")) {
      const main = document.querySelector(".download-main");
      if (main) {
        const box = document.createElement("div");
        box.className = "notice";
        const p = document.createElement("p");
        p.textContent = "Release downloads are being prepared. The software archives are not yet hosted on GitHub. The buttons below open the GitHub Releases page; the test reports and checksums are available now.";
        box.append(p);main.prepend(box);
      }
    }
  }
});
