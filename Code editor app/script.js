function run() {
    let htmlCode = document.getElementById("html-code").value;
    let cssCode = document.getElementById("css-code").value;
    let jsCode = document.getElementById("javascript-code").value;
    let outputFrame = document.getElementById("output");

    let outputDocument = outputFrame.contentDocument || outputFrame.contentWindow.document;

    outputDocument.body.innerHTML = htmlCode;
    let styleTag = outputDocument.createElement("style");
    styleTag.innerHTML = cssCode;
    outputDocument.head.appendChild(styleTag);

    // Using new Function() to execute JavaScript
    let scriptTag = outputDocument.createElement("script");
    scriptTag.textContent = jsCode;
    outputDocument.body.appendChild(scriptTag);
}