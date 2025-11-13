document.querySelectorAll('.delete-form').forEach(form => {
    form.addEventListener('submit', function (e) {
        if (!confirm('Удалить задачу?')) {
            e.preventDefault(); // Отмена отправки
        }
    });
});
