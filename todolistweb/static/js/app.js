function showAddForm() {
    document.getElementById('add-form').style.display = 'block';
}

function hideAddForm() {
    document.getElementById('add-form').style.display = 'none';
}

function showCompleteForm() {
    document.getElementById('complete-form').style.display = 'block';
}

function hideCompleteForm() {
    document.getElementById('complete-form').style.display = 'none';
}

function deleteTask(taskId) {
    window.location.href = '/delete/' + taskId;
}