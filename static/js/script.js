// Base JavasScript for functionality present on all pages.

// Declare constants:
const githubBtn = document.getElementById("github-btn");
const newPostBtn = document.getElementById("new-btn");

// Add event listeners:

// Source code button.
if (githubBtn) {
  githubBtn.addEventListener("click", () => {
    loadNewTab("https://github.com/OperaVaria/instant-serotonin");
  });
}

// New post button (ins practice -> reloads page).
if (newPostBtn) {
  newPostBtn.addEventListener("click", () => {
    window.location.reload(true);
  });
}

// General link buttons.
document.querySelectorAll(".link-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    loadPage(btn.getAttribute("data-target"));
  });
});

// Load a page, same tab.
function loadPage(page) {
  let safePage = encodeURI(page)
  window.location.href = safePage;
}

// Load a page in new tab.
function loadNewTab(page) {
  let safePage = encodeURI(page)
  window.open(safePage, "_blank");
}

// Reset alert box.
function resetAlert() {
  setTimeout(() => {
    alert("Content reset successful!");
  }, 1000);
}
