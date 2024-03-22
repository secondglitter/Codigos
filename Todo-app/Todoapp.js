function LinkedList() {
    this.head = null;
    this.tail = null;
}

function Node(id, description, status, next, prev) {
    this.id = id;
    this.description = description;
    this.status = status;
    this.next = next;
    this.prev = prev;
}

LinkedList.prototype.addToHead = function (id, description, status) {
    const newNode = new Node(id, description, status, this.head, null);
    if (this.head) {
        this.head.prev = newNode;
    } else {
        this.tail = newNode;
    }
    this.head = newNode;
};

LinkedList.prototype.addToTail = function (id, description, status) {
    const newNode = new Node(id, description, status, null, this.tail);
    if (this.tail) {
        this.tail.next = newNode;
    } else {
        this.head = newNode;
    }
    this.tail = newNode;
};

LinkedList.prototype.removeHead = function () {
    if (!this.head) return null;
    const removedHead = this.head;
    this.head = this.head.next;
    if (this.head) {
        this.head.prev = null;
    } else {
        this.tail = null;
    }
    return removedHead;
};

LinkedList.prototype.removeTail = function () {
    if (!this.tail) return null;
    const removedTail = this.tail;
    this.tail = this.tail.prev;
    if (this.tail) {
        this.tail.next = null;
    } else {
        this.head = null;
    }
    return removedTail;
};

LinkedList.prototype.removeNode = function (id) {
    let currentNode = this.head;

    while (currentNode) {
        if (currentNode.id === id) {
            if (currentNode === this.head) {
                return this.removeHead();
            }
            if (currentNode === this.tail) {
                return this.removeTail();
            }

            const prevNode = currentNode.prev;
            const nextNode = currentNode.next;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;

            return currentNode;
        }
        currentNode = currentNode.next;
    }

    return null;
};

LinkedList.prototype.printTasks = function () {
    const pendingList = document.getElementById('pending-tasks');
    const completedList = document.getElementById('completed-tasks');
    const pendingCount = document.getElementById('pending-count');
    const completedCount = document.getElementById('completed-count');
    pendingList.innerHTML = '';
    completedList.innerHTML = '';
    pendingCount.textContent = 0;
    completedCount.textContent = 0;

    let currentNode = this.head;

    while (currentNode) {
        const listItem = document.createElement('li');
        listItem.textContent = `${currentNode.id}, Tarea: ${currentNode.description}`;
        if (currentNode.status === 1) {
            pendingList.appendChild(listItem);
            pendingCount.textContent = parseInt(pendingCount.textContent) + 1;
        } else if (currentNode.status === 2) {
            completedList.appendChild(listItem);
            completedCount.textContent = parseInt(completedCount.textContent) + 1;
        }

        currentNode = currentNode.next;
    }
};


const taskList = new LinkedList();

// Agregar tarea
document.addEventListener('DOMContentLoaded', function() {
const addTaskButton = document.getElementById('add-task-button');
addTaskButton.addEventListener('click', () => {
    const idInput = document.getElementById('add-task-id');
    const descriptionInput = document.getElementById('add-task-description');
    const statusSelect = document.getElementById('add-task-status');

    const id = idInput.value;
    const description = descriptionInput.value;
    const status = parseInt(statusSelect.value);

    if (id && description && (status === 1 || status === 2)) {
        taskList.addToTail(id, description, status);
        taskList.printTasks();
        alert("Se ha creado la tarea");
        idInput.value = '';
        descriptionInput.value = '';
        statusSelect.selectedIndex = 0;
    }
});
});

// Eliminar tarea
document.addEventListener('DOMContentLoaded', function() {
const removeTaskButton = document.getElementById('remove-task-button');
removeTaskButton.addEventListener('click', () => {
    const idInput = document.getElementById('remove-task-id');
    const id = idInput.value;

    if (id) {
        taskList.removeNode(id);
        taskList.printTasks();
        alert("Tarea eliminada");
        idInput.value = '';
    }
});
});

//Tarea como completada
document.addEventListener('DOMContentLoaded', function() {
const completeTaskButton = document.getElementById('complete-task-button');
completeTaskButton.addEventListener('click', () => {
    const idInput = document.getElementById('complete-task-id');
    const id = idInput.value;

    if (id) {
        const node = taskList.removeNode(id);
        if (node) {
            node.status = 2;
            taskList.addToTail(node.id, node.description, node.status);
            taskList.printTasks();
            alert("Se ha completado la tarea");
            idInput.value = '';
        }
    }
});
});

