async function loadHTML(id, path) {
  const res = await fetch(path);
  const html = await res.text();
  document.getElementById(id).innerHTML = html;
}

// Determine which sidebar to load based on current path
const currentPath = window.location.pathname;
const isAdmin = currentPath.startsWith("/app/admin");

// Load navbar and appropriate sidebar
loadHTML("navbar", "/app/shared/navbar.html");
loadHTML("sidebar", isAdmin ? "/app/shared/sidebar-admin.html" : "/app/shared/sidebar-client.html");

// Set active sidebar link after sidebar is loaded
setTimeout(() => {
  document.querySelectorAll('.sidebar-nav a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  // Set user email in navbar
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  const userEmailEl = document.getElementById("userEmail");
  if (userEmailEl && user.email) {
    userEmailEl.textContent = user.email;
  }
}, 100);

// Logout handler
document.addEventListener('click', (e) => {
  if (e.target.id === 'logoutBtn') {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/auth/login.html';
  }
});
