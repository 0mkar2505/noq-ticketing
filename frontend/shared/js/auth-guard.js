// Auth guard - redirect to login if not authenticated
const token = localStorage.getItem("token");

if (!token) {
  window.location.href = "/auth/login.html";
} else {
  try {
    const payload = JSON.parse(atob(token.split(".")[1]));
    const currentPath = window.location.pathname;

    // Enforce role-based access
    if (currentPath.startsWith("/app/admin")) {
      if (payload.role !== "admin") {
        window.location.href = "/auth/login.html";
      }
    } else if (currentPath.startsWith("/app/client")) {
      if (payload.role !== "client") {
        window.location.href = "/auth/login.html";
      }
    }

    // Store user info for shared components
    localStorage.setItem("user", JSON.stringify(payload));
  } catch (e) {
    localStorage.removeItem("token");
    window.location.href = "/auth/login.html";
  }
}
