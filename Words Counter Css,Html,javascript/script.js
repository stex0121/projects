document.addEventListener("DOMContentLoaded", function() {

    const input = document.querySelector("textarea");
    const characterCount = document.querySelector("#characterCount"); // Add '#' to select by ID
    const wordCount = document.querySelector("#wordCount"); // Add '#' to select by ID
    const sentenceCount = document.querySelector("#sentenceCount"); // Add '#' to select by ID

    input.addEventListener("input", function() {

        const text = input.value.trim();

        characterCount.textContent = text.length;

        const words = text.split(/\s+/).filter(word => word.length > 0);
        wordCount.textContent = words.length;

        // You might want to refine this regex for better sentence splitting
        const sentences = text.split(/[.!?]+/).filter(sentence => sentence.length > 0);

        sentenceCount.textContent = sentences.length;
    });
});