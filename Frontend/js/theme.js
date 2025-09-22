const root = document.documentElement;

function toggleTheme() {
  const current = root.getAttribute("data-theme");
  root.setAttribute("data-theme", current === "dark" ? "light" : "dark");
}

// Optional: attach theme toggle button later

document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("themeToggle");
  const htmlTag = document.documentElement;

  function updateButtonLabel() {
    if (htmlTag.getAttribute("data-theme") === "dark") {
      themeToggle.textContent = "🌙 Dark Mode";
    } else {
      themeToggle.textContent = "☀️ Light Mode";
    }
  }

  themeToggle.addEventListener("click", () => {
    const currentTheme = htmlTag.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    htmlTag.setAttribute("data-theme", newTheme);
    updateButtonLabel();
  });

  // initialize button text
  updateButtonLabel();
});
