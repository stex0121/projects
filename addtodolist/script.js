const todoList = document.getElementById("toDoList");
const newTodoInput = document.getElementById("newToDoInput");
const addTodoBtn = document.getElementById("addToDoBtn");

addTodoBtn.addEventListener("click", () => {
    const newtodoText = newTodoInput.value.trim(); // trim to remove leading/trailing whitespace

    if (newtodoText !== "") {
        const newtoDoItem = document.createElement("li");
        newtoDoItem.innerText = newtodoText;

        const deleteToDoBtn = document.createElement("button");
        deleteToDoBtn.innerText = "X";
        deleteToDoBtn.classList.add("delete-todo-btn");

        deleteToDoBtn.addEventListener("click", function () {
            newtoDoItem.remove();
        });

        newtoDoItem.appendChild(deleteToDoBtn);
        todoList.appendChild(newtoDoItem);
        newTodoInput.value = ""; // clear input field after adding todo
    }
});