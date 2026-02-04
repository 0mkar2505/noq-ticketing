document.addEventListener("DOMContentLoaded", () => {
  const authToggle = document.getElementById("authToggleLink");

  if (!authToggle) return;

  const currentPage = window.location.pathname;

  if (currentPage.includes("login.html")) {
    authToggle.textContent = "Register";
    authToggle.href = "/auth/register.html";
  } else if (currentPage.includes("register.html")) {
    authToggle.textContent = "Log In";
    authToggle.href = "/auth/login.html";
  }
});
