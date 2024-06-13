function drag() {
    let dragging = null;
    let mouseX, mouseY;
    let eleX, eleY;
    const boxes = document.querySelectorAll("[draggable]");

    boxes.forEach(box => {
        box.addEventListener("mousedown", mouseDown);
        box.style.position = "relative"; // Set the position of draggable elements to relative
        box.style.cursor = "grab"; // Change cursor to grab when hovering over draggable elements
    });

    function mouseDown(e) {
        e.preventDefault();
        dragging = this;
        mouseX = e.pageX;
        mouseY = e.pageY;
        eleX = parseInt(dragging.style.left) || 0;
        eleY = parseInt(dragging.style.top) || 0;
        document.addEventListener("mousemove", mouseMove);
        document.addEventListener("mouseup", mouseUp);
    }

    function mouseMove(e) {
        if (dragging) {
            const deltamouseX = e.pageX - mouseX;
            const deltamouseY = e.pageY - mouseY;
            dragging.style.left = eleX + deltamouseX + "px";
            dragging.style.top = eleY + deltamouseY + "px";
        }
    }

    function mouseUp() {
        dragging = null;
        document.removeEventListener("mousemove", mouseMove);
        document.removeEventListener("mouseup", mouseUp);
    }
}

drag();