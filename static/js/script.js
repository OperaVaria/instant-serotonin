// Insert current year into copyright info.
let currentYear = new Date().getFullYear();
document.getElementById("yearVariable").innerHTML = currentYear;

// Load a page, same tab.
function loadPage(Page) {
    window.location.href = Page;
}  

// Load a page in new tab.
function loadNewTab(Page) {
    window.open(Page, "_blank");
}
