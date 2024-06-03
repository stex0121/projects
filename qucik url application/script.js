const bookMarkForm = document.getElementById("bookmarkForm");
const siteNameInput = document.getElementById("siteName");
const siteUrlInput = document.getElementById("siteUrl");
const bookmarkList = document.getElementById("bookmarkList");

bookMarkForm.addEventListener("submit", addBookmark);

function addBookmark(event) {
    event.preventDefault();

    const siteName = siteNameInput.value;
    const siteUrl = siteUrlInput.value;
    if (!validateForm(siteName, siteUrl)) {
        return;
    }
    if (isDuplicateBookmark(siteName, siteUrl)) {
        alert("This bookmark already exists");
        return;
    }

    const bookmark = {
        name: siteName,
        url: siteUrl,
    };
    displayBookmark(bookmark);
    saveBookmark(bookmark);
    siteNameInput.value = "";
    siteUrlInput.value = "";
}

function validateForm(siteName, siteUrl) {
    if (!siteName || !siteUrl) {
        alert("Please fill in both fields.");
        return false; // Added return false to prevent form submission
    }
    return true; // Added to ensure the function always returns a value
}

function displayBookmark(bookmark) {
    const bookmarkItem = document.createElement("li");
    const link = document.createElement("a");
    link.href = bookmark.url;
    link.textContent = bookmark.name;
    link.target = "_blank";
    const removeButton = document.createElement("button");
    removeButton.innerHTML = '<i class="fas fa-trash-alt"></i>';
    removeButton.addEventListener("click", () => removeBookmark(bookmark));
    bookmarkItem.appendChild(link); // Fixed the typo here
    bookmarkItem.appendChild(removeButton);
    bookmarkList.appendChild(bookmarkItem);
}

function isDuplicateBookmark(siteName, siteUrl) {
    let bookmarks = getBookmarks();
    return bookmarks.some(
        (bookmark) =>
            bookmark.name.toLowerCase() === siteName.toLowerCase() &&
            bookmark.url.toLowerCase() === siteUrl.toLowerCase()
    );
}

function saveBookmark(bookmark) {
    let bookmarks = getBookmarks();
    bookmarks.push(bookmark);
    localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
}

function getBookmarks() {
    return JSON.parse(localStorage.getItem("bookmarks")) || [];
}

function displayBookmarks() {
    let bookmarks = getBookmarks();
    bookmarks.forEach((bookmark) => {
        displayBookmark(bookmark);
    });
}

function removeBookmark(bookmark) {
    let bookmarks = getBookmarks();
    bookmarks = bookmarks.filter(
        (b) =>
            b.name.toLowerCase() !== bookmark.name.toLowerCase() ||
            b.url.toLowerCase() !== bookmark.url.toLowerCase()
    );
    localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
    clearBookmarkskList();
    displayBookmarks(); // Corrected function call
}

function clearBookmarkskList() {
    bookmarkList.innerHTML = ""; // Fixed the assignment operator
}

// Call displayBookmarks when the page loads
window.addEventListener("load", displayBookmarks);