(function () {
  const token = localStorage.getItem("token");

  if (!token) {
    window.location.href = "../../auth/login.html";
    return;
  }

  try {
    const payload = JSON.parse(atob(token.split(".")[1]));
    const path = window.location.pathname;

    // Admin pages protection
    if (path.includes("/admin/") && payload.role !== "admin") {
      localStorage.removeItem("token");
      window.location.href = "../../auth/login.html";
    }

    // Client pages protection
    if (path.includes("/client/") && payload.role !== "client") {
      localStorage.removeItem("token");
      window.location.href = "../../auth/login.html";
    }

  } catch {
    localStorage.removeItem("token");
    window.location.href = "../../auth/login.html";
  }
})();
