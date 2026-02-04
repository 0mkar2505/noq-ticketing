/**
 * Smooth page transitions for same-origin links
 */
document.querySelectorAll("a").forEach(link => {
  if (link.href && link.origin === location.origin) {
    link.addEventListener("click", e => {
      // Skip if link has nohref="#" or is a download
      if (link.getAttribute("href") === "#" || link.download) return;
      
      e.preventDefault();
      document.body.style.opacity = "0";
      document.body.style.transition = "opacity 0.2s ease";
      
      setTimeout(() => {
        window.location = link.href;
      }, 200);
    });
  }
});
