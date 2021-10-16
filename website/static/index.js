function deleteReminder(id) {
  fetch("/delete-reminder", {
    method: "POST",
    body: JSON.stringify({ id }),
  }).then((response) => {
    window.location.href = "/";
  });
}
