const form = document.getElementById("loginForm");
const errorEl = document.getElementById("error");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("http://localhost:5000/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok) {
      errorEl.innerText = data.error || "Login failed";
      return;
    }

    // Save JWT
    localStorage.setItem("token", data.token);

    // Decode payload
    const payload = JSON.parse(atob(data.token.split(".")[1]));

    // Redirect by role
    if (payload.role === "admin") {
      window.location.href = "../app/admin/dashboard.html";
    } else {
      window.location.href = "../app/client/dashboard.html";
    }

  } catch {
    errorEl.innerText = "Backend not reachable";
  }
});
